from docxtpl import DocxTemplate

tabela = [
    {'nome': 'Pedro Henrique Santana Nascimento', 'email': 'pedrohenriquesn90@hotmail.com'},
    {'nome': 'John rodrigues neves teixeira', 'email': 'john@gmail.com'},
    {'nome': 'vacilda duarte albano', 'email': 'vania@gmail.com'}
]

template = DocxTemplate('tpl2.docx')

contexto = {
    'candidatos': tabela
}

template.render(contexto)
template.save('candidatos.docx')

print('Foi feito com Sucesso!')