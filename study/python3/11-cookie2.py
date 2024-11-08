import urllib.request, http.cookiejar

filename = "python3\\11-cookie22.txt"
# Mozilla
# cookie = http.cookiejar.MozillaCookieJar(filename)
# LWP格式（libwww-perl)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
