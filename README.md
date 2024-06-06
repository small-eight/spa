# spa
single packet authorization python realize<br>
SPA单包认证，一种网络安全技术，用以在不开放网络端口的情况下，进行认证授权.<br>
与[port knock](https://github.com/small-eight/portknock)技术理念相同，都是以满足“先认证后链接”这一理念（零信任中也包含此概念）。弥补了TCP/IP协议公开连接的缺点。<br>
PK技术与SPA技术区别在于，PK以传输层包头为认证信息，而SPA则是在data中，可以对数据进行加密等操作。<br>

SPA目前主要应用于[SDP(Software Defined Perimeter )](https://github.com/small-eight/SDP)技术中.

## 说明
encipher.py 加密模块，所有加解密都在此模块中<br>
spa_sever.py服务端模块，接受数据，解密数据<br>
spa_client.py客户端，发送数据<br>
客户端使用AES对数据进行了加密，同时使用RSA加密密钥，使用UDP发送单包。数据包中应包含账户信息，校验信息以及其他必要信息。

## 使用
首次使用，请执行encipher 中 generate_rsa_key生成rsa密钥，公钥与spa_client在同一目录下。私钥与spa_server在同一目录下（请注意妥善保管私钥）。<br>
spa_sever.py 中 packet_callback里面执行捕获到的数据包的处理逻辑与其他操作<br>
spa_client.py中修改对应服务端IP<br>
服务端执行 python3 spa_sever.py<br>
客户端执行 python3 spa_client.py  
