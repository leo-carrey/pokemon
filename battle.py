from pokemon import Pokemon
import random


class Battle:

    STARTER_POKEMONS = ["Bulbizarre", "Carapuce", "Salameche"]
    MOVES_ARR = [0, 1, 2, 3]

    def __init__(self):
        self.player_pokemon = Pokemon("Carapuce")
        self.enemy_pokemon = Pokemon(random.choice(self.STARTER_POKEMONS))
        self.player_hp = self.player_pokemon.get_hp()
        self.enemy_hp = self.enemy_pokemon.get_hp()
        self.checkspeed()

    def checkspeed(self):
        if self.player_pokemon.speed >= self.enemy_pokemon.speed:
            self.player_turn()
        else:
            self.enemy_turn()

    def player_turn(self):
        print(
            f"0 - {self.player_pokemon.moves[0]}\n1 - {self.player_pokemon.moves[1]}\n2 - {self.player_pokemon.moves[2]}\n3 - {self.player_pokemon.moves[3]}")

        while True:
            user_input = input("choose a move : ")
            if int(user_input) in self.MOVES_ARR:
                self.get_stats(int(user_input))
                break
            else:
                print("please enter a number in range 0 at 3")

        if self.check_win():
            self.enemy_turn()

    def enemy_turn(self):
        random_choice = random.choice(self.enemy_pokemon.moves)
        print(f"{self.enemy_pokemon.get_name()} use {random_choice}")
        self.player_hp -= int(self.enemy_pokemon.move[random_choice]["power"] *
                              self.enemy_pokemon.type_attack[self.enemy_pokemon.type][self.player_pokemon.type])
        self.set_hp()
        print(f"your {self.player_pokemon.get_name()} have {self.player_hp} hp")
        print(f"{self.enemy_pokemon.get_name()} have {self.enemy_hp} hp")
        if self.check_win():
            self.player_turn()

    def print_move(self, i):
        print(
            f"your {self.player_pokemon.get_name()} use {self.player_pokemon.moves[i]}")

    def operation_degat(self, i):
        self.enemy_hp -= int(self.player_pokemon.move[self.player_pokemon.moves[i]]["power"]
                             * self.player_pokemon.type_attack[self.player_pokemon.type][self.enemy_pokemon.type])

    def get_stats(self, i):
        self.print_move(i)
        self.operation_degat(i)
        self.set_hp()
        print(f"your {self.player_pokemon.get_name()} have {self.player_hp} hp")
        print(f"{self.enemy_pokemon.get_name()} have {self.enemy_hp} hp")

    def set_hp(self):
        if self.player_hp <= 0:
            self.player_hp = 0
        if self.enemy_hp <= 0:
            self.enemy_hp = 0

    def check_win(self):
        if self.player_hp <= 0:
            print("enemy win")
            return False
        if self.enemy_hp <= 0:
            print("you win")
            self.enemy_hp = self.enemy_pokemon.get_hp()
            self.enemy_pokemon = Pokemon(random.choice(self.STARTER_POKEMONS))
            return True
        else:
            return True


game = Battle()