nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))  # Corrigido aqui

# Verificar a idade do usuário
print(f"{nome} é maior de idade." if idade >= 18 else f"{nome} é menor de idade.")
