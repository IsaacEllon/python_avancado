# HTTP (HyperText Transfer Protocol) é uma protocolo usado para enviar e
# receber dados na internet. Ele funciona no modo cliente/servidor, onde o
# cliente (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.

# A menagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#   - Leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (método suportados)
#   - Escrita - POST, PUT (substitui), PATCH (atualiza), DELETE (atualiza)
# O endereço do recurso a ser acessado (/users/)
# Os cabeçalhos HTTP (Content-Type, Authorization)
# O corpo da mensagem (caso necessário, de acordo com o método HTTP)

# A mensagem de resposta do servidor deve incluir dados como:
# - Código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

