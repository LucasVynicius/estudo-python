from math import sqrt
from meu_modulo import saudacao, dobro

print("Exemplo de importação de um módulo padrão: ")


raiz_quadrada = sqrt(16)
print(f"A raiz quadrada de 16 é {raiz_quadrada}")

print("\nExemplo de criação e uso de um módulo personalizado:")

mensagem = saudacao("Miguel")
print(mensagem)
resultado_dobro = dobro(5)
print(f"O dobro de 5 é {resultado_dobro}")
