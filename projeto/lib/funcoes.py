from database import Database

db = Database()

def cadastrar_time(nome_time):
    return db.add_team(nome_time)

def remover_time(nome_time):
    return db.remove_team(nome_time)

def cadastrar_jogador(nome_jogador, nome_time):
    return db.add_player(nome_jogador, nome_time)

def remover_jogador(nome_jogador):
    return db.remove_player(nome_jogador)

def atualizar_time_jogador(nome_jogador, novo_time):
    return db.update_player_team(nome_jogador, novo_time)

def listar_jogadores_time(nome_time):
    return db.get_players_in_team(nome_time)

def emitir_relatorio_jogadores():
    return db.get_players_report()

def emitir_relatorio_times():
    return db.get_teams_report()
