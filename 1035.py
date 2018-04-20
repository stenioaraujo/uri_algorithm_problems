# -*- coding: utf-8 -*-
"""
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
"""
import sys

def compute(l):
    A, B, C, D = map(int, l.split())
    conditions = [
        B > C, D > A, (C + D) > (A + B),
        C >= 0, D >= 0, A % 2 == 0
    ]
    if all(conditions):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")


def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
