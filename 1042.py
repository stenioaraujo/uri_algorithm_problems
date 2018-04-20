# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1042
"""
import sys

def compute():
    lista = list(map(int, r()[0].split()))
    s = sorted(lista)
    print('\n'.join(map(str, s)))
    print()
    print('\n'.join(map(str, lista)))

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
