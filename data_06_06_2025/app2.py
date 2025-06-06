from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)
private_key = key.export_key()  
public_key = key.publickey().export_key()

message = b'Hello, world!'
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
ciphertext = cipher.encrypt(message)
print('Ciphertext:', ciphertext)

cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
plaintext = cipher.decrypt(ciphertext)
print('Plaintext:', plaintext)