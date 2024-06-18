# spa
single packet authorization python realize<br>

SPA单包认证，一种网络安全技术，用以在不开放网络端口的情况下，进行认证授权.<br>
与[port knock](https://github.com/small-eight/portknock)技术理念相同，都是以满足“先认证后链接”这一理念（零信任中也包含此概念）,用以弥补TCP/IP协议公开连接的缺点。<br>
PK技术与SPA技术区别在于，PK以传输层包头为认证信息（顺序端口访问），而SPA则是在data中写入了认证信息，并对数据进行加密等操作。<br>

SPA具体应用，请查看[SDP(Software Defined Perimeter )](https://github.com/small-eight/SDP)技术<br>

**本项目仅作为技术实现，请不要应用于生成环境<br>**(由于没有过滤，目前存在执行任意代码漏洞)

## 说明
encipher.py 加密模块，所有加解密都在此模块中<br>
spa_sever.py服务端模块，接受数据，解密数据<br>
spa_client.py客户端，发送数据<br>
spa_client.py客户端使用AES对数据进行加密，同时使用RSA加密AES密钥，用UDP发送。数据包中应包含账户信息、时间戳、校验信息以及其他必要信息。

## 使用
首次使用，请执行encipher 中 generate_rsa_key生成rsa密钥<br>
```python3
  python3 encioher.py generate
``` 
公钥与spa_client在同一目录下使用。私钥与spa_server在同一目录下（请注意妥善保管私钥）。<br>

服务端执行 <br>
```python3
  python3 spa_sever.py 29578 
```
指定监听的端口为29578，如不添加参数，默认为29578。<br>
请注意文件中iface="eth0" 此处为监听的网卡，默认为"eth0"<br>
spa_sever.py 中 packet_callback里面执行捕获到的数据包的处理逻辑与操作，放通符合认证要求的的客户端<br>

客户端执行<br>
```python3
  python3 spa_client.py 127.0.0.1  29578
```
服务端将会在控制台输出收到的数据。<br>

