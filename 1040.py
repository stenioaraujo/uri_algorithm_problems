# -*- coding: utf-8 -*-
"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1040
"""
from decimal import Decimal
import sys

def compute():
    a, b, c, d = map(Decimal, r().split())
    avg = (a*2 + b*3 + c*4 + d)/10
    print("Media: {:.1f}".format(avg))
    if avg >= Decimal('7.0'):
        print("Aluno aprovado.")
        return False
    elif avg >= Decimal('5.0'):
        print("Aluno em exame.")
    else:
        print("Aluno reprovado.")
        return False
    e = Decimal(r())
    print("Nota do exame: {:.1f}".format(e))
    avg = (avg + e) / 2
    if avg >= Decimal('5.0'):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(avg))
    return False

def r(prompt=None):
    """Read one line from the standard input"""
    if prompt:
        return input(prompt)
    return input()


if __name__ == "__main__":
    try:
        while compute():
            pass
    except:
        pass
