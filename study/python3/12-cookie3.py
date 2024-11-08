import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load("python3\\11-cookie22.txt", ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))
