from socket import *

nomeServidor = '127.0.0.1'
portaServidor = 12000

socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((nomeServidor, portaServidor))

requisicao = 'GET / HTTP/1.1\nHost: ' + nomeServidor + '\n\n'
socketCliente.send(requisicao.encode())

resposta = socketCliente.recv(4096).decode()

cabecalho, conteudo = resposta.split('\n\n', 1)
if cabecalho.split()[1] == '200':
    print(conteudo)
else:
    print('Erro ao receber a resposta do servidor')

socketCliente.close()
