
#Python http/sock5:

#coding=utf-8
import requests
#import urllib3

#请求地址
targetUrl = "http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=85764&vkey=5DF841380DF11561FC8854B0EF196203&num=200&time=30&plat=0&re=0&type=0&so=1&ow=1&spl=1&addr=广东&db=1"

#代理服务器

#使用http模式请打开注释
proxyType = "socks5"
#proxyType = "http"

#使用用户名密码验证请打开注释
proxyU = "1mm"
proxyP = "W6NsTV2.xGp8CX."
#proxyU = "你的用户名"
#proxyP = "你的密码"

proxyHost = "携趣代理IP地址"
proxyPort = "携趣代理IP端口"

#urllib3.disable_warnings()
#pip install -U requests[socks]  socks5代理
if proxyType == "socks5":
	print("socks5")
	if proxyU == "":
		proxyMeta = "socks5://%(host)s:%(port)s" % {
			"host" : proxyHost,
			"port" : proxyPort,
		}
	else:
		proxyMeta = "socks5://%(user)s:%(pass)s@%(host)s:%(port)s" % {
			"host" : proxyHost,
			"port" : proxyPort,
			"user" : proxyU,
			"pass" : proxyP,
		}
	myproxies = {
		"http"  : proxyMeta,
		"https"  : proxyMeta
	}
	resp = requests.get(targetUrl, proxies=myproxies ,timeout=5)


else:
	print("http")
	if proxyU == "":
		proxyMeta = "http://%(host)s:%(port)s" % {
			"host" : proxyHost,
			"port" : proxyPort,
		}
	else:
		proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
			"host" : proxyHost,
			"port" : proxyPort,
			"user" : proxyU,
			"pass" : proxyP,
		}
	myproxies = {
		"http"  : proxyMeta,
		"https"  : proxyMeta
	}
	resp = requests.get(targetUrl, proxies=myproxies)
	
print(resp.status_code)
print(resp.text)
