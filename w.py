import socket
import os,time

def server():
    HOST, PORT = '', 8846

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client, client_address = listen_socket.accept()
        handler(client)



def handler(client):
        
        request = client.recv(1024)
        l=request.split()
        fname=l[1].split('/')[1]
        d=open(fname,'rb').read()
        cfile = client.makefile('wb', 0) 
        print request
        cfile.write('HTTP/1.1 200 OK\n') 
        cfile.write('Accept-Ranges: bytes\n')
        cfile.write('Content-Type: image/png\n')
        cfile.write('Content-Length: 35678\n')
        cfile.write('Connection: keep-alive\n')
        cfile.write('Access-Control-Allow-Origin: *\n\n')
        cfile.write('<html><body>')
        cfile.write(d)
        cfile.write('</body></html>\n\n')
        cfile.close()
        client.close()
server()
