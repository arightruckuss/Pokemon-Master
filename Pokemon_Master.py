import random
from random import randint

#pokeman battle
#pokemon can challange another pokemon only the challengers health and experience_level are affected
#pokemon is unable to flight if they are already knocked out and can be reveived
#pokemon winner is determined by there type.
#If the types are the same the winner is determined by random speed values
#pokemon health is restored to max once experience level reaches 5
#super classes are used to revive pokemen and trainers

#create pokemon class with functions and variables
class Pokemon:
    def __init__(self, name, experience_level, type, current_health):
        self.name = name
        self.experience_level = experience_level
        self.type = type
        self.current_health = current_health
        self.max_health = 10
        self.is_ko = False   

    #checks if pokemon has the same type or checks which pokemon wins based on there type
    def pokemon_attack(self, pokemon2):
        #checks if either pokemon is already knocked out
        if self.current_health <= 0:
            return print('{challanger} is already knocked out!!'.format(challanger = self.name))
        if pokemon2.current_health <= 0:
            return print('{pokemon2} is already knocked out!!'.format(pokemon2 = pokemon2.name))
        self.pokemon_challange(pokemon2)
        #checks if pokemen types are the same 
        if self.type == pokemon2.type:
            print('Pokemon type\'s are the same which pokemon will be faster!!')
            #create random intergers to represent the speed the pokemen fire
            self_speed = [randint(1, 5)]
            pokemon2_speed = [randint(1, 5)]
            #if the speed if the same pokemen cancel each other
            if self_speed == pokemon2_speed:
                print('Both pokemen fire at the same time and cancel each other out!')
            #winner is determined by the higher number interger presenting the pokemen speed
            elif self_speed > pokemon2_speed:
                print('{pokemon} is faster'.format(pokemon = self.name))
                self.gain_health(pokemon2)
            else:
                print('{pokemon} is to slow challenger loses'.format(pokemon = self.name))
        #checks the winner if pokemen type's are different        
        elif self.type == 'Fire' and pokemon2.type == 'Grass':
            self.gain_health(pokemon2)
        elif self.type == 'Fire' and pokemon2.type == 'Water':
            self.lose_health(pokemon2)
        elif self.type == 'Water' and pokemon2.type == 'Fire':
            self.gain_health(pokemon2) 
        elif self.type == 'Water' and pokemon2.type == 'Grass':
            self.lose_health(pokemon2)
        elif self.type == 'Grass' and pokemon2.type == 'Water':
            self.gain_health(pokemon2)
        elif self.type == 'Grass' and pokemon2.type == 'Fire':
            self.lose_health(pokemon2)

    #prints pokemon challange flight
    def pokemon_challange(self, pokemon2):
        print('{pokemon}\'s type of '.format(pokemon = self.name) + self.type + ' challenges {pokemon2}\'s type of '.format(pokemon2 = pokemon2.name) + pokemon2.type + '!')
        
    #increases pokemons health and level if pokemon challanger wins
    def gain_health(self, pokemon2):
        self.current_health += 1
        self.experience_level += 1
        if self.current_health > 10:
            self.current_health = self.max_health
            print(self.name + ' defeats ' + pokemon2.name +'! {pokemon}\'s health is at max health '.format(pokemon = self.name) + str(self.current_health))
        else:
            print(self.name + ' defeats ' + pokemon2.name +'! {pokemon}\'s health increases to: '.format(pokemon = self.name) + str(self.current_health))
        if self.experience_level == 5:
            self.restore_health()

    #decreases pokemons health if pokemon challanger loses       
    def lose_health(self, pokemon2):
        self.current_health -= 1
        print(pokemon2.type + ' defeats ' + self.type +'! {pokemon}\'s health decreases to : '.format(pokemon = self.name) + str(self.current_health))
        if self.current_health == 0:
            self.is_knocked_out()


    #changes pokemon's is_ko to true, sets current_health to 0 and prints KO statement
    def is_knocked_out(self):
        self.is_ko = True
        self.current_health = 0
        print('{pokemon}\'s has been knocked out!!'.format(pokemon = self.name))

    #restores pokemen health to max once experience level(pokemen beaten) has reached 5
    def restore_health(self):
        self.current_health = 10
        self.experience_level = 0
        print('{pokemon} has beaten 5 pokemen health is restored to max! '.format(pokemon = self.name))

#inherit from Pokemon class to revive Pokemon
class revive_pokemon(Pokemon):
    def __init__(self, name, experience_level, type, current_health):
        super().__init__(name, experience_level, type, current_health)
        self.current_health = 5
        self.is_ko = False
        print(self.name + ' has been revived with health at ' + str(self.current_health))
       
#trainer battles
#trainer fights are based on the amount of potions the trainer has
#if potions are equal winner is
#trainer class determined on trainers attack over defense
#challengers uses potions 1 each time they flight
#challengers attack and potions increases every time a trainers wins with no limits
#challengers defense increases every time trainers loses and gains a potion with no limits

