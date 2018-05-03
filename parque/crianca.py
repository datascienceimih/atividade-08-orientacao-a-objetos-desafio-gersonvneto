""" Vamos criar um parque. Nesse parque várias crianças estão brincando de pegador.
As regras do jogo do pegador são:

O pegador corre atrás das outras crianças.

Quando alguém é pegado fica paralisado.

Quem está paralisado só pode se mexer de novo se alguém que não for o pegador tocar nele e salvá-lo.

Para isso, vamos criar um script chamado crianca.py onde vamos programar nossa classe abstrata Criança.
A criança precisa saber seu nome e sua idade. Precisa saber também se ela é ou não é a pegadora.

As crianças vão CORRER, PEGAR e SALVAR. Obviamente, uma criança que está paralisada não pode correr.
Se eu tentar salvar uma criança que não está paralisada, ela vai me contar que já está livre.
Se o pegador tentar pegar uma criança que já está paralisada ela vai contar que já está paralisada.



"""

class Crianca:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
        self.e_pegador = False
        self.esta_correndo = False
        self.paralisado = False


    def correr(self):
        if self.paralisado:
            print('Não posso correr! Alguém me salva!')
        else:
            self.esta_correndo = True
            print('Eu corro muito rápido!!')


    def salvar(self, outra_crianca):
        if self.esta_correndo:
            if outra_crianca.paralisado and not self.e_pegador:
                outra_crianca.paralisado = False
                print('Te salvei! Começa a correr!!')

            elif self.e_pegador:
                print('Não vou salvar ninguém! Tenho que pegá-los!')

            else:
                print('Estou livre! Continue correndo!')
        else:
            print('Preciso correr para salvar alguém!')

class Pegador(Crianca):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.e_pegador = True

    def pegar(self, outra_crianca):
        if self.esta_correndo:
            if outra_crianca.paralisado:
                print('Já estou paralisado!')

            else:
                outra_crianca.paralisado = True
                print('Te pegueii!! Agora você está paralisado!')

        else:
            print('Não estou correndo, não posso pegar ninguém parado!')




















