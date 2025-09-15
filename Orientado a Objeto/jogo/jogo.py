from random import randint

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} causando {dano} de dano!")
        alvo.receber_dano(dano)


    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
        print(f"{self.get_nome()} recebeu {dano} de dano! Vida restante: {self.get_vida()}")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()
        return f"{detalhes_base} \nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        print(f"{self.get_nome()} usou {self.get_habilidade()} em {alvo.get_nome()} causando {dano} de dano!")
        alvo.receber_dano(dano)

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Arqueiro", vida=100, nivel=5, habilidade="Tiro com Arco")
        self.inimigo = Inimigo(nome="Goblin", vida=50, nivel=2, tipo="Monstro")

    def iniciar_batalha(self):
        print("\nBatalha Iniciada!")
        # Lógica simplificada de batalha
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print(f"\nTipo de Inimigo: {self.inimigo.get_tipo()}\n")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("\nPressione Enter para o herói atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial, 3 - Sair do jogo): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                print(f"{self.heroi.get_nome()} usou um ataque especial!")
                self.heroi.atacar(self.inimigo)
                self.heroi.atacar(self.inimigo)
            elif escolha == '3':
                print("Saindo do jogo...")
                break 
            # Ataque duplo para especial
            else:
                print("Escolha inválida! O inimigo aproveita a oportunidade para atacar.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

            #     break
        if self.heroi.get_vida() > 0:
            print(f"\n{self.heroi.get_nome()} venceu a batalha!")

        else:
            print(f"\nGAME OVER")


jogo = Jogo()
jogo.iniciar_batalha()




