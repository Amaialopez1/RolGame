import time
import numpy as np  # Instalar el modulo: pip install numpy
import sys

from mysqlx.protobuf.t import x
from numpy import void
from sqlalchemy import Column, String, Integer, Float


# Imprime lentamente las caracteristicas del objetivo
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, stats, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = stats['Ataque']
        self.defense = stats['Defensa']
        self.health = health
        self.bars = 20

    def attack(self, enemy, type_attack):
        self.attack -= 4
        return


class PokemonAttack:
    __tablename__ = "pokemon_attack"
    id = Column(String(255), primary_key=True)
    attack_id = Column(String(255), primary_key=True)
    pokemon_id = Column(String(255), primary_key=True)


class Attack:
    __tablename__ = "attack"
    id = Column(String(255), primary_key=True)
    type = Column(String(255))
    name = Column(String(255))
    power = Column(Integer)


class PokemonTrainer:
    __tablename__ = "pokemon_trainer"
    id = Column(String(255), primary_key=True)
    trainer_id = Column(String(255), primary_key=True)
    pokemon_id = Column(String(255), primary_key=True)
    level = Column(Integer)
    health = Column(Float)


class Trainer:
    __tablename__ = "trainer"
    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    username = Column(String(255))
    experience = Column(Integer)
    email = Column(String(255))
    password = Column(String(255))
    position_x = Column(Integer)
    position_y = Column(Integer)
    pokemons: []
    user_id = Column(String(255), primary_key=True)

    def move(self, x, y):
        pass


if __name__ == '__main__':
    # Crear pokemon

    Charizard = Pokemon('Charizard', 'Fuego', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                        {'Ataque': 12, 'Defensa': 8})
    Blastoise = Pokemon('Blastoise', 'Agua', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                        {'Ataque': 10, 'Defensa': 10})
    Venusaur = Pokemon('Venusaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],
                       {'Ataque': 8, 'Defensa': 12})

    Charmander = Pokemon('Charmander', 'Fuego', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                         {'Ataque': 4, 'Defensa': 2})
    Squirtle = Pokemon('Squirtle', 'Agua', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'Ataque': 3, 'Defensa': 3})
    Bulbasaur = Pokemon('Bulbasaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],
                        {'Ataque': 2, 'Defensa': 4})

    Charmeleon = Pokemon('Charmeleon', 'Fuego', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                         {'Ataque': 6, 'Defensa': 5})
    Wartortle = Pokemon('Wartortle', 'Agua', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                        {'Ataque': 5, 'Defensa': 5})
    Ivysaur = Pokemon('Ivysaur\t', 'Planta', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],
                      {'Ataque': 4, 'Defensa': 6})

    Charmander.fight(Squirtle)  # Selecciona pokemon y pelea
