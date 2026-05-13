import random

class Monster():
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg


    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return True if self.__hp > 0 else False

    def show_status(self):
        print (f'{self.__name} HP: {self.__hp}')

    def take_damage(self, damage):
        self.set_hp(self.__hp - damage)

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp() - self.__dmg)


class Zombie(Monster):
    def __init__(self, name = 'Зомби'):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print (f'{self.get_name()} теряет конечность! Получено {damage}. HP: {self.get_hp()}')


class Vampire(Monster):
    def __init__(self, name = 'Вампир'):
        super().__init__(name,80,15)

    def take_damage(self, damage):
        feature = max (0, damage - 5)
        self.set_hp(self.get_hp() - feature)
        print (f'{self.get_name()} поглащает 5 урона! Получено {feature}. HP: {self.get_hp()}')


class Ghost(Monster):
    def __init__(self, name = 'Призрак'):
        super().__init__(name,60,20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print (f'{self.get_name()} уклонился от удара! Не прошло {damage}. HP: {self.get_hp()}')
        else:
            self.set_hp(self.get_hp() - damage)
            print (f'{self.get_name()} пропустил двоечку! Получено {damage}. HP: {self.get_hp()}')


class Werewolf(Monster):
    def __init__(self, name = 'Оборотень'):
        super().__init__(name,100,25)
        self.__transformed = False

    def take_damage(self,damage):
        self.set_hp(self.get_hp() - damage)
        print (f'{self.get_name()} получает в пасть! Получено {damage}. HP: {self.get_hp()}')
        if self.__hp < 50 and self.__transformed == False:
            print (f'{self.get_name()} имеет меньше 50 HP. Оборотень трансформируется!')
            self.__transformed = True





class Weapon():
    def __init__(self, name,dmg):
        self.__name = name
        self.__dmg = dmg


class SilverSword(Weapon):
    def __init__(self, name = 'Серебряный меч'):
        super().__init__(name,30)

    def use(self,monster):
        print (f'Охотник наносит рассекающий удар оружием: {self.get_name()}')
        monster.take_damage(self.__dmg)


class HolyWater(Weapon):
    def __init__(self, name = 'Святая вода'):
        super().__init__(name,20)

    def use(self,monster):
        print (f'Охотник обливает врага: {self.__name}')
        monster.take_damage(self.__dmg)


class CrossbowBolt(Weapon):
    def __init__(self,name = 'Арбалет с болтом'):
        super().__init__(name,25)

    def use(self,monster):
        print (f'Охотник делает выстрел из: {self.__name}')
        monster.take_damage(self.__dmg)


weapons = [SilverSword(),HolyWater(),CrossbowBolt()]
zombie = Zombie('Зомби')
for w in weapons:
    w.use(zombie)
