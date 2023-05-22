import random
import string

tamanho_senha = int(input('Digite o tamanho da senha desejada: '))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = []
for i in range(tamanho_senha):
    senha.append(random.choice(caracteres))

senha_str = ''.join(senha)

print('Sua senha gerada é: ', senha_str)





