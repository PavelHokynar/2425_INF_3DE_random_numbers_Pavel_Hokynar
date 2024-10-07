import random

def generate_sequence(n):
    for _ in range(10):
        print(random.randint(1,n))
    pass

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
