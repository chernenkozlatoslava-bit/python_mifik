import random

brand_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 5}
}

pet_list = {
    "Cat": {"food_less": 6, "gladness_up": 10},
    "Dog": {"food_less": 10, "gladness_up": 15},
    "Parrot": {"food_less": 2, "gladness_up": 7},
    "Hamster": {"food_less": 1, "gladness_up": 4}
}


class Human:

    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()


    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_pet(self):
        self.pet = Pet(pet_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def play_pet(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.gladness += self.pet.gladness_up
            self.home.food -= self.pet.food_less


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return


    def shopping(self, manage):
        if self.car.drive():
            pass

        else:
            self.to_repair()
            return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicates":
            print("Hooray! delicates!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15



    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0


    def to_repair(self):
            self.car.strength += 100
            self.money -= 50

    def days_indexes(self, day):
        day = f"Today the {day}, of {self.name},s live"
        print(f"{day:=^40}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I get a job {self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"I have a pet {self.pet.pet}")
        self.days_indexes(day)
        dice = random.randint(1, 5)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I clean the house")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need repair my car")
            self.to_repair()
        elif dice == 1:
            print("Chill!")
            self.chill()
        elif dice == 2:
            print("Clean time")
            self.clean_home()
        elif dice == 3:
            print("Start working")
            self.work()
        elif dice == 4:
            print("Time to treats")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Time to play with pet")
            self.play_pet()




class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move")
            return False


class House:

    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

class Pet:
    def __init__(self, pet_list):
        self.pet = random.choice(list(pet_list))
        self.food_less = pet_list[self.pet]["food_less"]
        self.gladness_up = pet_list[self.pet]["gladness_up"]


persona = Human(name="Nastya")

for day in range(1, 12):
    if persona.live(day) == False:
        break