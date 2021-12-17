import socket

# 1初始化套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2建立链接  要传入链接的服务器ip和port
tcp_socket.connect(('127.0.0.1', 9999))

while True:
    text = input('python发送的数据')
    # 3发数据
    tcp_socket.send(text.encode('utf8'))
    # 4接收数据
    data = tcp_socket.recv(1024)
    print(data.decode('utf8'))

# 5断开
tcp_socket.close()