class Trainer:
    def __init__(self, current_pokemen, attack, defense, potions, current_health, name):
        self.potions = potions
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        self.name = name
        self.max_health = 10
        self.is_ko = False

    #prints the challenge
    def trainer_challange(self, trainer2):
            print('Trainer {trainer} challanges'.format(trainer = self.name) + ' trainer {trainer2} '.format(trainer2 = trainer2.name))

    #create's trainer fight envokes trainer_fight_tie, gain_health or lose_health
    def trainer_attack(self, trainer2):
        self.trainer_challange(trainer2)
        if self.potions == trainer2.potions:
            print('Both trainers have the same amount of potions who has the better attack over defense!?')
            self.potions -= 1
            self.trainer_fight_tie(trainer2)
        elif self.potions > trainer2.potions:
            self.gain_health(trainer2)
            self.attack += 1
        else:
            self.lose_health(trainer2)
            self.defense += 1
            trainer2.potions += 1

    #if trainers potions are tied winner is determined on trainers attack over defense    
    def trainer_fight_tie(self, trainer2):
        if self.attack == trainer2.defense:
            return print('Trainers are  equal and cancel each other out!')
        elif self.attack > trainer2.defense:
            print('{trainer1}'.format(trainer1 = self.name) + ' defeats ' + trainer2.name + '  with more attack and gains health!')
            print('{trainer1}'.format(trainer1 = self.name) + '\'s health is now ' + str(self.current_health))
            self.attack += 1
            self.potions += 1
        else:
            print('{trainer2}'.format(trainer2 = trainer2.name) + ' defends attack against ' + self.name + ' and gains defense')
            self.defense += 1
            trainer2.potions += 1

    #increases trainers health if they when there fight
    def gain_health(self, trainer2):
        self.current_health += 1
        self.attack += 1
        self.potions += 1
        #prevents health from going higher than 10
        if self.current_health > 10:
            self.current_health = self.max_health
        print('{trainer1}'.format(trainer1 = self.name) + ' defeats ' + trainer2.name + ' and gains health!')
        print('{trainer1}'.format(trainer1 = self.name) + '\'s health is now ' + str(self.current_health))


    #decreases trainers health if they when there fight       
    def lose_health(self, trainer2):
        self.current_health -= 1
        self.defense += 1
        #prevents health from going below 0
        if self.current_health <= 0:
            self.current_health = 0
        if self.potions < trainer2.potions:
            print('{trainer1}'.format(trainer1 = self.name) + ' loses to {trainer2}'.format(trainer2 = trainer2.name) + ' and loses health')
            print('{trainer1}'.format(trainer1 = self.name) + '\'s health is now ' + str(self.current_health))

    #trainer switchs to another pokemon if pokemon's health is 0  
    def switch_pokemon(self, current_pokemon):
        if current_pokemon.current_health < 0:
            if current_pokemon in pokemen:
                #removes the current pokemon from the pokemen list so he is not picked 
                pokemen.remove(current_pokemon)
                new_training_pokemon = random.choice(pokemen)
                print('{current_pokemon} has no health! '.format(current_pokemon = current_pokemon.name) + self.name + ' switches to train ' + str(new_training_pokemon.name))

#inherit from Trainer class to revive Trainers 
class revive_trainer(Trainer):
    def __init__(self, current_pokemen, attack, defense, potions, current_health, name):
        super().__init__(current_pokemen, attack, defense, potions, current_health, name)
        self.current_health = 5
        self.potions = 5
        self.is_ko = False
        print(self.name + ' has been revived with health at ' + str(self.current_health))
        
#pokemen
charizard = Pokemon('Charizard', 4, 'Water', 1)
pikachu = Pokemon('Pikachu', 3, 'Fire', 4)
snorlax = Pokemon('Snorlax', 2, 'Grass',7)
eevee = Pokemon('Eevee', 1, 'Grass', 11)
mewtwo = Pokemon('Mewtwo', 4, 'Water', 1)
celebi = Pokemon('Celebi', 5, 'Fire', 0)
pokemen = [charizard, pikachu, snorlax, eevee, mewtwo, celebi]

#trainers 
leaf = Trainer([charizard, pikachu], 4, 4, 5, 5, 'Leaf')
cynthia = Trainer([snorlax, eevee], 6, 2, 4, 3, 'Cynthia')
elaine = Trainer([pikachu, eevee], 5, 4, 5, 1, 'Elaine')
allister = Trainer([pikachu, eevee], 6, 3, 3, 3, 'Allister')
gloria = Trainer([snorlax, charizard], 3, 8, 3, 0, 'Gloria')

#pokemon challenges
charizard.pokemon_attack(pikachu)
mewtwo.pokemon_attack(snorlax)
eevee.pokemon_attack(charizard)
charizard.pokemon_attack(snorlax)

#trainer challenges 
elaine.trainer_attack(allister)
leaf.trainer_attack(cynthia)
elaine.trainer_attack(allister)

#knocked out pokemon and trainer are revived
revive_pokemon('Celebi', 5, 'Water', 0)
revive_trainer([snorlax, charizard], 3, 8, 3, 0, 'Gloria')
