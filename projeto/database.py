class Database:
    def __init__(self):
        self.teams = {}
        self.players = {}

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = []
            return True
        return False

    def remove_team(self, team_name):
        if team_name in self.teams:
            del self.teams[team_name]
            return True
        return False

    def add_player(self, player_name, team_name):
        if player_name not in self.players:
            if team_name in self.teams:
                self.players[player_name] = team_name
                self.teams[team_name].append(player_name)
                return True
        return False

    def remove_player(self, player_name):
        if player_name in self.players:
            team_name = self.players[player_name]
            del self.players[player_name]
            self.teams[team_name].remove(player_name)
            return True
        return False

    def update_player_team(self, player_name, new_team_name):
        if player_name in self.players:
            current_team_name = self.players[player_name]
            if current_team_name != new_team_name and new_team_name in self.teams:
                self.teams[current_team_name].remove(player_name)
                self.players[player_name] = new_team_name
                self.teams[new_team_name].append(player_name)
                return True
        return False

    def get_players_in_team(self, team_name):
        return self.teams.get(team_name, [])

    def get_all_players(self):
        return list(self.players.keys())

    def get_all_teams(self):
        return list(self.teams.keys())

    def get_players_report(self):
        return "\n".join(self.get_all_players())

    def get_teams_report(self):
        return "\n".join(self.get_all_teams())
