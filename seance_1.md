Introduction à la programmation orientée objet
==============================================

Durant cette séance et les suivante nous allons developper une petite application
dans laquelle on aide à la confection de cadeaux avec des structures élémentaires disponibles
dans Python puis nous créerons nos propres structures.

aides mémoire en python
----------------------

https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf
https://s3.amazonaws.com/dq-blog-files/python-cheat-sheet-intermediate.pdf

Liens de reference
------------------

https://inforef.be/swi/download/apprendre_python3_5.pdf a partir de la page 50
https://inforef.be/swi/download/cours_python.zip Les fichiers source

https://automatetheboringstuff.com/ Se familiariser avec les chapitres 1 à 6

Correction de la premiere partie
--------------------------------

https://github.com/cgte/cours_iut/blob/master/seance_1_dict.py


Position du problème
--------------------

On souhaite modéliser l'emballage et la livraison de cadeau de Noël. il existe trois types de cadeaux:
- petit "small" prends 0.5 seconde à emballer et pese 1kg
- moyen "medium" prends 1 seconde à emballer et pese 2kg
- grand "large" prends 2 secondes à emballer et pese 5kg
Les cadeaux on un identifieur pour nous aider a suivre leur traitement

On souhaite ensuite mettre les cadeaux dans le traineau, le traineau
- ne peut 12kg de cadeaux au maximum
- met 0.5 seconde aller-retour par cadeau

Quand le traineau livre on n'emballe pas de cadeau.

À savoir
--------



Pour modeliser l'attente nous utiliserons la fonction time.sleep
`from time import sleep` ou bien `import time` puis `sleep(f)` où f est le nombre de secondes d'attente.

creation des identifieurs
```python
import random
import string
def make_identifier(k=4):
    return ''.join(random.choices(string.ascii_uppercase, k=4))
```


```python
def create_point(x, y):
    d = {'x': x, 'y': y, 'id': make_identifier()}
    return d

def wrap(aremplir):
    print("On emballe le cadeau ")

    sleep(quelquechose)
```

Questions
---------
Pour toutes les fonctions pensez à bien afficher ce qui est fait.

- Question 1: créer une fonction qui renvoie une dictionnaire avec les les clefs 'kind', 'duration' et 'weight' et 'identifier'
- Question 2: créer une fonction wrap\_gift qui attends le nombre de secondes
- Question 3: creer un dictionaire 'sledge' qui modelise un traîneau avec la charge maximale `max_load` les cadeaux contenus `gifts` et le temps pris par cadeau `time_per_gift`
- Question 4: les fonctions `compute_free_load` pour la charge encore disponible, `take_gift` pour mettre un cadeau dans le traineau et une fonction `ship` pour modéliser l'attente pendant la livraison.
- Question 5: une fonction `process_gifts`, qui prend en parametre une liste de dictionnaires crées avec create\_gift qui modélise le processus d'embalage et de livraison

tester le programme comme suit:
```python
if __name__ == '__main__':
    from random import choices
    gifts = choices(['small', 'medium', 'large'], k=15)
    gifts = [create_gift(gift) for gift in gifts]
    print(gifts)
    process_gifts(gifts)
```

Problématique
-------------

Nous utilisons uniquement des dictionnaires et des fonctions, nous obligés de nous souvenir de leurs structure et de quelles fonctions prennent quels types de dictionnaires. Afin de pouvoir organiser les concepts en ensembles cohérents il a été inventé la Programation orientée objet, nous allons creer des classes (les concepts) et des instances (les objets en question).

Pour creer une classe `Point` avec deux attributs `x` et `y`.

```python
def create_point(x,y):
    return {'x': x, 'y': y}


class Point:
    """ creates a simple point
    '''
    >>> #point = Point(0, 0)
    >>> #origine.x

    '''
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

```


Si on veut obtenir la distance à l'origine on ajoute la méthode `norme2` comme suit.

```python

class Point:
    """ Models simple points
    >>> p = Point(0,1)
    >>> p.x
    0
    >>> p.norm2()
    1

    def __init__(self, x, y): #Le constructeur
        self.x = x
        self.y = y
        # Notez bien que la fonction donne l'impression de ne rien renvoyer.

    def norm2(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def norm(self, n=2):
        return (abs(self.x) ** n + abs(self.y) ** n) ** (1/float(n))

```
plutôt que
``` python
def create_point(x,y):
    return {'x': x, 'y': y}

def norm_point(p):
    return (p['x']**2 + p['y'] **2) ** 0.5
```

`self` désigne l'object courant par convention (c'est le premier paramètre)

* Question 6.a : créez les classes Gift et Sledge, implémentez les methodes `__init__` pour les deux classes et la methode `wrap` pour gift.
* Quesiton 6.b : supprimez la methode create_gift et replacez la par Gift
* Question 6.c : relances le code et bugfixez

.


#Methodes et variables de classe
--------------------------------

Ce sont des méthodes qui ne s'appliquent pas a des instances mais qui prennent en paramète la classe, par exemple plutot que
```python
def create_point_from_input(input_string):
    #on imagine la saisie par un utilisateur exemple '2.3 3.2'
    x, y = input_string.split(' ')
    x,y = float(x), float(y)
    return Point(x, y)
```

On utilise ceci

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Notez bien que la fonction donne l'impression de ne rien renvoyer.

    @classmethod
    def fromstring(cls, string_):
        #on ajoute un tiret pour ne pas écraser le module 'string'
        #Par convention on utilise cls pour class
        x, y = [float(_) for _ in input_string.split(' ')]
        return cls(x,y)
```

Dans des cas plus complexes cela nous permet aussi de "proteger" le code pour le client, lui utilisera fromstring et non pas `__init__` et de lui fournir une fonction plus simple.

Les variables de classes sont des variables qui sont communes à toutes les instances.

Si on voulait utiliser la liste de point créés depuis le début on peut utiliser des variables de classe comme suit

```python
class Point:
    instances = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Notez bien que la fonction donne l'impression de ne rien renvoyer.
        self.__class__.instances.append(self)

    @classmethod
    def fromstring(cls, string_):
        #on ajoute un tiret pour ne pas écraser le module 'string'
        #Par convention on utilise cls pour class
        x, y = [float(_) for _ in input_string.split(' ')]
        return cls(x,y)
```


Attention cependant, Python nous donne une certaine souplesse avec les variables de classe.

```python
>>> class Point:
...     x = 0
...     def __init__(self, y):
...         self.y = y

>>> point01 = Point(1)
>>> point02 = Point(2)
>>> point01.x = 1
>>> point01.x
1
>>> point02.x
0
>>> point01.__class__.x
0

```

C'est une astuce qui peut etre très pratique mais de laquelle il faut se mefier.

- Question 7: Utilisez une méthode de classe pour fournir un interface plus simple pour creer des cadeaux.
- Question 8: Utilisez des variables de classe pour les caracteristiques du traineau là ou cela vous semble judicieux.
