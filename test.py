import unittest
from flask import Flask, request
import json
from fractions import Fraction

V1=[5.556,7,2/3,9.1]
V2=[6.555,14,3/2,1.9]

add_script=[]
add_test=[]
for i in range (0,len(V1)):
    add_from_test=V1[i] + V2[i]
    add_test.append(round(add_from_test,3))
    PARAM= {"A":Fraction(V1[i]),"B":Fraction(V2[i])}
    url_add = 'http://127.0.0.1:5000/add'
    req=request.get(url_add ,params=PARAM)
    data=req.json()
    add_script.append(round(data,3))

if add_script[i]==add_test[i]:
    print ("sucessfully tested")
else:
    print ("testing failed")
