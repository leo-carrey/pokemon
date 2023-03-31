import json


def open_json(destination):
    with open(f'{destination}.json') as f:
        data = json.load(f)
    return data


def dump_json(destination, data):
    with open(f'{destination}.json', 'w') as f:
        json.dump(data, f, indent=4)


pokedex = open_json('pokemon')
type_pokemon = open_json('tableau_types')


class Pokemon:
    def __init__(self, name):
        self.__name = name
        self.type = pokedex[name]["type"]
        self.__hp = pokedex[name]["hp"]
        self.attack = pokedex[name]["attack"]
        self.defense = pokedex[name]["defense"]
        self.specialAttack = pokedex[name]["specialAttack"]
        self.specialDefense = pokedex[name]["specialDefense"]
        self.speed = pokedex[name]["speed"]
        self.moves = pokedex[name]["moves"]


    def __str__(self):
        return f"Name : {self.__name}\nType : {self.type}\nHp : {self.__hp}\nAttack : {self.attack}\nDefense : {self.defense}\nSpecialAttack : {self.specialAttack}\nSpecialDefense : {self.specialDefense}\nSpeed : {self.speed}\n"

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

