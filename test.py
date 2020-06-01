#!usr/bin/python3

import unittest
from flask import Flask, request
import json
from fractions import Fraction


n1 = [5,7.1,18/3,5/5,7.885]
n2 = [7,8.67,8/23,6/6,7.511]

add_from_script = []
add_from_test = []
for i in range(0,len(n1)):

	PARAM={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
	
	test_add = n1[i] + n2[i]
	add_from_test.append(round(test_add,3))

    url_add = 'http://127.0.0.1:5000/add'
	req = request.get(url_add, params=PARAM)
	data = req.json()
	add_from_script.append(round(data,3)) 

    if add_from_script[i] == add_from_test[i]:
		print ("Tested addition successfully:OK")
	else:
		print ("Failed addition Test")
