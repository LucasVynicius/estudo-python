
# Classe (Modem)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


pessoa1 = Pessoa("Miguel", 6)
pessoa2 = Pessoa("Noah", 2)

print(pessoa1.nome, pessoa1.idade)
mensagem = pessoa2.saudacao()
print(mensagem)