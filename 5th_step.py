import random

#--------------------------------------------------------------------------

class Monster:
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

#--------------------------------------------------------------------------

class Zombie(Monster):
    def __init__(self, name = 'Зомби'):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print (f'{self.get_name()} теряет конечность! Получено {damage} урона. HP: {self.get_hp()}')


class Vampire(Monster):
    def __init__(self, name = 'Вампир'):
        super().__init__(name,80,15)

    def take_damage(self, damage):
        feature = max (0, damage - 5)
        self.set_hp(self.get_hp() - feature)
        print (f'{self.get_name()} поглащает 5 урона! Получено {feature} урона. HP: {self.get_hp()}')


class Ghost(Monster):
    def __init__(self, name = 'Призрак'):
        super().__init__(name,60,20)

    def take_damage(self, damage):
        if random.random() < 0.3:
            print (f'{self.get_name()} уклонился от удара! Не прошло {damage} урона. HP: {self.get_hp()}')
        else:
            self.set_hp(self.get_hp() - damage)
            print (f'{self.get_name()} пропустил двоечку! Получено {damage} урона. HP: {self.get_hp()}')


class Werewolf(Monster):
    def __init__(self, name = 'Оборотень'):
        super().__init__(name,100,25)
        self.__transformed = False

    def take_damage(self,damage):
        self.set_hp(self.get_hp() - damage)
        print (f'{self.get_name()} получает в пасть! Получено {damage} урона. HP: {self.get_hp()}')
        if self.__hp < 50 and self.__transformed == False:
            print (f'{self.get_name()} имеет меньше 50 HP. Оборотень трансформируется!')
            self.__transformed = True

#--------------------------------------------------------------------------

class Weapon:
    def __init__(self, name):
        self.name = name

    def use(self, monster):
        pass


class SilverSword(Weapon):
    def __init__(self):
        super().__init__('Скалка')
        self.dmg = 20

    def use(self, monster):
        print(f"Охотник наносит удар: {self.name}! На {self.dmg} урона")
        monster.take_damage(self.dmg)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__('Куринный бульон')
        self.dmg = 30

    def use(self, monster):
        print(f"Охотник обливает монстра: {self.name}! На {self.dmg} урона")
        monster.take_damage(self.dmg)


class CrossbowBolt(Weapon):
    def __init__(self):
        super().__init__('АК-47')
        self.dmg = 25

    def use(self, monster):
        print(f"Охотник стреляет из: {self.name}! На {self.dmg} урона")
        monster.take_damage(self.dmg)

#--------------------------------------------------------------------------

class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def add_weapon(self,weapon):
        self.__weapons.append(weapon)

    def get_weapon_count(self):
        return len(self.__weapons)

    def show_inventory(self):
        print(f'Инвентарь {self.__name}:')
        count = 1
        for weapon in self.__weapons:
            print(f'{count}. {weapon.name}')
            count += 1

    def get_attack(self,weapon_index,monster):
        if 0 <= weapon_index < len(self.__weapons):
            self.__weapons[weapon_index].use(monster)
        else:
            print('Неверный индекс оружия.')

    def is_alive(self):
        return True if self.__hp > 0 else False

#--------------------------------------------------------------------------

def run_game():
    hunter = Hunter('Зинаида Федоровна')
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(CrossbowBolt())
    hunter.show_inventory()
    print(f'Количество оружия: {hunter.get_weapon_count()}')
    print('')

    zombie = Zombie('Зомби')
    hunter.get_attack(0, zombie)
    hunter.get_attack(1, zombie)
    hunter.get_attack(2, zombie)
    print('')

    monsters = [
        Zombie('Зомби'),
        Vampire('Вампир'),
        Ghost('Призрак'),
        Werewolf('Оборотень'),
    ]

    print(f'{hunter.get_name()} залетает в замок! Её встречает {len(monsters)} монстра.')
    print('*' * 60)
    print('')

    for monster in monsters:
        print('')
        print(f'Появляется {monster.get_name()}!')
        turn = 0

        while monster.is_alive() and hunter.is_alive():
            weapon_index = turn % hunter.get_weapon_count()
            hunter.get_attack(weapon_index, monster)

            if not monster.is_alive():
                print(f'{monster.get_name()} повержен!')
                break

            monster.attack_hunter(hunter)
            print(f'{monster.get_name()} атакует {hunter.get_name()}! Нанесено {monster.get_dmg()}')
            print(f'{hunter.get_name()}: {hunter.get_hp()} HP')

            if not hunter.is_alive():
                print(f'{hunter.get_name()} ушла в поликлиннику! Бой окончен')
                break

            turn += 1
            print('')

        print('=' * 50)
        if hunter.is_alive():
            print('Победа! Замок очищен от нечистой силы.')
        else:
            print('ПоРаЖеНиЕ! Жители замка оказались сильнее.')


run_game()
