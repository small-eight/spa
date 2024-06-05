# spa
single packet authorization python realize
SPA单包认证，一种网络安全技术，用以在不开放网络端口的情况下，进行认证授权，与[port knock](https://github.com/small-eight/portknock)技术理念相同，弥补了TCP/IP协议无法“先认证后连接”的缺点。<br>
PK技术与SPA技术区别在于，PK认证信息在传输层包头中，而SPA则是在包里，可以对数据进行加密等操作。<br>

SPA目前主要应用与[SDP(Software Defined Perimeter )](https://github.com/small-eight/SDP)技术中.
