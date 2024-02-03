from random import randint
import requests
from datetime import datetime, timedelta
import time

hunger = 0
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.hp = randint(25, 100)
        self.power = randint(5, 20)
        #self.info = self.info()
        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"

    
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "Pikachu"
    

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  
    #def feed(self):
        #global hunger
        #if hunger < 3:
            #hunger += 1
            #return "Покемон покормлен!"
        #else:
            #return "Покемон сыт. Может пришло время тренировки?"
        

    #def train(self):
        #url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        #response = requests.get(url)
        #global hunger
        #if hunger != 0 and response.status_code == 200:
            #hunger -= 1
            #self.ability +=1
            #return f"Статистики повышены! Статистики: {self.ability}"
        #else:
            #return "Покемон голоден. Может надо его покормить?"


    # Метод класса для получения информации


    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def lvl(self):
        return f"Начальные статистики: {self.ability}"


    def info(self):
        return f"""Имя твоего покеомона: {self.name}
        сила покемона: {self.power}
        здоровье покемона: {self.hp}"""
    

class Fighter(Pokemon):
    def attack(self, enemy):
        sup = randint(5,15)
        self.power += sup
        result = super().attack(enemy)
        self.power -= sup
        return result + f"\n Боец применил супер-атаку силой:{super} "

class Wizard(Pokemon):
    def feed(self):
        return super().feed(10)


wizard = Wizard("username1")
fighter = Fighter("username2")
time.sleep(21)
print(wizard.feed())
print()
print(fighter.info())
print()
print(fighter.attack(wizard))