from math import gcd
def tortosszeg(a,b):
    d,e=a.split(",")
    f,g=b.split(",")
    x=int(d)*int(g)+int(e)*int(f)
    y=int(e)*int(g)
    print(int(x / gcd(x, y)), "/", int(y / gcd(x, y)), sep="")

try:
    a="8,12"
    b="16,24"
    tortosszeg(a,b)
except:
    print("hibás bemenet")