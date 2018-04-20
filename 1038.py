# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1038
"""
import sys


ITENS = {'1': 4, '2': 4.5, '3': 5, '4': 2, '5': 1.5}

def compute(l):
    x, y = l.split()
    total = ITENS[x]*int(y)
    print("Total: R$ {:.2f}".format(total))

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
