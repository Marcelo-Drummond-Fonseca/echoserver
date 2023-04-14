# Exemplo basico socket (lado ativo)

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA)) 

# envia uma mensagem para o par conectado e aguarda a resposta. Fecha a conexão se for "fim"
while True:
    sentmsg = input('insira a mensagem\n')
    if(sentmsg == "fim"): break
    sock.send(sentmsg.encode('utf-8'))
    msg = sock.recv(1024)
    print(str(msg,  encoding='utf-8'))
    
sock.close() 
