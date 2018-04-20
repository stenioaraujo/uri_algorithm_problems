# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
"""
from decimal import Decimal
import sys

def compute():
    a, b, c = map(Decimal, r()[0].split())
    t = [a < b+c, b < a+c, c < a+b]
    if all(t):
        print("Perimetro = {:.1f}".format(a+b+c))
    else:
        print("Area = {:.1f}".format((a+b)*c/2))

def r(lines=1, prompt=None):
    """Read one line from the standard input"""
    lista = []
    for i in range(lines):
        l = sys.stdin.readline()
        if l:
            lista.append(l)
        else:
            exit()
    return lista


if __name__ == "__main__":
    while True:
        compute()
