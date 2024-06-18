import socket
import encipher
import sys

def send_data(host,port):
# 定义目标IP地址和端口
    target_ip = host  # 本地IP地址，用于测试
    target_port = port  # 端口号，确保该端口没有被其他程序占用

    # 创建UDP socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 准备要发送的数据

    data = f"accout:admin,password:pass,time,hello-spa".encode()  # 需要将字符串转换为字节串
    #加密数
    encrypt_data=encipher.encryption(data)

    # 发送数据
    sock.sendto(encrypt_data, (target_ip, target_port))

    # 关闭socket
    sock.close()
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 spa_client.py <host> <port>")
        sys.exit(1)
    else:
        send_data(sys.argv[2],sys.argv[3])
