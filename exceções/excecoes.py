print("Exemplo de captura de exceção")

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ValueError as e:
    print(f"Erro: {e}.")
    raise ValueError("Entrada inválida: não é um número inteiro.")
except Exception as e:
    print(f"Erro: {e}.")
else:
    print("Operação concluída com sucesso.")
finally:
    print("Fim do bloco try-except.")
