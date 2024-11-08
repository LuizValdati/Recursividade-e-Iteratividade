def potencia(a, n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= a
    return resultado

a = int(input(f"\n Digite o valor da base: "))
n = int(input(f"\n Digite o valor da potência: "))

print(f"Resultado de", a,"elevado a", n,":", potencia(a,n))