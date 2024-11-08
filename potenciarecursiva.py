def potencia(a, n):
    if n == 0:
        return 1
    else:
        return a * potencia(a, n - 1)
    
a = int(input(f"\n Digite o valor da base: "))
n = int(input(f"\n Digite o valor da potência: "))

print(f"Resultado de", a,"elevado a", n,":", potencia(a,n))