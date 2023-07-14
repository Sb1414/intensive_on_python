import random

def turrets_generator():
    # случайные значения для каждой черты личности
    neuroticism = random.randint(0, 100)
    openness = random.randint(0, 100)
    conscientiousness = random.randint(0, 100)
    extraversion = random.randint(0, 100)
    agreeableness = random.randint(0, 100)

    # сумма всех черт личности была равна 100
    total = neuroticism + openness + conscientiousness + extraversion + agreeableness
    scaling_factor = 100 / total
    neuroticism = int(neuroticism * scaling_factor)
    openness = int(openness * scaling_factor)
    conscientiousness = int(conscientiousness * scaling_factor)
    extraversion = int(extraversion * scaling_factor)
    agreeableness = 100 - (neuroticism + openness + conscientiousness + extraversion)

    # динамические методы
    turret_class = type('Turret', (object,), {
        'shoot': lambda self: print('shoot'),
        'search': lambda self: print('search'),
        'talk': lambda self: print('talk'),
    })

    turret_instance = turret_class()

    # динамические атрибуты для черт личности
    turret_instance.neuroticism = neuroticism
    turret_instance.openness = openness
    turret_instance.conscientiousness = conscientiousness
    turret_instance.extraversion = extraversion
    turret_instance.agreeableness = agreeableness

    return turret_instance

if __name__ == '__main__':
    turret = turrets_generator()
    turret.shoot()
    turret.search()
    turret.talk()
    print('neuroticism:', turret.neuroticism)
    print('openness:', turret.openness)
    print('conscientiousness:', turret.conscientiousness)
    print('extraversion:', turret.extraversion)
    print('agreeableness:', turret.agreeableness)
    print('sum:', turret.neuroticism + turret.openness + turret.conscientiousness +
          turret.extraversion + turret.agreeableness)
