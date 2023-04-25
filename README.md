# docker-atividade
Atividade de Docker da disciplina de laboratório de redes.

# Informações Aluno
- DENISSON SANTOS ALVES DE FREITAS
- Disciplina: COMP0463 - LABORATÓRIO DE REDES DE COMPUTADORES (2022.2 - T01)
- Professora: EDILAYNE MENESES SALGUEIRO
# Manual para disponibilizar a página web em um container Docker no Laboratório Elan
Este manual tem como objetivo orientar o processo de disponibilização da página web da Empresa Universitário Ensina em um container Docker no Laboratório Elan.

# Pré-requisitos
- Acesso ao Laboratório Elan
- Conhecimento básico em Docker e comandos Linux
- Conta no Github para clonar o repositório da aplicação
- Conhecimento básico em HTML e Python

# Passo-a-passo
## 1. Clonar o repositório da aplicação
Para clonar o repositório da aplicação, execute o seguinte comando:
```
https://github.com/denisfreitas999/docker-atividade.git
```
## 2. Acessar a pasta do projeto
Acesse a pasta do projeto com o seguinte comando:
```
cd docker-atividade
```
## 3. Construir a imagem Docker
Construa a imagem Docker executando o seguinte comando:
```
docker build -t docker-denisson-freitas .
```
## 4. Executar o container Docker
Execute o container Docker com o seguinte comando:
```
docker run docker-denisson-freitas
```
Com isso o server será iniciado graças na porta 12000 como solicitado no Dockerfile e indicado no arquivo TCPServer.py:
- EXPOSE 12000
- CMD [ "python", "./TCPServer.py" ]
- portaServidor = 12000
## 5. Descobrir o 'CONTAINER ID' do container executado com o servidor
Para isso devemos digitar o comando a seguir e buscar  o 'CONTAINER ID' de acordo com o 'NAME' da nossa imagem, que no caso é docker-denisson-freitas:
```
docker ps
```
## 6. Testar a aplicação
Abra outro terminal e execute o comando a seguir:
```
docker exec <CONTAINER ID> python TCPClient.py
```
Substituindo 'CONTAINER ID' pelo id encontrado através do comando anterior. A resposta do terminal deve ser as informações da página index.html do servidor referente a empresa Universitario Ensina.

## 7. Verificar informações do container caso sejam necessárias
Para isso devemos acessar o container com acesso root digitando o seguinte comando:
```
docker exec -i -t <CONTAINER ID> /bin/bash
```
Substituindo o 'CONTAINER ID' pelo id do container recuperado no passo 5. Dessa forma se dermos um ls conseguimos ver os arquivos do container.