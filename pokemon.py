import time
import numpy as np      # Instalar el modulo: pip install numpy
import sys

# Imprime lentamente las caracteristicas del objetivo
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['Ataque']
        self.defense = EVs['Defensa']
        self.health = health
        self.bars = 20


    def fight(self, Pokemon2):
        # Permite que Pokemon pelee con Pokemon2

        # Imprime información de la batalla

        print("---BATALLA---")
        print(f"\n{self.name}")
        print("Tipo/", self.types)
        print("Ataque/", self.attack)
        print("Defensa/", self.defense)
        print("Level/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("Tipo/", Pokemon2.types)
        print("Ataque/", Pokemon2.attack)
        print("Defensa/", Pokemon2.defense)
        print("Level/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Ventajas de tipo
        version = ['Fuego', 'Agua', 'Planta']
        for i,k in enumerate(version):
            if self.types == k:
                # Si los dos son el mismo tipo
                if Pokemon2.types == k:
                    string_1_attack = '\nEsto es efectivo...!'
                    string_2_attack = '\nEsto no es efectivo...'

                # Pokemon2 es fuerte a

                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nEsto es efectivo...!'
                    string_2_attack = '\nEsto no es efectivo...'

                # Pokemon2 es débil a

                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nEsto es efectivo...!'
                    string_2_attack = '\nEsto no es efectivo...'



        # Continuar mientras los pokemon tengan ps

        # Imprime los ps de cada pokemon
        while (self.bars > 0) and (Pokemon2.bars > 0):
            print(f"\n{self.name}\t\tPS\t{self.health}")
            print(f"{Pokemon2.name}\t\tPS\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):    # Obtenemos el indice y el nombre del movimiento en pantalla
                print(f"{i+1}.", x)
            index = int(input('Seleccione un movimiento: '))
            delay_print(f"\n{self.name} usó {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determina el daño
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Añade barras de defensa
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Checked si el pokemon ha sido derrotado
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' derrotado.')
                break

            # Turno de Pokemon2

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Seleccione un movimiento: '))
            delay_print(f"\n{Pokemon2.name} usó {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determina el daño
            self.bars -= Pokemon2.attack
            self.health = ""

            # Defensa
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tPS\t{self.health}")
            print(f"{Pokemon2.name}\t\tPS\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check si el pokemon está derrotado
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' derrotado.')
                break

        # money = np.random.choice(5000)
        # delay_print(f"\nOpponent paid you ${money}.\n")




if __name__ == '__main__':
    #Crear pokemon

    Charizard = Pokemon('Charizard', 'Fuego', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'Ataque':12, 'Defensa': 8})
    Blastoise = Pokemon('Blastoise', 'Agua', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'Ataque': 10, 'Defensa':10})
    Venusaur = Pokemon('Venusaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'Ataque':8, 'Defensa':12})

    Charmander = Pokemon('Charmander', 'Fuego', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'Ataque':4, 'Defensa':2})
    Squirtle = Pokemon('Squirtle', 'Agua', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'Ataque': 3, 'Defensa':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Planta', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'Ataque':2, 'Defensa':4})

    Charmeleon = Pokemon('Charmeleon', 'Fuego', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'Ataque':6, 'Defensa':5})
    Wartortle = Pokemon('Wartortle', 'Agua', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'Ataque': 5, 'Defensa':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Planta', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'Ataque':4, 'Defensa':6})


    Charizard.fight(Blastoise) # Get them to fight