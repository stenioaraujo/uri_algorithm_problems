import sys

def compute(l):
    s = int(l)
    h = s // (3600)
    s = s - h*3600

    m = s // 60
    s = s - m*60
    result = "{:d}:{:d}:{:d}".format(h, m, s)

    print(result)

def main():
    for l in sys.stdin:
        compute(l)

if __name__ == "__main__":
    main()
