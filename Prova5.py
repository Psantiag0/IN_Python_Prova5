# Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.

def maior_numero():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    else:   
        return numero3

# Teste a função

print("O maior número é:", maior_numero())
