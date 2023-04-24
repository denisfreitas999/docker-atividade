FROM python:3-slim

LABEL version="1.0.0" description="Atividade de Docker" maintainer="Denisson Freitas <denisson.freitas@dcomp.ufs.br>"

WORKDIR /usr/src/docker-denisson-freitas

COPY . .

EXPOSE 12000

CMD [ "python", "./TCPServer.py" ]
