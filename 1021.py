"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
"""
from decimal import Decimal
import sys

def compute(l):
    m = Decimal(l)
    valores = [
        ('nota', ['100', '50', '20', '10', '5', '2']),
        ('moeda', ['1', '0.50', '0.25', '0.10', '0.05', '0.01'])
    ]

    for t, lista in valores:
        print("{}S:".format(t.upper()))
        for i in lista:
            i = Decimal(i)
            qnt = m//i
            print("{:} {}(s) de R$ {:.2f}".format(qnt.to_eng_string(), t, i))
            m = m - qnt*i

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
