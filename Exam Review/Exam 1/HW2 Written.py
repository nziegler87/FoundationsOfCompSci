def f1(m):
    m = m + 1
    print(m)

def f2(n):
    print(n)
    n = n + 1
    f1(n)
    return n

def main():
    m = 18
    m = f2(m)
    print(m)

main()

# 18
# 20
# 19
