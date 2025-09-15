def meu_decorado(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorado
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()