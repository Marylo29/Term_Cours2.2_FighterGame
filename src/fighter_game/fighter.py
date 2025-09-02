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

    def summary(self):
        """
        Retourne les caracteristiques du combattant.
        """
        return f"{self._name} : {self._description}\nHP : {self._healthPoints}\nAgility : {self._agility}\nStrenght : {self.get_strenght()}"
    
    def punch(self,a_fighter):
        """
        Coup de poing
        """
        hp = (1*self.get_strenght())-(1*a_fighter.get_agility())


marcel = Fighter('Marcel','The best one')
maurice = Fighter('Maurice','The second best one')