class Weapon:
    def __init__(self, name):
        self.name = name

    def use (self,monster):
        pass

class SilverSword(Weapon):
    def __init__(self):
        super().__init__('Серебрянный меч')
        self.dmg = 30

    def use(self,monster):
        print (f'Охотник наносит рассекающий удар {self.name}! {self.dmg} урона.')
        monster.take_damage(self.dmg)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__('Святая вода')
        self.dmg = 20

    def use(self,monster):
        print (f'Охотник обливает врага: {self.name}. {self.dmg} урона.')
        monster.take_damage(self.dmg)


class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__('Арбалет с болтом')
        self.dmg = 25

    def use(self,monster):
        print (f'Охотник делает выстрел: {self.name}! На {self.dmg} урона')
        monster.take_damage(self.dmg)
