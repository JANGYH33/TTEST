# client 소스

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)

clientsock.connect(('127.0.0.1', 8888)) # 해당 주소로 능동적으로 접촉 시도
clientsock.send('안녕 반가워'.encode(encoding = 'utf-8', erros = 'strict'))


clientsock.close()