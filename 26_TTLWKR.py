from math import gcd
def video(part,total):
    hi, mi, si = part.split(":")
    ht, mt, st = total.split(":")
    megnezett = int(hi) * 60 * 60 + int(mi) * 60 + int(si)
    teljes = int(ht) * 60 * 60 + int(mt) * 60 + int(st)
    x = int(gcd(megnezett, teljes))
    megnezett = int(megnezett / x)
    teljes = int(teljes / x)
    print(megnezett, "/", teljes, sep="")
try:
    part=input("hh:mm:ss: ")
    total=input("hh:mm:ss: ")
    video(part,total)
except:
    print("hibás bemenet")