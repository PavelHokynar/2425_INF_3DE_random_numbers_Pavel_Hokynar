import random

def roll_die(k):
    # Tvůj kód zde
    return(random.randint(1,k))
    pass

# Otestování funkce
print(roll_die(6))  # Simulace hodu 6-hranou kostkou
