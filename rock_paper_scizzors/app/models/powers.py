from app.models.power import Power

rock = Power("Rock")
paper = Power("Paper")
scizzors = Power("Scizzors")

def winning_power(power_1, power_2):
    if power_1.name == "Rock" and power_2.name == "Scizzors":
        return power_1

    if power_1.name == "Scizzors" and power_2.name == "Paper":
        return power_1

    if power_1.name == "Paper" and power_2.name == "Rock":
        return power_1

    return power_2