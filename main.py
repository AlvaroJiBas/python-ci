from mathe import add
from mathe import minus


if __name__ == '__main__':
    op = input("Que quieres hacer suma (s) resta (r)")
    if op == "s":
        n1 = int(input("sumando 1"))
        n2 = int(input("sumando 2"))
        r= add(n1,n2)
    else:
        n1 = int(input("minuendo"))
        n2 =int(input("sustraendo"))
        r= minus(n1,n2)
    print(f"Resultado {r}" )

