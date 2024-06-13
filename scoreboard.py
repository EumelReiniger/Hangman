class Scoreboard:
    def __init__(self):
        self.score = 0

    def update_score(self, points):
        self.score += points

    def display_score(self):
        print("Score: {}".format(self.score))

# Beispiel-Nutzung
scoreboard = Scoreboard()
scoreboard.update_score(1)
scoreboard.display_score()