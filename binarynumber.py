from string import *

n, b = 26, 5
alf = digits + ascii_uppercase
s = ''
while n>0:
    s = alf[n%b]+s
    n //=b
print(s)