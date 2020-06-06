from __future__ import absolute_import, unicode_literals
import urllib.request as ur
import json 
from app import app 

@app.task
def getData(url):
    resp = ur.urlopen(url)
    data= json.loads(resp.read())
    return data