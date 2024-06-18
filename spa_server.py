from scapy.all import *
import subprocess
import encipher
import sys

def creat_callback():
    def packet_callback(packet):
        decrypt_data=encipher.decryption(packet["UDP"].load)
        # 这里可以添加对捕获到的数据包的处理逻辑与其他操作
        print(packet["UDP"].load)
        print(decrypt_data)
    return packet_callback



if __name__ == '__main__':
    if len(sys.argv) < 2:
        port1=29578

    elif 1<int(sys.argv[2])<65535:
        port1=sys.argv[2]
    filter1 = f'udp and dst port {port1}'

    my_packet_callback=creat_callback()
    print(f"等待数据连接端口{port1}：")
    #请注意此处的iface网卡名称
    sniff(iface="eth0", prn=my_packet_callback, store=False,count=1,filter=filter1)
