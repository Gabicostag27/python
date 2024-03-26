from database import Database

db = Database()

def add_team():
    team_name = input("Digite o nome do time: ")
    if db.add_team(team_name):
        print(f"Time '{team_name}' cadastrado com sucesso.")
    else:
        print(f"O time '{team_name}' já está cadastrado.")

def remove_team():
    team_name = input("Digite o nome do time: ")
    if db.remove_team(team_name):
        print(f"Time '{team_name}' removido com sucesso.")
    else:
        print(f"O time '{team_name}' não foi encontrado.")

def add_player():
    player_name = input("Digite o nome do jogador: ")
    team_name = input("Digite o nome do time: ")
    if db.add_player(player_name, team_name):
        print(f"Jogador '{player_name}' cadastrado no time '{team_name}'.")
    else:
        print(f"Não foi possível cadastrar o jogador no time.")

def remove_player():
    player_name = input("Digite o nome do jogador: ")
    if db.remove_player(player_name):
        print(f"Jogador '{player_name}' removido com sucesso.")
    else:
        print(f"O jogador '{player_name}' não foi encontrado.")

def update_player_team():
    player_name = input("Digite o nome do jogador: ")
    new_team_name = input("Digite o novo time do jogador: ")
    if db.update_player_team(player_name, new_team_name):
        print(f"Time do jogador '{player_name}' atualizado para '{new_team_name}'.")
    else:
        print(f"Não foi possível atualizar o time do jogador.")

def get_players_in_team():
    team_name = input("Digite o nome do time: ")
    players = db.get_players_in_team(team_name)
    print(f"Jogadores do time '{team_name}': {players}")

def get_players_report():
    report = db.get_players_report()
    print("Lista de todos os jogadores:")
    print(report)

def get_teams_report():
    report = db.get_teams_report()
    print("Lista de todos os times:")
    print(report)

while True:
    print("\n1. Cadastrar time")
    print("2. Remover time")
    print("3. Cadastrar jogador")
    print("4. Remover jogador")
    print("5. Atualizar time de jogador")
    print("6. Listar jogadores de um time")
    print("7. Emitir relatório de todos os jogadores")
    print("8. Emitir relatório de todos os times")
    print("9. Sair")
    
    option = input("Escolha uma opção: ")
    
    if option == "1":
        add_team()
    elif option == "2":
        remove_team()
    elif option == "3":
        add_player()
    elif option == "4":
        remove_player()
    elif option == "5":
        update_player_team()
    elif option == "6":
        get_players_in_team()
    elif option == "7":
        get_players_report()
    elif option == "8":
        get_teams_report()
    elif option == "9":
        break
    else:
        print("Opção inválida. Tente novamente.")
