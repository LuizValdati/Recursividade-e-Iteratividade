def somapar(n):
    if n <= 0:
        return 0
    elif n % 2 != 0:
        return somapar(n-1)
    else:
        return n + somapar(n-1)
    
a = int(input(f"\n Digite a quantidade de elementos do intervalo: "))

print (f"A soma dos pares de 0 a", a,":", somapar(a))