# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
"""
import decimal
import sys

def compute(l):
    decimal.getcontext().prec = 100
    a, b, c = map(decimal.Decimal, l.split())
    base = decimal.Decimal('0.00000')

    delta = b**2 - 4*a*c
    if delta >= 0 and a != 0:
        r1 = (-b + delta.sqrt()) / (2*a)
        r2 = (-b - delta.sqrt()) / (2*a)
        print("R1 = {}".format(r1.quantize(base)))
        print("R2 = {}".format(r2.quantize(base)))
    else:
        print("Impossivel calcular")

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
