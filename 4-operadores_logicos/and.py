entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha:')

senha_permitda = '123456'
if entrada == 'E' and senha_digitada == senha_permitda:
    print('Entrar')
else:
    print('Sair')