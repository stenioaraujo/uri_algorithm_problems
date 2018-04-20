"""
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
"""
import sys

def compute(l):
    d = int(l)
    a = d // 365
    d = d - a*365

    m = d // 30
    d = d - m*30
    print("""{:d} ano(s)
{:d} mes(es)
{:d} dia(s)""".format(a, m, d))

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
