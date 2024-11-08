def somaimpar(n):
    soma = 0
    for i in range(0, n+1):
        if (i % 2 != 0):
            soma += i
    return soma

a = int(input(f"\n Digite a quantidade de elementos do intervalo: "))

print (f"A soma dos ímpares de 0 a", a,":", somaimpar(a))