# Module:urllib is for processing request and response.
# Module:http is for http service and client.
# Module:requests is a wrapper of module:urllib.

import urllib.request as ur
import requests
url = 'https://www.google.com'

conn = ur.urlopen(url)
print(conn)

data = conn.read() # get response content
print(conn.status) # get response status
for key,value in conn.getheaders(): # get response headers
  print(key, value)

resp = requests.get(url)
print(resp.headers) # get response headers
print(resp.text) # get response content
print(resp.status_code) # get response status
