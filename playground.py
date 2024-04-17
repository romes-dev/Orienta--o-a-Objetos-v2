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
