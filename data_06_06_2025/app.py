from cryptography.fernet import Fernet

key = Fernet.generate_key()
print('Chave', key)

cipher_suite = Fernet(key)
mensagem = b'Ola, mundo!'

texto_codificado = cipher_suite.encrypt(mensagem) 
print(texto_codificado)
print('Codificado:', texto_codificado)

texto_decodificado = cipher_suite.decrypt(texto_codificado)
print('Decodificado:', texto_decodificado)