from __future__ import absolute_import, unicode_literals

from app import app

@app.task
def add(x,y):
    return x+y 

@app.task
def mult(x,y):
    return x+y

@app.task
def xsum(numbers):
    return sum(numbers)