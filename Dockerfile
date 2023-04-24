LABEL version="1.0.0" description="Atividade de Docker" maintainer="Denisson Freitas <denisson.freitas@dcomp.ufs.br>"

FROM python:3-slim

WORKDIR /home/20121iqui0192/docker-atividade

COPY . .

EXPOSE 12000

CMD [ "python", "./TCPServer.py" ]