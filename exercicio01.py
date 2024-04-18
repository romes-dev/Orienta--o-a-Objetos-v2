"""
            Exercício: Zoológico Interativo
                        ____
                   .---'-    \
      .-----------/           \
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\).

Objetivo: Desenvolver um programa em Python que simula um zoológico com diferentes tipos de animais, cada um com seus próprios comportamentos para emitir sons, comer e realizar uma atividade característica.



### Descrição: Você criará uma classe base chamada Animal e várias subclasses representando diferentes tipos de animais. Cada classe terá métodos para emitir_som, comer e atividade. O objetivo é demonstrar polimorfismo ao chamar esses métodos de uma lista de animais e observar comportamentos distintos.


### Classe Base Animal:
Métodos: emitir_som(), comer(), atividade()
Método __str__ para retornar uma descrição do animal.
Subclasses (Exemplos: Cachorro, Gato, Pássaro, Elefante):
Sobrescrever todos os métodos da classe base.
Adicionar um método atividade que descreve uma ação específica do animal (exemplo: Cachorro pode "buscar bola").
    """
    
class Animal:
    def __str__(self):
        return "Animal"
    
    def emitir_som(self):
        return "Este animal emite um som."
    
    def comer(self):
        return "Este animal come."
    
    def atividade(self):
        return "Este animal realiza uma atividade."

class Cachorro(Animal):
    def __str__(self):
        return "Cachorro"
    
    def emitir_som(self):
        return "Au au!"
    
    def comer(self):
        return "O cachorro come ração."
    
    def atividade(self):
        return "O cachorro busca a bola."

class Gato(Animal):
    def __str__(self):
        return "Gato"
    
    def emitir_som(self):
        return "Miau!"
    
    def comer(self):
        return "O gato come rato."
    
    def atividade(self):
        return "O gato brinca com o novelo de lã."

class Passaro(Animal):
    def __str__(self):
        return "Pássaro"
    
    def emitir_som(self):
        return "Piu piu!"
    
    def comer(self):
        return "O pássaro come sementes."
    
    def atividade(self):
        return "O pássaro voa."

class Elefante(Animal):
    def __str__(self):
        return "Elefante"
    
    def emitir_som(self):
        return "fuumm uuuuh!"
    
    def comer(self):
        return "O elefante come folhas."
    
    def atividade(self):
        return "O elefante joga água com a tromba."
    
zoologico = [Cachorro(), Gato(), Passaro(), Elefante()]
for animal in zoologico:
    print(animal)
    print(animal.emitir_som())
    print(animal.comer())
    print(animal.atividade())
    print()
    