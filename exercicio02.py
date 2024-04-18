# Polimorfismo na prática

## Desenvolver um programa que simule um sistema de pagamento de uma loja. Ele deve ser capaz de processar diferentes tipos de pagamentos, utilizando polimorfismo para chamar métodos específicos de cada classe de pagamento.

# Classe Base Pagamento e suas subclasses: Dinheiro, Cartão de Crédito, Cartão de Débito.

# Classe Base Pagamento:
## Métodos: autorizar(), finalizar()
## Método __str__ para retornar uma descrição do pagamento.

class Pagamento:
    def __str__(self):
        return "Pagamento"
    
    def autorizar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
    
    def finalizar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
    
    
# Subclasses (Exemplos: Dinheiro, Cartão de Crédito, Cartão de Débito):

class Dinheiro(Pagamento):
    def __str__(self):
        return "Dinheiro"
    
    def autorizar(self):
        return "Pagamento em dinheiro autorizado."
    
    def finalizar(self):
        return "Pagamento em dinheiro finalizado."

class CartaoCredito(Pagamento):
    def __str__(self):
        return "Cartão de Crédito"
    
    def autorizar(self):
        return "Pagamento com cartão de crédito autorizado."
    
    def finalizar(self):
        return "Pagamento com cartão de crédito finalizado."

class CartaoDebito(Pagamento):
    def __str__(self):
        return "Cartão de Débito"
    
    def autorizar(self):
        return "Pagamento com cartão de débito autorizado."
    
    def finalizar(self):
        return "Pagamento com cartão de débito finalizado."


lista_de_pagamentos = [Dinheiro(), CartaoCredito(), CartaoDebito(), Dinheiro(), CartaoCredito(), CartaoDebito()]

for pagamento in lista_de_pagamentos:
    print(pagamento)
    print(pagamento.autorizar())
    print(pagamento.finalizar())
    print("-" * 30)
    
