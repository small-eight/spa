from scapy.all import *
import subprocess
import encipher

def creat_callback():
    def packet_callback(packet):
        decrypt_data=encipher.decryption(packet["UDP"].load)
        # 这里可以添加对捕获到的数据包的处理逻辑与其他操作
        print(packet["UDP"].load)
        print(decrypt_data)
    return packet_callback



if __name__ == '__main__':
    port1=29578
    filter1 = f'udp and dst port {port1}'

    my_packet_callback=creat_callback()
    print("等待数据连接：")
    sniff(iface="eth0", prn=my_packet_callback, store=False,count=1,filter=filter1)