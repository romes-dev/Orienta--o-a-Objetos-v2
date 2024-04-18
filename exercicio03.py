# Sistema de Gestão de Eventos
""" Desenvolva um programa que simule um sistema de gestão de eventos. Ele deve ser capaz de processar diferentes tipos de eventos, utilizando polimorfismo para chamar métodos específicos de cada classe de evento.

Crie uma classe base Evento e suas subclasses: Palestra, Workshop, Conferencia e Show.

Atributos da classe base Evento: nome, data, horario, local, duracao.

Métodos da classe base Evento: __str__ para retornar uma descrição do evento, exibir_detalhes() para mostrar todos os atributos do evento, custo() para calcular o custo do evento e lucratividade() para calcular a lucratividade do evento e participantes() para calcular o número de participantes do evento.

Métodos das subclasses: Palestra, Workshop, Conferencia e Show: __str__ para retornar uma descrição do evento, exibir_detalhes() para mostrar todos os atributos do evento mais um atributo específico de cada tipo de evento. 
    Para Palestra: palestrante e tema.
    Para Workshop: instrutor e vagas.
    Para Conferencia: organizador e participantes.
    Para Show: banda e estilo musical.

Crie uma lista de eventos com diferentes tipos de eventos e exiba todos os detalhes de cada evento.

Desafio: Implemente um método para calcular o custo total de todos os eventos e sua lucratividade.

Desafio 2: Implemente um método para calcular o número total de participantes de todos os eventos.

Desafio 3: Implemente um método para que o usuário cadastre novos eventos nessa lista.

Desafio 4: Implemente um método para calcular o número total de eventos de cada tipo (Palestra, Workshop, Conferencia e Show).
"""