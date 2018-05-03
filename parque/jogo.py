""" Crie outro script chamado jogo.py e nele crie três crianças de verdade (três instâncias da classe abstrata Criança).
Você deve passar na criação o nome, a idade e se a criança é ou não a pegadora.

Essas três crianças vão brincar de pegador. Programe o jogo! Pergunte o nome e a idade das crianças.
Verifique se ela é a pegadora. Use a criatividade. E acima de tudo, Divirta-se, porque programar é bom demais!!!
"""

from crianca import Crianca
from crianca import Pegador

crianca1 = Crianca('João', 7)
crianca2 = Crianca('Maria', 5)
crianca3 = Pegador('Neymar', 5)

# Qual o nome de vocês?
print(crianca1.nome)
print(crianca2.nome)
print(crianca3.nome)

# Qual a idade de vocês?
print(crianca1.idade)
print(crianca2.idade)
print(crianca3.idade)

# Algum de vocês é o pegador?
print(crianca1.e_pegador)
print(crianca2.e_pegador)
print(crianca3.e_pegador)

## vamos brincar

crianca2.correr()
crianca3.correr()

crianca3.pegar(crianca2)
crianca2.correr()
crianca3.pegar(crianca2)
crianca1.salvar(crianca2)
crianca1.correr()
crianca1.salvar(crianca2)
crianca1.salvar(crianca2)


