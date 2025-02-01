import re

def validar_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def validar_cpf(cpf):
    cpf_pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(cpf_pattern, cpf) is not None

# Solicita entrada do usuário
email = input("Digite seu e-mail: ")
cpf = input("Digite seu CPF (formato: 000.000.000-00): ")

# Validação
email_valido = validar_email(email)
cpf_valido = validar_cpf(cpf)

# Exibe resultados
if email_valido:
    print("E-mail válido.")
else:
    print("E-mail inválido.")

if cpf_valido:
    print("CPF válido.")
else:
    print("CPF inválido.")
