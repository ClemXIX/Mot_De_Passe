import random

"""
Génère un mot de passe aléatoire, de base entre 9 et 13, minimun 1 majuscule, 1 symbole spécial, 1 chiffre
avec la possibilité de : 
- retirer les carac spéciaux 
- retirer les chiffres 
- tout en minuscule 
- tout en majuscule
- que des chiffres 
 
 Mais chose importante, il n'y a pas de 0 ou de o, ni de 1, ni de l
 Pour éviter les fameux 'Mais c'est un l ou un un' 
 """


# Les ingrédients pour le mélange

lettres_minus = "abcdefghjkmnpqrstxyz"
lettres_majus = "ABCDEFGHJKMNPQRSTXYZ"
chiffres = "23456789"
symbol = ["!","@","_",'#']

mdp: str = ""  # mot de passe


def mdp_complet(mdp):

    # UN complet, salades tomates oignons sauce andalouse

    lettre_m = random.choices(([i for i in lettres_minus]), k=random.randrange(3, 5))
    lettre_M = random.choices(([i for i in lettres_majus]), k=random.randrange(3, 5))
    lettre_C = random.choices(([i for i in chiffres]), k=random.randrange(2, 4))
    lettre_S = random.choices(([i for i in symbol]), k=random.randrange(1, 3))

    mdp = lettre_m + lettre_M + lettre_C + lettre_S
    mdp = random.sample(mdp, len(mdp))
    mdp = ''.join(mdp)

    return mdp



def mdp_sans_symbole_avec_chiffres(mdp):

    # Alors comme ça on n'aime pas les oignons ?!

    lettre_m = random.choices(([i for i in lettres_minus]), k=random.randrange(4, 6))
    lettre_M = random.choices(([i for i in lettres_majus]), k=random.randrange(4, 6))
    lettre_C = random.choices(([i for i in chiffres]), k=random.randrange(1, 3))

    mdp = lettre_m + lettre_M + lettre_C
    mdp = random.sample(mdp, len(mdp))
    mdp = ''.join(mdp)

    return mdp


def mdp_sans_chiffres_avec_symbol(mdp):

    # Un complet sans sauce !

    lettre_m = random.choices(([i for i in lettres_minus]), k=random.randrange(4, 6))
    lettre_M = random.choices(([i for i in lettres_majus]), k=random.randrange(4, 6))
    lettre_S = random.choices(([i for i in symbol]), k=random.randrange(1, 3))

    mdp = lettre_m + lettre_M + lettre_S
    mdp = random.sample(mdp, len(mdp))
    mdp = ''.join(mdp)

    return mdp


def mdp_lettres(mdp):

    # Que des légumes en accompagnement ?

    lettre_m = random.choices(([i for i in lettres_minus]), k=random.randrange(5, 7))
    lettre_M = random.choices(([i for i in lettres_majus]), k=random.randrange(5, 7))

    mdp = lettre_m + lettre_M
    mdp = random.sample(mdp, len(mdp))
    mdp = ''.join(mdp)

    return mdp


def mdp_chiffres(mdp):

    # Que de la sauce ????

    mdp = "".join(random.choices(([i for i in chiffres]), k=random.randint(8,8)))

    return mdp

def mdp_minus(mdp):

    # Salade friendly, une tortue ?

    mdp = "".join(random.choices(([i for i in lettres_minus]), k=random.randint(8,12)))

    return mdp

def mdp_majus(mdp):

    # Que des tomates, un merle ?

    mdp = "".join(random.choices(([i for i in lettres_majus]), k=random.randint(8, 12)))

    return mdp

if __name__ == "__main__":
    print(mdp_complet(mdp))
