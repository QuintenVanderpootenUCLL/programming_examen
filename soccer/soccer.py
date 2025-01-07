class Team():
    def __init__(self, naam):
        self.name = naam
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0
        self.goals_scored = 0 
        self.goals_conceded = 0
        self.goal_difference = 0
        self.points = 0
    

    def play(self, opponent, punten_home, punten_out):
        #eigen stats
        self.goals_scored += punten_home
        self.goals_conceded += punten_out
        self.goal_difference += punten_home - punten_out
        self.games_played += 1
        #opponent stats
        opponent.goals_scored += punten_out
        opponent.goals_conceded += punten_home
        opponent.goal_difference += punten_out - punten_home
        opponent.games_played += 1
        #winnaar bepalen
        if punten_home > punten_out:
            self.games_won += 1
            opponent.games_lost += 1
            self.points += 3
        elif punten_home == punten_out:
            self.games_drawn += 1
            opponent.games_drawn += 1
            self.points += 1
            opponent.points += 1
        else:
            self.games_lost += 1
            opponent.games_won += 1
            opponent.points += 3



class Competitoin():
    def __init__(self):
        self.teams = {}
    

    def add_team(self, naam):
        self.teams[naam] = Team(naam)
    

    def get_team(self, naam):
        return self.teams[naam]

    
    def update_competition(self, updates):
        for update in updates:
            team_a, team_b, score_a, score_b = update
            team_a_object = self.teams.get(team_a, None)
            team_b_object = self.teams.get(team_b, None)
            if team_a_object == None:
                self.add_team(team_a)
                team_a_object = self.get_team(team_a)
            if team_b_object == None:
                self.add_team(team_b)
                team_b_object = self.get_team(team_b)
            team_a_object.play(team_b_object, score_a, score_b)
    

    def display_table(self):
        result = ""
        result += "Team                | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts\n"
        for team in self.teams.values():
            line = ( 
                f"{team.name.ljust(20, ' ')}| " 
                f"{str(team.games_played).ljust(4, ' ')}| " 
                f"{str(team.games_won).ljust(4, ' ')}| "
                f"{str(team.games_drawn).ljust(4, ' ')}| " 
                f"{str(team.games_lost).ljust(4, ' ')}| " f"{str(team.goals_scored).ljust(5, ' ')}| " 
                f"{str(team.goals_conceded).ljust(5, ' ')}| " 
                f"{str(team.goal_difference).ljust(5, ' ')}| " 
                f"{team.points}\n" 
                )
            result += line
        result = result[:len(result)- 1]
        return result



    def read_match_data_file(self, filename):
        update  = []
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        for line in lines:
            teams, score = line.split(":")
            team1 , team2 = teams.split(" - ")
            score1 , score2 = score.split(" - ")
            update.append((team1, team2, int(score1), int(score2)))
        self.update_competition(update)

    
    def write_table(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.display_table())


def process_match_data(match_data_file_name, output_file_name):
    competitie = Competitoin()
    competitie.read_match_data_file(match_data_file_name)
    competitie.write_table(output_file_name)
        


process_match_data('match_data.txt', 'output.txt')
