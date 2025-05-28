from typing import List, Optional, Union
from datetime import date

class Usuario:
    def __init__(self, nome: str, saldo: float):
        self.nome: str = nome
        self.saldo: float = saldo
        self.operacoes: List[dict] = []

    def obter_dados(self) -> dict:
        return {'nome': self.nome, 'saldo': self.saldo}

    def registrar_compra(self, ticker: str, valor: float, data: date):
        self.operacoes.append({
            'operacao': 'compra',
            'ticker': ticker,
            'valor': valor,
            'data': data.isoformat()
        })

    def registrar_venda(self, ticker: str, valor: float, data: date):
        self.operacoes.append({
            'operacao': 'venda',
            'ticker': ticker,
            'valor': valor,
            'data': data.isoformat()
        })

    def obter_extrato(self) -> str:
        linhas = []
        for op in self.operacoes:
            linha = f"{op['data']}: {op['operacao']} do ativo {op['ticker']} no valor R${op['valor']:.2f}"
            linhas.append(linha)
        return "\n".join(linhas)
        

class PessoaJuridica(Usuario):
    def __init__(self, nome: str, cnpj: str, saldo: float):
        super().__init__(nome, saldo)
        self.cnpj: str = cnpj

    def obter_dados(self):
        dados = super().obter_dados()
        dados['cnpj'] = self.cnpj
        return dados

class PessoaFisica(Usuario):
    def __init__(self, nome: str, cpf: str, saldo: float):
        super().__init__(nome, saldo)
        self.cpf: str = cpf

    def obter_dados(self):
        dados = super().obter_dados()
        dados['cpf'] = self.cpf
        return dados

class Ativo:
    def __init__(self, ticker: str, emissor: PessoaJuridica, detentor: Usuario):
        self.ticker: str = ticker
        self.emissor: PessoaJuridica = emissor
        self.detentor: Usuario = detentor

    def pagar_provento(self, lucro: float, payout: float):
        provento = lucro * (payout / 100)
        self.detentor.saldo += provento

class Oferta:
    def __init__(self, ativo: Ativo, ofertante: Usuario, valor: float):
        self.ativo: Ativo = ativo
        self.ofertante: Usuario = ofertante
        self.valor: float = valor
        self.finalizada: bool = False

    def comprar(self, comprador: Usuario):
        if comprador.saldo >= self.valor and not self.finalizada:
            comprador.saldo -= self.valor
            self.ofertante.saldo += self.valor
            self.ativo.detentor = comprador
            comprador.registrar_compra(self.ativo.ticker, self.valor, date.today())
            self.ofertante.registrar_venda(self.ativo.ticker, self.valor, date.today())
            self.finalizada = True

class Cadastros:
    def __init__(self):
        self.ativos: List[Ativo] = []
        self.pessoas_fisicas: List[PessoaFisica] = []
        self.pessoas_juridicas: List[PessoaJuridica] = []

    def listar_tickers(self) -> List[str]:
        return [ativo.ticker for ativo in self.ativos]

class Pregao:
    def __init__(self, cadastros: Cadastros, data: date):
        self.cadastros: Cadastros = cadastros
        self.data: date = data
        self.ofertas: List[Oferta] = []

    def comprar_ativo(self, emissor: Usuario, ticker: str, valor_max: Optional[float] = None) -> Union[float, None]:
        for oferta in self.ofertas:
            if (not oferta.finalizada and 
                oferta.ativo.ticker == ticker and 
                (valor_max is None or oferta.valor <= valor_max)):
                oferta.comprar(emissor)
                return oferta.valor
        return None

    def calcular_cotacao(self, ativo: Ativo) -> float:
        valores = [oferta.valor for oferta in self.ofertas 
                   if oferta.ativo.ticker == ativo.ticker and oferta.finalizada]
        if valores:
            return sum(valores) / len(valores)
        return 0.0

    def oferta_publica_inicial(self, emissor: PessoaJuridica, ticker: str, valor: float, quantidade: int):
        for _ in range(quantidade):
            ativo = Ativo(ticker, emissor, emissor)
            self.cadastros.ativos.append(ativo)
            oferta = Oferta(ativo, emissor, valor)
            self.ofertas.append(oferta)
