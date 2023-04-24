from socket import *
import os

portaServidor = 12000

socketServidor = socket(AF_INET, SOCK_STREAM)

socketServidor.bind(('', portaServidor))

socketServidor.listen(1)

print("O servidor está pronto para receber")

while True:
    socketConexao, endereco = socketServidor.accept()
    requisicao = socketConexao.recv(1024).decode()
    
    if requisicao.startswith('GET'):
        nome_arquivo = requisicao.split()[1]
        if nome_arquivo == '/':
            nome_arquivo = '/index.html'
            
        if os.path.isfile('.' + nome_arquivo):
            arquivo = open('.' + nome_arquivo, 'rb')
            resposta = arquivo.read()
            arquivo.close()
            cabecalho = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
        else:
            resposta = 'Arquivo não encontrado'.encode()
            cabecalho = 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n'
    else:
        resposta = 'Método não suportado'.encode()
        cabecalho = 'HTTP/1.1 405 Method Not Allowed\nContent-Type: text/plain\n\n'

    socketConexao.send(cabecalho.encode() + resposta)
    socketConexao.close()
