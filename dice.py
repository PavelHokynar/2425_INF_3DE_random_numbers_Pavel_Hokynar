import random

def roll_die(k):
    # Tvůj kód zde
    numbers = [1,2,3,4,5,6]
    return(random.choice(numbers))
    pass

# Otestování funkce
print(roll_die(6))  # Simulace hodu 6-hranou kostkou
