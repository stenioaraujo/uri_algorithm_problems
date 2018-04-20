# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1041
"""
from decimal import Decimal
import sys

def compute():
    x, y = map(Decimal, r()[0].split())
    c = [
        x>0 and y>0, x<0 and y>0, x<0 and y<0, x>0 and y<0,
        x==0 and y==0, x==0, y==0
    ]
    s = [
        "Q1", "Q2", "Q3", "Q4",
        "Origem", "Eixo Y", "Eixo X"
    ]
    for i, j in zip(c, s):
        if i:
            print(j)
            break

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
