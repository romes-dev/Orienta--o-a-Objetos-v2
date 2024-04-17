# Criar uma classe chamada Animal e duas subclasses, cachorro e gato. Trabalhar com polimorfismo de substituição de métodos.
class Animal:
    def __str__(self):
        return "Animal"
    
    def emitir_som(self):
        return "Este animal emite um som."
    
class Cachorro(Animal):
    def __str__(self):
        return "Cachorro"
    
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def __str__(self):
        return "Gato"
    
    def emitir_som(self):
        return "Miau!"
    
zoologico = [Cachorro(), Gato(), Cachorro(), Gato(), Cachorro(), Gato(), Animal()]
for animal in zoologico:
    print(animal)
    print(animal.emitir_som())


# Criar um programa em python que simule diferentes animais em um parque com base com comportamento alimentar desses animais e no som que emitem.

class Animal:
    def __str__(self):
        return "Animal"
        
    def emitir_som(self):
        return "Este animal emite um som."
    
    def comer(self):
        return "Este animal come."
    
class Cachorro(Animal):
    def __str__(self):
        return "Cachorro"
        
    def emitir_som(self):
        return "Au au!"
    
    def comer(self):
        return "O cachorro come ração."

class Gato(Animal):
    def __str__(self):
        return "Gato"
        
    def emitir_som(self):
        return "Miau!"
    
    def comer(self):
        return "O gato come rato."
    
class Passaro(Animal):
    def __str__(self):
        return "Pássaro"
        
    def emitir_som(self):
        return "Piu piu!"
    
    def comer(self):
        return "O pássaro come sementes."
    

parque =[Gato(), Gato(), Passaro(), Cachorro(), Cachorro(), Passaro(), Cachorro(), Gato(), Passaro()]

for animal in parque:
    print(animal)
    print(animal.emitir_som())
    print(animal.comer())
    print("-"*50)
    print()