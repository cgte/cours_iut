# coding: utf-8

# On admet ce code
class Conteneur:
    pass


# on crée un objet qui peut contenir n'importe quoi

gg = Conteneur()

gg.entier = 1
print(gg.entier)

gg.liste = [1, 2, 3, 4]
gg.autreliste = [None, "bonjour"]

gg.a = "a1"


def make_point(conteneur, x, y):
    setattr(conteneur, "x", x)
    conteneur.y = y
    return conteneur


gg = make_point(gg, 1, 2)
print(gg)
print(gg.x)
print(gg.y)


def make_point_2(conteneur, x, y):
    conteneur.x = x
    conteneur.y = y


point = Conteneur()
make_point_2(point, 3, 4)
point.x
Conteneur.__init__ = make_point_2
nouveau_point = Conteneur(5, 6)
nouveau_point.x


def stringify_point(point):
    return f"({point.x},{point.y})"


print(stringify_point(nouveau_point))
Conteneur.__str__ = stringify_point
print(nouveau_point)
