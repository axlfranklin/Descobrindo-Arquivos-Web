import argparse
import socket


#Criação dos Argumentos
parser = argparse.ArgumentParser(description="Scanner de diretórios")
parser.add_argument("-i", "--ip", help="IP alvo", required=True)
parser.add_argument("-p", "--port", help="Porta", type=int, required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist", required=True)
args = parser.parse_args()

# Uso dos argumentos definidos na outra parte
ip_address = args.ip
port = args.port
wordlist_file = args.wordlist

# Função para abrir wordlist linha por linha
def enum(ip, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            directory = line.strip()

            # Criando uma conexão TCP com o IP e porta específicos
            target_address = (ip, port)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(2)  # Defina um tempo limite adequado para a conexão
            result = client_socket.connect_ex(target_address)
            if result == 0:
                print(f"==> Conexão estabelecida com {target_address}")
                client_socket.send(f"GET /{directory} HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
                response = client_socket.recv(4096)  # Receba a resposta do servidor
                if response:
                    print(f"==> Encontrado: {target_address}/{directory}")
            client_socket.close()

enum(ip_address, wordlist_file)
