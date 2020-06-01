import unittest
import requests
import json
from fractions import Fraction

value1=[5.556,7,2/3,9.1]
value2=[6.555,14,3/2,1.9]

add_script=[]
add_test=[]
for i in range (0,len(value1)):
    add_from_test=value1[i] + value2[i]
    add_test.append(round(add_from_test,3))
