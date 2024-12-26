
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
        return self.players.values()
    


class Match():
    def __init__(self):
        self.teams = []
    

    def read_match_data_file(self, file):
        data_lines = None
        with open(file, "r", encoding= "utf-8") as data_file:
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
    

    def read_match_statistics_file(self, file):
        data_lines = None
        with open(file , "r", encoding= "utf-8") as data_file:
            data_lines = data_file.readlines()
        for line in data_lines:
            splitted = line.strip("\n").split(",")
            team = splitted[0]
            player = splitted[1]
            action = splitted[2]
            if  action == "FG":
                self.get_team(team).get_player(player).add_FG(splitted[3])
            elif action == "FT":
                self.get_team(team).get_player(player).add_FT(splitted[3])
            elif action == "3P":
                self.get_team(team).get_player(player).add_3P(splitted[3])
            elif action == "AS":
                self.get_team(team).get_player(player).add_assist()
            elif action == "RB":
                self.get_team(team).get_player(player).add_rebound()
            else:
                raise(AssertionError(f"This is not a action:{action}"))
    
    def display_match(self):
        string = ""
        line = "------------------------------------------------------------------------------------"
        for team in self.teams:
            string += "\n" + line
            substring = f"\n| {team.name}"
            amount_of_spaces = len(line) - len(substring)
            substring += amount_of_spaces * " "
            substring += "|"
            string += substring
            string += "\n"
            string += line
            string += "\n"
            stats = "| Nbr | Name                         | FGA | FGM | 3PA | 3PM | FTA | FTM | AS | RB |"
            string += stats
            for player in team.all_players():
                substring = "\n"
                nbr = f"| {player.number}"
                substring += nbr + ((6 - len(nbr)) * " ")
                name = f"/ {player.name}"
                substring += name + ((31 - len(name)) * " ")
                fga = f"/ {player.statistics["FGA"]}   "
                substring += fga
                substring += f"/ {player.statistics["FGM"]}   "
                substring += f"/ {player.statistics["3PA"]}   "
                substring += f"/ {player.statistics["3PM"]}   "
                substring += f"/ {player.statistics["FTA"]}   "
                substring += f"/ {player.statistics["FTM"]}   "
                substring += f"/ {player.statistics["AS"]}  "
                substring += f"/ {player.statistics["RB"]}  "
                substring += "/"
            
                string += substring
            string += "\n" + line
            string = string[1:]

        return string


    def write_match_details(self, file):
        with open(file, "w", encoding="utf-8") as output_file:
            output_file.write(self.display_match())

    
match = Match()
match.read_match_data_file("Match_data.txt")
match.read_match_statistics_file("match_statistics.txt")
match.write_match_details("output.txt")