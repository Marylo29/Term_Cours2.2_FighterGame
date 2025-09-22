from fighter import Fighter

def until_death(fighter_1,fighter_2):
    while fighter_1.get_health() > 0 and fighter_2.get_health() > 0 :
        fighter_1.punch(fighter_2)
        fighter_2.punch(fighter_1)
    return (fighter_1 if fighter_1.get_health() > 0 else fighter_2)

marcel = Fighter('Marcel','The best one')
maurice = Fighter('Maurice','The second best one')
print(marcel.summary())
print(maurice.summary())
print(until_death(marcel,maurice))