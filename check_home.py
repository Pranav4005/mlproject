import urllib.request

resp = urllib.request.urlopen('http://127.0.0.1:5000/')
print('code', resp.getcode())
body = resp.read()
print('len', len(body))
print(repr(body[:500]))
