class Evento:
    def __init__(self, nome, data, horario, local, duracao):
        self.nome = nome
        self.data = data
        self.horario = horario
        self.local = local
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} em {self.local} no dia {self.data} às {self.horario}"

    def exibir_detalhes(self):
        return f"{self.nome}, Data: {self.data}, Horário: {self.horario}, Local: {self.local}, Duração: {self.duracao} horas"

    def custo(self):
        # Implementação simples, pode ser sobrescrita
        return 500  # custo básico fixo

    def lucratividade(self):
        # Implementação simples, pode ser sobrescrita
        return 1000  # lucro fixo

    def participantes(self):
        # Implementação simples, pode ser sobrescrita
        return 50  # número fixo de participantes

class Palestra(Evento):
    def __init__(self, nome, data, horario, local, duracao, palestrante, tema):
        super().__init__(nome, data, horario, local, duracao)
        self.palestrante = palestrante
        self.tema = tema

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Palestrante: {self.palestrante}, Tema: {self.tema}"

class Workshop(Evento):
    def __init__(self, nome, data, horario, local, duracao, instrutor, vagas):
        super().__init__(nome, data, horario, local, duracao)
        self.instrutor = instrutor
        self.vagas = vagas

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Instrutor: {self.instrutor}, Vagas: {self.vagas}"

class Conferencia(Evento):
    def __init__(self, nome, data, horario, local, duracao, organizador, participantes):
        super().__init__(nome, data, horario, local, duracao)
        self.organizador = organizador
        self.participantes = participantes

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Organizador: {self.organizador}, Participantes: {self.participantes}"

class Show(Evento):
    def __init__(self, nome, data, horario, local, duracao, banda, estilo_musical):
        super().__init__(nome, data, horario, local, duracao)
        self.banda = banda
        self.estilo_musical = estilo_musical

    def exibir_detalhes(self):
        return super().exibir_detalhes() + f", Banda: {self.banda}, Estilo Musical: {self.estilo_musical}"

# Lista de eventos
eventos = [
    Palestra("Ciência de Dados", "25/10/2024", "14:00", "Centro de Conferência", 2, "Dr. Data", "Big Data"),
    Workshop("Fotografia com Smartphones", "01/11/2024", "10:00", "Studio X", 3, "Jane Snapshot", 20),
    Conferencia("Tech Week", "15/11/2024", "09:00", "Tech Park", 8, "Innovatech", 300),
    Show("Rock Night", "21/12/2024", "20:00", "Downtown Arena", 5, "The Rockers", "Rock")
]

# Função para exibir todos os detalhes de cada evento
def exibir_todos_eventos(eventos):
    for evento in eventos:
        print(evento)
        print(evento.exibir_detalhes())
        print("-" * 50)

exibir_todos_eventos(eventos)

def calcular_custo_total(eventos):
    return sum(evento.custo() for evento in eventos)

def calcular_lucratividade_total(eventos):
    return sum(evento.lucratividade() for evento in eventos)

def calcular_total_participantes(eventos):
    return sum(evento.participantes() for evento in eventos)

def adicionar_novo_evento(eventos):
    tipo = input("Digite o tipo de evento (Palestra, Workshop, Conferencia, Show): ").strip()
    nome = input("Nome do Evento: ").strip()
    data = input("Data (dd/mm/yyyy): ").strip()
    horario = input("Horário (HH:MM): ").strip()
    local = input("Local: ").strip()
    duracao = int(input("Duração (em horas): "))
    if tipo.lower() == 'palestra':
        palestrante = input("Nome do Palestrante: ").strip()
        tema = input("Tema da Palestra: ").strip()
        eventos.append(Palestra(nome, data, horario, local, duracao, palestrante, tema))
    elif tipo.lower() == 'workshop':
        instrutor = input("Nome do Instrutor: ").strip()
        vagas = int(input("Número de Vagas: "))
        eventos.append(Workshop(nome, data, horario, local, duracao, instrutor, vagas))
    elif tipo.lower() == 'conferencia':
        organizador = input("Nome do Organizador: ").strip()
        participantes = int(input("Número Estimado de Participantes: "))
        eventos.append(Conferencia(nome, data, horario, local, duracao, organizador, participantes))
    elif tipo.lower() == 'show':
        banda = input("Nome da Banda: ").strip()
        estilo_musical = input("Estilo Musical: ").strip()
        eventos.append(Show(nome, data, horario, local, duracao, banda, estilo_musical))
    else:
        print("Tipo de evento não reconhecido.")

def contar_tipos_eventos(eventos):
    tipos = {'palestra': 0, 'workshop': 0, 'conferencia': 0, 'show': 0}
    for evento in eventos:
        if isinstance(evento, Palestra):
            tipos['palestra'] += 1
        elif isinstance(evento, Workshop):
            tipos['workshop'] += 1
        elif isinstance(evento, Conferencia):
            tipos['conferencia'] += 1
        elif isinstance(evento, Show):
            tipos['show'] += 1
    return tipos

def gerenciar_eventos():
    eventos = []  # Inicializa uma lista vazia de eventos
    while True:
        print("\nSistema de Gestão de Eventos")
        print("################################################")
        print("#┌────────────────────────────────────────────┐#")
        print("#│             MENU PRINCIPAL                 │#")
        print("#├────────────────────────────────────────────┤#")
        print("#│ 1. Adicionar Evento                        │#")
        print("#│ 2. Exibir Eventos                          │#")
        print("#│ 3. Calcular Custos e Lucratividade         │#")
        print("#│ 4. Contar Participantes                    │#")
        print("#│ 5. Contar Tipos de Eventos                 │#")
        print("#│ 6. Sair                                    │#")
        print("#└────────────────────────────────────────────┘#")
        print("################################################")
        print("################################################")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_novo_evento(eventos)
        elif escolha == '2':
            exibir_todos_eventos(eventos)
        elif escolha == '3':
            custo = calcular_custo_total(eventos)
            lucro = calcular_lucratividade_total(eventos)
            print(f"Custo Total: {custo}, Lucratividade Total: {lucro}")
        elif escolha == '4':
            participantes = calcular_total_participantes(eventos)
            print(f"Total de Participantes: {participantes}")
        elif escolha == '5':
            tipos = contar_tipos_eventos(eventos)
            for tipo, quantidade in tipos.items():
                print(f"Total de {tipo.capitalize()}s: {quantidade}")
        elif escolha == '6':
            break
        else:
            print("Opção inválida.")

# Executar o sistema
gerenciar_eventos()