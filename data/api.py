from __future__ import absolute_import, unicode_literals
import urllib.request as ur
import json 

url = 'https://jsonplaceholder.typicode.com/posts'

@app.task
def getData(*args):    
    resp = ur.urlopen(url)
    data=json.loads(resp.read())
    return print(data)
    # print(data)

# getData(url)