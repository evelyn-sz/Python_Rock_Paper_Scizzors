class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def winning_power(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scizzors":
            return player_1.name

        if player_1.choice == "Scizzors" and player_2.choice == "Paper":
            return player_1.name

        if player_1.choice == "Paper" and player_2.choice == "Rock":
            return player_1.name

        return player_2.name



# def winning_power(power_1, power_2):
#     if power_1.name == "Rock" and power_2.name == "Scizzors":
#         return power_1

#     if power_1.name == "Scizzors" and power_2.name == "Paper":
#         return power_1

#     if power_1.name == "Paper" and power_2.name == "Rock":
#         return power_1

#     return power_2