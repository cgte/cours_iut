Seance2
=======

Maintenant que nous avons des classes, nous alons voir quelques spécificités du langage Python.

Chronométrage de la fonction process\_gifts
-------------------------------------------

Nous aimerions compter le temps pris par la fonction process\_gifts


```python
from time import time, sleep
t_debut = time()
sleep(0,1) #Une fontion qui prend du temps
t_fin = time()
delta= t_fin - t_debut
print(f"Le sommeil a duré {delta} secondes")

```

La première méthode consiste integrer le code dans la fonction :
```python
>>> from time import time, sleep
>>> def timed_process_gifts(gifts):
...     t0 = time()
...     # du code ....
...     sleep(0.1)
...     t1 = time()
...     print(f"la fonction a pris {t1 - t0:.2f} secondes")
>>> timed_process_gifts([])
la fonction a pris 0.10 secondes

```

Cette approche n'est pas satifaisante pour plusieurs raisons.
- On doit creer une nouvelle fonction et modifier le code partout ou celle ci est appelée.
- On ajoute du code qui n'a pas d'interet fonctionnel dans une fonction, ceci pollue le code et rend sa lecture difficile.

Ce que nous aimerions c'est pouvoir modifier la fonction pour que celle ci soit
chronometrée sans changer le code à l'interieur de la fonction.
Dans les fait cela avoir une nouvelle fonction qui "contient" l'ancienne mais étoffée d'un chronometrage.
Ce procédé s'appelle *décorer* un objet (en python tout est objet, y compris les fonction)

Voyons quelques approches

```python
>>> def ma_fonction(*args):
...     sleep(0.2)
...
>>> def timed_mafonction(*args):
...     t_debut = time()
...     res = ma_fonction(*args)
...     t_fin = time()
...     print(f"Temps pris par {ma_fonction.__name__} {t_fin - t_debut:.2f}")
...     return res
...
>>> timed_mafonction()
Temps pris par ma_fonction 0.20
>>> def time_wrapper(function):
...     def fonction_chrono(*args, **kwargs):
...         t_debut = time()
...         res = function(*args, **kwargs)
...         t_fin  = time()
...         print(f"Temps pris par {function.__name__} {t_fin - t_debut:.2f}")
...         return res
...
...     return fonction_chrono
...
>>> def toto():
...     sleep(0.1)
...
>>> toto = time_wrapper(toto)
>>> toto.__name__
'fonction_chrono'
>>> toto()
Temps pris par toto 0.10
>>> @time_wrapper
... def autre_fonction():
...     sleep(0.1)
...     print("Autre fonction")
...
>>> autre_fonction()
Autre fonction
Temps pris par autre_fonction 0.10

```

Méthodes speciales et property
------------------------------

Observons les méthodes compute\_free\_load et load, ces methodes effectuent un calcul mais ne font
rien de particulier, Python nous permet de manipuler ces fonctions comme si elles etaient des attributs
de l'instance grâce au décorateur *property*


```python

>>> class A:
...     def __init__(self, a: int):
...         self.a = a
...
...     def carre(self):
...         return self.a ** 2
...
...     @property
...     def cube(self):
...         return self.a ** 3
...
>>> a = A(2)
>>> a.carre()
4
>>> a.cube
8

```

Utilisez le decorateur property pour les méthodes qui ne font que des calculs (load et free_load)
de Sledge.

TODO: Parler un peu plus des properties

Méthodes spéciales:
__str__, __repr__, __len__, __iter__, __getitem__


```python
>>> print(a)
<__main__.A object at ...>

```

Ce qui n'est pas d'une grande aide pour le lecteur

```python
>>> def printa(a):
...     return str(a.a)
...
>>> A.__str__ = printa
>>> print(a)
2

```
Est deja plus pratique


implementez la methode __str__ pour gift et sledge

Nous voyons que la classe Sledge represente en fait une liste de Gift et aimerions pouvoir faire
les memes operations qu'avec une liste par exemple pouvoir écrire `for gift in sledge` plutot que
`for gift in sledge.gifts` de la meme façon utiliser `len(sledge)`

la fonction __iter__ renvoie pour le moment self.gift

implementez les methodes __len__, __iter__ et __getitem__ et __contains__ pour Sledge.

Réecrire le corps de la fonction `process_gifts` pout utiliser if sledge et if gift in sledge

Quelle autres fonctions pourriez vous implementer (https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/)


Generateurs
-----------

Ajoutons un temps d'attente d'une seconde lors de la cration d'un cadeau, que se passe-t-il ?

Pour palier à ce problème nous allons modifier un peu notre code en utiliseant le mot clef yield

``` python
>>> def simple_gen():
...     yield 1
...     yield 2
...     yield 3
...
>>> list(x for x in simple_gen())
[1, 2, 3]
```

Effectons une verification de convergence:

```python

# coding: utf-8
from time import sleep
from random import randint
def gen():
    for i in range(100):
        sleep(0.3)
        yield randint(0, 100)

def moyenneur(args):
    somme = 0.0
    for i, v in enumerate(args, start=1):
        somme += v
        moyenne = somme / i
        print(f"apres {i} elements la moyenne est de {moyenne:.2f}")
    return moyenne

moyenneur(x for x in gen())
```

Nous voyons qu'il es tpossible d'effectuer des calculs sans que toutes les données n'aient été calculées
au prealable. Ceci est tres pratique quand le volume de donnée commence a croître et qu'il ne devient
plus forcément posible ou souhaitable de tout charger en mémoire.

Utilisez la methode yield pour pouvoir commencer a livrer dans cadeaux avant d'attendre qu'ils ne soient tous
fabriqués.

