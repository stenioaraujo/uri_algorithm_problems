# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
"""
from decimal import Decimal
import sys

def compute(l):
    n = Decimal(l)
    intervals = [
        ['0', '25'], ['25', '50'],
        ['50', '75'], ['75', '100']
    ]
    for i in intervals:
        infe, supe = i
        if Decimal(infe) <= n and n <= Decimal(supe):
            t = '('
            if infe == '0':
                t = '['
            print("Intervalo {}{},{}]".format(t, infe, supe))
            break
    else:
        print("Fora de intervalo")

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
