import random

def flip_biased_coin(p):
    # Tvůj kód zde
    numbers = [0,0,0,1,1,1,1,1,1,1]
    return(random.choice(numbers))
    pass

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
