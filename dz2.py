import random


class Pet:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 0
        self.alive = True

    def to_study(self):
        print("Time to eat")
        self.satiety += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Play time")
        self.gladness +=5
        self.satiety -= 0.1

    def is_alive(self):
        if self.satiety < -0.5:
            print("Your pet ran away")
            self.alive = False
        elif self.gladness <= 0:
            print("Your pet ran away")
            self.alive = False
        elif self.satiety > 5:
            print("Your pet is still home")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")

    def live(self, day):
        day = f"Day {day} of {self.name} live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


pet1 = Pet(name="Pushok")

for day in range(365):
    if pet1.alive == False:
        break
    pet1.live(day)


# satiety = ситий