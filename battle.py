from pokemon import Pokemon
import random


class Battle:

    def __init__(self):
        self.starter_arr = ["Bulbizarre", "Carapuce", "Salameche"]
        self.player_pokemon = Pokemon("Carapuce")
        self.player_turn = True
        self.enemy_fuc()
        self.checkspeed()
        self.player_moves()
        self.get_stats()

    def enemy_fuc(self):
        self.enemy = Pokemon(random.choice(self.starter_arr))

    def checkspeed(self):
        if self.player_pokemon.speed >= self.enemy.speed:
            self.player_turn = True
        else:
            self.player_turn = False

    def player_moves(self):
        if self.player_turn:
            print(f"1 Attack : {self.player_pokemon.moves[2]}\n2 Defense : {self.player_pokemon.moves[0]}\n3 SpecialAttack : {self.player_pokemon.moves[3]}\n4 SpecialDefense : {self.player_pokemon.moves[1]}")
            userinput = input("you choose the skill: ")
        else:
            print(f"{self.enemy.get_name()} use {random.choice(self.enemy.moves)}")

    def get_stats(self):
        print(f"your {self.player_pokemon.get_name()} have {self.player_pokemon.get_hp()} hp")
        print(f"{self.enemy.get_name()} have {self.enemy.get_hp()} hp")


game = Battle()
