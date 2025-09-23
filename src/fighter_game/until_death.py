from fighter import Fighter

def until_death(fighter_1,fighter_2):
    while fighter_1.is_alive() and fighter_2.is_alive():
        if fighter_1.get_weapon():
            fighter_1.shoot(fighter_2)
        else:
            fighter_1.punch(fighter_2)
        if not fighter_2.is_alive():
            break
        if fighter_2.get_weapon():
            fighter_2.shoot(fighter_1)
        else:
            fighter_2.punch(fighter_1)
    return (fighter_1 if fighter_1.is_alive() else fighter_2)

def until_death_rec(combattant,combattu):
    if combattant.get_weapon():
        combattant.shoot(combattu)
    else:
        combattant.punch(combattu)
    
    if combattu.is_alive():
        return until_death_rec(combattu,combattant)
    else:
        return combattant

marcel = Fighter('Marcel','The best one')
maurice = Fighter('Maurice','The second best one')
print(until_death(marcel,maurice))

jb = Fighter('Jean-Batiste',"Les Maths, c'est son domaine")
yves = Fighter('Yves',"L'informatique, c'est son domaine")
print(until_death_rec(yves,jb))