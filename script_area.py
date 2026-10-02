#!/usr/bin/env python3

import sys

a = sys.argv[1]
b = sys.argv[2]

if a.isdigit() and b.isdigit():
    if int(a) < 500 and int(b) < 500:
        A = int(a)*int(b)/2
        print('A área do triangulo retângulo com lados a=',a, 'e b=',b,', é', A)
    else:
        print('Números excedem o limite')
else:
    print('números enviados não são inteiros')

