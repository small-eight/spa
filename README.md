# spa
single packet authorization python realize<br>
SPA单包认证，一种网络安全技术，用以在不开放网络端口的情况下，进行认证授权.<br>
与[port knock](https://github.com/small-eight/portknock)技术理念相同，都是以满足“先认证后链接”这一理念（零信任中也包含此概念）。弥补了TCP/IP协议无法“先认证后连接”的缺点。<br>
PK技术与SPA技术区别在于，PK以传输层包头为认证信息，而SPA则是在data中，可以对数据进行加密等操作。<br>

SPA目前主要应用于[SDP(Software Defined Perimeter )](https://github.com/small-eight/SDP)技术中.
