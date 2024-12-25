
#player class to hold all personal statistics
class Player():
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.statistics = {"FGA": 0,
                           "FGM": 0,
                           "FTA": 0,
                           "FTM": 0,
                           "3PA": 0,
                           "3PM": 0,
                           "AS": 0,
                           "RB": 0}
        

        def add_FG(self, status):
            self.statistics["FGA"] += 1
            if status == "Scored":
                self.statistics["FGM"] += 1

        def add_FT(self, status):
            self.statistics["FTA"] += 1
            if status == "Scored":
                self.statistics["FTM"] += 1
        
        def add_3P(self, status):
            self.statistics["3PA"] += 1
            if status == "Scored":
                self.statistics["3PM"] += 1
            
        def add_assist(self):
            self.statistics["AS"] += 1
        
        def add_rebound(self):
            self.statistics["RB"] += 1




class Team():
    def __init__(self, name, afkorting):
        self.name = name
        self.abbreviation = afkorting
        self.players = {}
    

    def add_player(self, player_name, player_number):
        self.players[player_number] = Player(player_name, player_number)
    
    def get_player(self, number):
        return self.players[number]
    
    def all_players(self):
        return self.players.keys()
    


class Match():
    def __init__(self):
        self.teams = []
    

    def read_match_data_file(self):
        data_lines = None
        with open("Match_data.txt", "r", encoding= "utf-8") as data_file:
            data_lines = data_file.readlines()
        for line in data_lines:
            splited = line.strip("\n").split(" - ")
            if splited[0] == "Team":
                self.teams.insert(0, Team(splited[1], splited[2]))
            
            else:
                self.teams[0].add_player(splited[1], splited[0])
            
    
    def get_team(self, afkorting):
        if self.teams[0].abbreviation == afkorting:
            return self.teams[0]
        elif self.teams[1].abbreviation == afkorting:
            return self.teams[1]
        else:
            raise(AssertionError(f"This team is not in this match: {afkorting}"))
        


    

    
match = Match()
match.read_match_data_file()
