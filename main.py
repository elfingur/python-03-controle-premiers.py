"""Module principal qui affiche les nombres premiers inférieurs à 100."""
from math import ceil

#### Fonction secondaire

def isprime(p):
    """Verifie si le paramètre est un boolean
Args : 
    p (int) : nombre a tester
Returns : 
    boolean : resultat du test """
    if p <= 1:
        return False
    for i in range(2, ceil(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale

def main():
    """Fonction principale qui affiche les nombres premiers de 0 à 99."""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
