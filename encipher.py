from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encryption(data):

    #生成随机密钥向量
    key = urandom(32)
    iv = urandom(16)
    #aes加密
    encrypt_data=aes_encryption(data,key,iv)
    #RSA加密密钥
    encrypt_key=rsa_encrypt(key)
    encrypt_iv = rsa_encrypt(iv)

    #打包所有加密后数据
    encrpyt_packet=encrypt_data+'\n,\n'.encode()+encrypt_key+'\n,\n'.encode()+encrypt_iv

    return encrpyt_packet

def decryption(encrypt_data):
    #分割收到的加密数据
    list=encrypt_data.split(b'\n,\n')
    #解密密钥
    key=rsa_decrypt(list[1])
    iv=rsa_decrypt(list[2])
    #AES解密数据
    data=aes_decryption(list[0],key,iv)
    return data
def aes_encryption(data,key,iv):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    # 创建一个Cipher对象，指定AES加密算法，模式和后端
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # 创建一个encryptor对象
    encryptor = cipher.encryptor()
    # 加密数据
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    # 输出加密后的密文（通常是二进制数据）
    #print(ciphertext)
    return ciphertext

def aes_decryption(cipherdata,key,iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # 创建一个decryptor对象
    decryptor = cipher.decryptor()
    # 解密数据
    decrypted_padded_data = decryptor.update(cipherdata) + decryptor.finalize()
    # 移除PKCS7填充
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    # 输出解密后的明文
    # 注意：如果原始数据是二进制数据，则不需要decode()调用
    return decrypted_data

def rsa_encrypt(data):
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    #print(data)
    # 使用公钥进行加密
    # 注意：OAEP填充模式通常用于公钥加密
    encrypt_data = public_key.encrypt(
        data,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # 打印加密后的消息（通常是二进制数据）
    #print("Encrypted message:", encrypt_data)
    return encrypt_data

def rsa_decrypt(data):
    #打开本的私钥PEM
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    #使用私钥解密
    decrypted = private_key.decrypt(
        data,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted
    #print("Decrypted message:", decrypted)

def generate_rsa_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # 序列化公钥以便保存或传输
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)


    # 序列化私钥以便保存（通常不会公开或传输私钥）
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("private_key.pem", "wb") as f:
        f.write(private_key_pem)
    print("!!!注意!!!请妥善保管private_key")

if __name__ == '__main__':
    #生成公、私密钥
    #generate_rsa_key()
     if len(sys.argv) < 2:
        print("Usage: 'python script.py generate'  to creat key")
        sys.exit(1)
     elif sys.argv[2]=="generate" :
        generate_rsa_key()
