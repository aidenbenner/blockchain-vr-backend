import urllib.request

req = urllib.request.Request('http://google.ca'
)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

    print(the_page)