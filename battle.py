import random
from nation import Nation


class Battle:

    def __init__(self, attacker: Nation, defender: Nation):
        self.attacker = attacker
        self.defender = defender

        self.outcome = self.battle()

    def battle(self):
        attacker_original_soldiers = self.attacker.soldiers
        defender_original_soldiers = self.defender.soldiers

        while self.attacker.soldiers > 0 and self.defender.soldiers > 0:
            attacker_regiment = 100
            defender_regiment = 100

            attacker_regiment = self.clash(attacker_regiment)
            defender_regiment = self.clash(defender_regiment)

            self.attacker.soldiers = self.attacker.soldiers - (100 - attacker_regiment)
            self.defender.soldiers = self.defender.soldiers - (100 - defender_regiment)


        if self.attacker.soldiers < 0:
            self.attacker.soldiers = 0
        if self.defender.soldiers < 0:
            self.defender.soldiers = 0
            self.attacker.add_regions(self.defender.regions)
            self.defender.regions = []

        return attacker_original_soldiers - self.attacker.soldiers, defender_original_soldiers - self.defender.soldiers

    def clash(self, regiment):
        roll = random.randint(1, 10)
        return regiment - (roll * 10)