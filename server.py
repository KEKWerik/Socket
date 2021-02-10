#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

#la funzione avvia_server crea un endpoint di ascolto dal quale accettare connessioni
#in entrata, la socket di ascolto viene passata alla funzione ricevi_comandi la quale
#accetta richieste di connessione e per ognuna crea una socket per i dati da cui
#ricevere le richieste e inviare le risposte.

def ricevi_comandi(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")
        contConn=0
        while True:
            dati = sock_service.recv(2048)
            contConn+=1
            if not dati:
                print("Fine dati dal client. Reset")
                break
            
            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)
            if dati=='0':
                print("Chiudo la connessione con " + str(addr_client))
                break

            ris=0
            dati=dati.split(';')
            if dati[0]=='piu':
                ris=int(dati[1]) + int(dati[2])
            elif dati[0]=='meno':
                ris=int(dati[1]) - int(dati[2])
            elif dati[0]=='per':
                ris=int(dati[1]) * int(dati[2])
            elif dati[0]=='diviso':
                ris=int(dati[1]) / int(dati[2])

            ris=str(ris)
            

                
            



            dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(ris)

            dati = dati.encode()

            sock_service.send(dati)

            sock_service.close()   
    

def avvia_server(indirizzo,porta):
    sock_listen = socket.socket()

    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
    ricevi_comandi(sock_listen)

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)



