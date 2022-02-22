import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 8000))
    s.listen(1)
    
    conn, addr = s.accept()
    while True:
        with conn:
            request = conn.recv(1024).decode('utf-8')
            print(request)
            conn.sendall('Hello world'.encode('utf-8'))    

def parse_http(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(
        line.split(':', maxsplit=1)
        for line in headers
    )
    return method, path, protocol, headers, body

    # def process_response(response):
    #     return(
    #         'HTTP/1.1 200 ok\r\n'
    #         f'Content-Ln'
    #     )

