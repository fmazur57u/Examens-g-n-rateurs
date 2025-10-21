## 1. Générateur de suite simple


def compter(start, end):
    for nombre in range(start, end + 1):
        yield nombre


gen = compter(1, 10)
for nombre in gen:
    print(nombre, end=" ")

print("")


## 2. Générateur filtrant
def nombres_pairs(iterable):
    for nombre in iterable:
        if nombre % 2 == 0:
            yield nombre


gen = nombres_pairs(range(1, 11))
for nombre in gen:
    print(nombre, end=" ")
print("")

## 3. Générateur infini avec pause


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()

for _ in range(10):
    print(next(gen), end=" ")

## 4. Générateur de puissances

print("")


def générateur_puissance(n):
    for number in range(n + 1):
        yield number**2


gen = générateur_puissance(10)
for nombre in gen:
    print(nombre, end=" ")
print("")

## 5. Utiliser next() pour afficher les lignes d'un texte une par une


def reader(texte):
    for ligne in texte.strip().split("\n"):
        yield ligne


texte = """
Il faut, autant qu'on peut, obliger tout le monde :
On a souvent besoin d'un plus petit que soi.
De cette vérité deux fables feront foi,
Tant la chose en preuves abonde.
Entre les pattes d'un Lion,
Un Rat sortit de terre assez à l'étourdie.
Le Roi des animaux, en cette occasion,
Montra ce qu'il était, et lui donna la vie.
Ce bienfait ne fut pas perdu.
Quelqu'un aurait-il jamais cru
Qu'un Lion d'un Rat eût affaire (1)?
Cependant il avint(2)qu'au sortir des forêts
Ce Lion fut pris dans des rets (3),
Dont ses rugissements ne le purent défaire.
Sire Rat accourut, et fit tant par ses dents
Qu'une maille rongée emporta tout l'ouvrage.
Patience et longueur de temps
Font plus que force ni que rage.
"""

gen = reader(texte.strip())
texte = texte.strip()
for _ in range(len(texte.strip().split("\n"))):
    print(next(gen))
