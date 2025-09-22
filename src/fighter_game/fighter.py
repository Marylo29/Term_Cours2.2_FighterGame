from random import randrange
class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._agility = randrange(1,10)
        self._healthPoints = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self._weapon = None

    def get_name(self):
        """
        Retourne le nom du combattant.
        """
        return self._name
    
    def get_description(self):
        """
        Retourne la description du combattant.
        """
        return self._description
    
    def get_agility(self):
        """
        Retourne l'agilité du combattant.
        """
        return self._agility
    
    def get_health(self):
        """
        Retourne les points de vie du combattant.
        """
        return self._healthPoints
    
    def get_strenght(self):
        """
        Retourne la force du combattant.
        """
        return 10 - self._agility

    def set_description(self, description):
        """
        Affecte la description du combattant.
        """
        self._description=description

    def _def_summary(self):
        """
        Retourne les caracteristiques du combattant.
        """
        return f"{self._name} : {self._description}\nHP : {self._healthPoints}\nAgility : {self._agility}\nStrenght : {self.get_strenght()}\nWeapon : {self.get_weapon()}"
    
    def summary(self):
        """
        Print les caracteristiques du combattant.
        """
        print(self._def_summary())

    def punch(self,a_fighter):
        """
        Coup de poing
        """
        lost_hp = (10*self.get_strenght())-(10*a_fighter.get_agility())
        a_fighter._healthPoints -= lost_hp if lost_hp > 0 else 0
        return a_fighter._healthPoints
    
    def set_weapon(self,a_weapon):
        self._weapon = a_weapon
        
    def get_weapon(self):
        return self._weapon
    
    def take_weapon(self,a_weapon):
        if not (a_weapon.get_owner() or self.get_weapon()):
            a_weapon.set_owner(self)
            self.set_weapon(a_weapon)
            return a_weapon
    
    def shoot(self,a_fighter):
        if self._weapon:
            return self._weapon.shoot(a_fighter)

    def __repr__(self):
        return self._def_summary()


class Weapon:
    def __init__(self,name,damage,ammos):
        self._name = name
        self._damage = damage
        self._ammos = ammos
        self._owner = None
    
    def set_owner(self,a_fighter):
        self._owner = a_fighter
        
    def get_owner(self):
        return self._owner
    
    def shoot(self,a_fighter):
        if self._ammos > 0:
            self._ammos -= 1
            a_fighter._healthPoints -= self._damage
        elif self._ammos == -1:
            a_fighter._healthPoints -= self._damage
        return a_fighter._healthPoints

marcel = Fighter('Marcel','The best one')
maurice = Fighter('Maurice','The second best one')
balle_de_baseball = Weapon('Balle de baseball',5,1)
batte_de_baseball = Weapon('Batte de baseball',10,-1)