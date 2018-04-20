# -*- coding: utf-8 -*-
"""
urionlinejudge::description
"""
from decimal import Decimal
import sys

def compute():
    print(r(2, "prompt: "))

def r(lines=1, prompt=None, split=True):
    """Read one line from the standard input"""
    lista = []
    for i in range(lines):
        if prompt:
            print(prompt, end='', flush=True)
        l = sys.stdin.readline()
        if l:
            if split:
                l = l.split()
            lista.append(l)
        else:
            exit()
    return lista


if __name__ == "__main__":
    while True:
        compute()
