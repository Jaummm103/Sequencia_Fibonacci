#Sequencia de Fibonacci
numero = int(input("Digite até um número para ser apresentado na sequência de Fibonacci : "))
antes = 1
depois = 1

for i in range(0, numero,):
    print(antes)
    soma = antes + depois
    antes = depois
    depois = soma

if numero <= 0:
    print("Sequência Invalida")