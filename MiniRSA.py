import random
import math as maths

'''
Puissance modulaire
'''
def puissance(a, e, n):
    p = 1
    while e > 0:
        if e % 2 != 0:
            p = (p * a) % n
        a = (a * a) % n
        e = e // 2
    return p

'''
Convertir un texte en un nombre et vice versa
'''
def str_to_int(text):
    s=0
    b=1
    for i in range(len(text)):
        s+=ord(text[i])*b
        b*=256
    return s

def int_to_str(c):
    s=""
    q,r =divmod(c,256)
    s+=chr(r)
    while q!=0:
        q,r =divmod(q,256)
        s+=chr(r)
    return s

'''
Calcul du PGCD de deux nombres
'''
def pgcd(u, v):
    while v != 0:
        u, v = v, u % v
    return u

'''
Calcul de l'inverse modulaire via l'algorithme d'Euclide étendu
'''
def bezout(a, b):
    a0 = a
    b0 = b

    p = 1
    q = 0
    r = 0
    s = 1

    c = 0
    quotient = None
    nouveau_r = None
    nouveau_s = None

    while b != 0:
        c = a % b
        quotient = a // b
        a = b
        b = c
        nouveau_r = p - quotient * r
        nouveau_s = q - quotient * s
        p = r
        q = s
        r = nouveau_r
        s = nouveau_s
    return p

'''
Premier pour voir si un nombre est premier (peu efficace)
'''
def test_premier(n):
    j = 0
    for i in range(1, n + 1):
        if n % i == 0:
            j = j + 1

    return j == 2

'''
Second test pour voir si un nombre est premier (plus efficace)
'''
def second_test_premier(n):
    if (
        puissance(2, n - 1, n) == 1
        and puissance(3, n - 1, n) == 1
        and puissance(5, n - 1, n) == 1
        and puissance(7, n - 1, n) == 1
        and puissance(11, n - 1, n) == 1
        and puissance(13, n - 1, n)
    ):
        return True
    return False

'''
Génération de la clé RSA publique et privée
'''
def gen_RSA_key():
    p = random.randint(2, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    q = random.randint(2, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    n = 0
    phi = 0
    d = 0

    while not second_test_premier(p):
        p = random.randint(2, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    while not second_test_premier(q):
        q = random.randint(2, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while pgcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = bezout(e, phi)
    if d < 0:
        d = d + phi
    assert(e*d % phi == 1)
    return (n, e, d)

'''
Chiffrement/Déchiffrement d'un nombre avec la puissance modulaire en utilisant la clé publique ou privée
'''
def chifferNombre(nb, e, n):
    return puissance(nb, e, n)


'''
Chiffrement/Déchiffrement d'un texte avec la puissance modulaire en utilisant la clé publique ou privée
'''
def chiffrer_texte(texte, e, n):
    textNumber = str_to_int(texte)
    text_chiffre = ""
    text_chiffre = puissance(textNumber, e, n)
    text_chiffre = int_to_str(text_chiffre)
    return text_chiffre


#Génération des clés RSA
key = gen_RSA_key()
key_pub = (key[1], key[0])
key_priv = key[2]

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."
assert(str_to_int(text) < key_pub[1])
assert(int_to_str(str_to_int("hello")) == "hello")

print(f"texte : {text}")
textChiffre = chiffrer_texte(text, key_pub[0], key_pub[1])
print(f"texte Chiffré : {textChiffre}")
textDechiffre = chiffrer_texte(textChiffre, key[2], key[0])
print(f"texte Déchiffré : {textDechiffre}")
