def somaimpar(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return somaimpar(n-1)
    else:
        return n + somaimpar(n-1)
    
a = int(input(f"\n Digite a quantidade de elementos do intervalo: "))

print (f"A soma dos ímpares de 0 a", a,":", somaimpar(a))