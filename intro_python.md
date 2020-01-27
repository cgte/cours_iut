Introduction à Python
=====================

- À regarder : https://www.youtube.com/watch?v=OSGv2VnC0go Attention c'est en python2
- À garder sous la main : https://docs.python.org/3/reference/datamodel.html


Types de données fondamentales en python.
=========================================

int, float et string
``` python
>>> i = 9
>>> chaine = 'Bonjour'
>>> len(chaine)
7
>>> flottant = 8.65
>>> i
9

```

Nous voyons donc quelques types dits "primitifs" et nous pouvons les utiliser dans des fonctions.
Dans le module str nous avons une fonction swapcase

``` python
>>> str.swapcase(chaine)
'bONJOUR'
>>> str.zfill(chaine, 10)
'000Bonjour'
>>> chaine + ' !'
'Bonjour !'

```

Listes, ensembles, dictionnaires.


``` python

>>> maliste = [1,1,2,3,5,4,7]
>>> maliste[::-1]
[7, 4, 5, 3, 2, 1, 1]
>>> maliste[3]
3
>>> maliste[-3]
5
>>> uniques = set(maliste)
>>> uniques
{1, 2, 3, 4, 5, 7}

>>> mondict = {'un': 1, 'deux': 2, 'trois': 3, 3:'trois'}
>>> mondict[3]
'trois'
>>> mondict['un']
1

```

Fonctions
=========

Un fonction est un ensemble d'instructions cohérentes qui effectuent un travail donné

`len` est une fonction qui est directement disponible, `dir` est une autre fonction, `print` aussi est une fonction.

Nous pouvons aussi définir des fonctions avec le mot clef `def`.

``` python
>>> def fonction_1():
...     "Renvoie toujours 1"
...     return 1
...
>>> print(fonction_1())
1
>>> def ajoute_2(nombre):
...     resultat =  nombre + 2
...     return resultat
...
>>> ajoute_2(3)
5
>>> def creer_un_dictionaire(clefs, valeurs):
...     """On remplit un dictionnaire avec les clefs et valeurs qui correspondent
...     """
...     res = {}
...     if len(clefs) != len(valeurs):
...         return None # Early return autorisé en python
...     for i in range(len(clefs)):
...         res[clefs[i]] = valeurs[i]
...     return res
...
>>> creer_un_dictionaire(['a', 'b'], [1,5])
{'a': 1, 'b': 5}
>>> def remplir_un_dictionnaire(dictionaire, clefs, valeurs):
...     if len(clefs) != len(valeurs):
...         return # Early return autorisé en python
...     for i in range(len(clefs)):
...         dictionaire[clefs[i]] = valeurs[i]
...
>>> vide = {}
>>> remplir_un_dictionnaire(vide, ['a', 'b'], [1,5])
>>> vide
{'a': 1, 'b': 5}

```

[exemple_poo.py]exemple_poo.py



Notion de classe et de type
===========================

``` python
>>> try:
...     str.swapcase(6) #Essayer directement le code suivant, nous verrons les exceptions plus tard
... except Exception as e:
...     print(e)
...
descriptor 'swapcase' requires a 'str' object but received a 'int'

```

On ne peut pas utiliser swapcase sur un entier, cela n'a pas vraiment de sens d'ailleurs.
Nous aimerions pouvoir utiliser la fonction sans forcément aller rechercher dans le module.

```
Dans ipython :
In [10]: str.swapcase??
Signature: str.swapcase(self, /)
Docstring: Convert uppercase characters to lowercase and lowercase characters to uppercase.
Type:      method_descriptor

```

``` python
>>> chaine.swapcase()
'bONJOUR'

```

Cette fonction ne semble pas prendre de paramètre, en fait python l'appelle implicitement avec
self.
``` python
>>> str.swapcase
<method 'swapcase' of 'str' objects>
>>> chaine.swapcase
<built-in method swapcase of str object at 0x...>

```

Quand on crée une chaine de caractères Python sait où aller chercher les methodes utiles et permet
d'y acceder directement. Dit rapidement: il a un mécanisme pour pouvoir trouver la méthode qui
convient, simplement avec la variable et quelques information.

Un exemple avec des chiffres:

``` python
>>> flottant = 6.0
>>> entier = 6
>>> flottant.real
6.0
>>> flottant.imag
0.0
>>> entier.real
6
>>> entier.imag
0

```

Ici plutot que d'appeler  `float.real(flottant)` et `int.real(entier)` on laisse aux developpeurs
du module la responsabilié d'appeler la bonne fonction.
Ce qui nous permet d'écrire par exemple le code suivant:


``` python
>>> [x.real for x in [entier, flottant]]
[6, 6.0]

```


Acceder à aux methodes disponibles pour une variable
``` python
>>> dir(chaine)
['__add__', '__class__', ..., 'swapcase', ..., 'zfill']
>>> chaine.zfill(10)
'000Bonjour'
>>> chaine.__add__(' !')
'Bonjour !'

```

En réalité tout est objet en python et le langage dispose de beaucoup de capacité d'introspection.


Position du probleme des cadeaux et du traineau

``` python
>>> def create_gift(kind):
...     types_acceptes =  ['s', 'm', 'l']
...     if kind in types_acceptes:
...         return {'kind': kind, 'duree': ord(kind) / 100.0}
...     else:
...         print(f"{kind:s} n'est pas un type valide")
...         return

```


La fonction ord renvoie un entier.
``` python
>>> petit_cadeau = create_gift('s')
>>> petit_cadeau
{'kind': 's', 'duree': 1.15}
>>> create_gift('x')
x n'est pas un type valide
>>> traineau = {'nom': 'premier_traineau', 'cadeaux': []}
>>> traineau['cadeaux'].append(petit_cadeau)
>>> traineau
{'nom': 'premier_traineau', 'cadeaux': [{'kind': 's', 'duree': 1.15}]}

```
Listes en compréhension

``` python

>>> gifts = [create_gift(kind) for kind in ['s', 's', 'm', 'l']]
>>> gifts
[{'kind': 's', 'duree': 1.15}, {'kind': 's', 'duree': 1.15}, {'kind': 'm', 'duree': 1.09}, {'kind': 'l', 'duree': 1.08}]


```
Dictionnaires en compréhension

``` python

>>> letter_count = {word: len(word) for word in 'bonjour hola hello'.split()}
>>> letter_count
{'bonjour': 7, 'hola': 4, 'hello': 5}

```


On crée ainsi des cadeaux que l'on peut placer dans le traineau

``` python
>>> for gift in gifts:
...     traineau['cadeaux'].append(gift)
...
>>> from pprint import pprint
>>> pprint(traineau)
{'cadeaux': [{'duree': 1.15, 'kind': 's'},
             {'duree': 1.15, 'kind': 's'},
             {'duree': 1.15, 'kind': 's'},
             {'duree': 1.09, 'kind': 'm'},
             {'duree': 1.08, 'kind': 'l'}],
 'nom': 'premier_traineau'}
>>> len(traineau['cadeaux'])
5
>>> def take_gift(letraineau, cadeau):
...     letraineau['cadeaux'].append(cadeau)

>>> take_gift(traineau, create_gift('m'))
>>> len(traineau['cadeaux'])
6

```






Sucres syntaxiques et réutilisaiton du code
===========================================

Nous aimerions pouvoir ecrire la chose suivante:
``` python
>>> try:
...    traineau += gift
... except TypeError as e:
...     print(e)
unsupported operand type(s) for +=: 'dict' and 'dict'

```

Quelques constats:
  - On peut facilement prototyper avec les dictionnaires, par contre il
    faut bien connaitre les fonctions
  - Cela rend le code difficilement utilisable par quelqu'un d'autre
    (il doit connaitre notre implémentation pour utiliser les outils)

Un premier exemple une ligne de points. Pour le moment on crée un point en 2D
avec les coordonnées x et y. Nous allons utiliser des dictionnaires, des namedtuple
et enfin creer notre propre classe

``` python
>>> def create_point2D(x, y):
...     return {'x': x, 'y': y}
>>> courbe_carre = []
>>> for x in range(10):
...     courbe_carre.append(create_point2D(x, x**2))
>>> courbe_cube = [create_point2D(x=x, y=x**3) for x in range(-10, 11)]
>>> pprint(courbe_carre)
[{'x': 0, 'y': 0},
 {'x': 1, 'y': 1},
 {'x': 2, 'y': 4},
 {'x': 3, 'y': 9},
 {'x': 4, 'y': 16},
 {'x': 5, 'y': 25},
 {'x': 6, 'y': 36},
 {'x': 7, 'y': 49},
 {'x': 8, 'y': 64},
 {'x': 9, 'y': 81}]

```

namedtuple crée des objets qui nous permettent facilement d'acceder à leurs attributs,
par contre on ne peut changer ceux-ci.

``` python
>>> from collections import namedtuple
>>> Point_NT = namedtuple('Point2D', 'x y')
>>> p = Point_NT(1 ,3)
>>> p.x, p.y
(1, 3)
>>> p
Point2D(x=1, y=3)
>>> Point_NT(x=1,y=4)
Point2D(x=1, y=4)

```

Quelques manipulations des arguments
``` python
>>> coords = [1, 5]
>>> Point_NT(*coords)
Point2D(x=1, y=5)
>>> params = {'x':0, 'y':42}
>>> Point_NT(**params)
Point2D(x=0, y=42)

```

Imaginons que nous voulions construre un point a partir d'une chaine de caractères
``` python

>>> Point_NT(*'1,3'.split(','))
Point2D(x='1', y='3')

```

Maintenant nous avons des points dont les coordonnées sont des chaines de caractères.
``` python

>>> Point_NT(*[float(x) for x in '1,3'.split(',')])
Point2D(x=1.0, y=3.0)

```

En faisant attention on arrive à comprendre mais cela n'est pas tres lisible.
Nous allons créer notre propre type d'objets point, ce que l'on appelle une classe.
Dans cette classe nous mettrons les fonctions utiles, comme si c'etait dans un module à part.

``` python

>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme attributs'''
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y # Un exemple d'affectation
...
>>> notre_point = Point2D(1,3)
>>> notre_point.x, notre_point.y
(1, 3)

```

Nous avons bien la meme chose qu'avec namedtuple mais

``` python
>>> notre_point
<__main__.Point2D object at 0x...>
>>> print(notre_point)
<__main__.Point2D object at 0x...>

```

Ce qui ne nous donne pas grande information
``` python
>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x, y):
...         self.x, self.y = x, y # Un exemple d'affectation
...
...     def __str__(self):
...         return f"Point2D:{{'x': {self.x}, 'y': {self.y}}}"
>>> notre_point = Point2D(1,3)
>>> print(notre_point)
Point2D:{'x': 1, 'y': 3}

```

Automatiquement python est allé appeler la methode __str__

Ajoutons deux fonctionalités : la norme du point et la translation
``` python
>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x, y):
...         self.x, self.y = x, y # Un exemple d'affectation
...
...     def __str__(self):
...         return f"Point2D:{{'x': {self.x}, 'y': {self.y}}}"
...
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...     def translation(self, x, y):
...         self.x += x
...         self.y += y
>>> notre_point = Point2D(3,4)
>>> notre_point.norm()
5.0
>>> notre_point.translation(1,2)
>>> print(notre_point)
Point2D:{'x': 4, 'y': 6}

```

On ne passe pas self, c'est l'interpreteur qui sait quoi mettre dedans.
Nous aimerions pouvoir créer des points a partir d'une chaine de caractères.
Une premiere approche pourait etre de creer un point a l'origine puis d'appeler
une méthode sur une chain  de caractères

``` python
>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x=None, y=None):
...         self.x, self.y = x, y # Un exemple d'affectation
...
...     def from_string(self, string_, sep=','):
...         coords = [float(coord) for coord in string_.split(sep)]
...         self.x, self.y = coords
...
...     def __str__(self):
...         return f"Point2D:{{'x': {self.x}, 'y': {self.y}}}"
...
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...     def translation(self, x, y):
...         self.x += x
...         self.y += y
>>> point = Point2D() #Car on a des parametres par defaut
>>> point.from_string('1,3')
>>> print(point)
Point2D:{'x': 1.0, 'y': 3.0}

```

Cela fonctionne mais cela pose quelques questions:
  - On peut desormais creeer des points sans pour autant etre sur de pouvoir les utiliser.
  - On risque de traiter le cas de l'origine comme cas spécial (en remplaçant None par 0)
  - La convertion d'une chainde de caractère dépend de la classe Point2D mais pas d'un point en partculier.

On utilise pour ça `@classmethod`

``` Python
>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x=None, y=None):
...         self.x, self.y = x, y
...
...     @classmethod
...     def fromstring(cls, string_, sep=','):
...         coords = [float(coord) for coord in string_.split(sep)]
...         return cls(*coords)
...
...     def __str__(self):
...         return f"Point2D:{{'x': {self.x}, 'y': {self.y}}}"
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...     def translation(self, x, y):
...         self.x += x
...         self.y += y
...     __repr__ = __str__
>>> dix_dix = Point2D.fromstring('10,10')
>>> dix_dix
Point2D:{'x': 10.0, 'y': 10.0}

```

Desormais nous aimerions identifier nos points, pour ne pas les compter deux fois.
Nous allons utiliser un compteur au niveau de la classe

``` python
>>> class Point2D:
...     compteur = 0
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x=None, y=None):
...         self.x, self.y = x, y
...         self.identifiant = self.__class__.compteur
...         self.__class__.compteur += 1
...     @classmethod
...     def fromstring(cls, string_, sep=','):
...         coords = [float(coord) for coord in string_.split(sep)]
...         return cls(*coords)
...
...     def __str__(self):
...         return f"Point2D:{{'x': {self.x}, 'y': {self.y}}} identifiant: {self.identifiant}"
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...     def translation(self, x, y):
...         self.x += x
...         self.y += y
...     __repr__ = __str__
>>> dix_dix = Point2D.fromstring('10,10')
>>> dix_onze = Point2D.fromstring('10,11')
>>> dix_onze
Point2D:{'x': 10.0, 'y': 11.0} identifiant: 1
>>> dix_dix
Point2D:{'x': 10.0, 'y': 10.0} identifiant: 0

```

Il faut changer l'implémentation de __str__, nous allons utiliser les capacités d'instrospection
pour avoir une fonction qui s'adapte mieux aux changement

``` python
>>> class Point2D:
...     compteur = 0
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x=None, y=None):
...         self.x, self.y = x, y
...         self.identifiant = self.__class__.compteur
...         self.__class__.compteur += 1
...     @classmethod
...     def fromstring(cls, string_, sep=','):
...         coords = [float(coord) for coord in string_.split(sep)]
...         return cls(*coords)
...
...     def __str__(self):
...         return f"{self.__class__.__name__}:{self.__dict__}"
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...     def translation(self, x, y):
...         self.x += x
...         self.y += y
...     __repr__ = __str__
>>> dix_dix = Point2D.fromstring('10,10')
>>> dix_onze = Point2D.fromstring('10,11')
>>> dix_onze
Point2D:{'x': 10.0, 'y': 11.0, 'identifiant': 1}
>>> dix_dix
Point2D:{'x': 10.0, 'y': 10.0, 'identifiant': 0}

```

Les instances peuvent acceder en lecture aux variables de classes
``` python

>>> dix_dix.compteur
2

```

On peut parfois remplacer a la volée une variable de classe pour une instance (à éviter ceci dit)
``` python
>>> dix_dix.compteur = 34
>>> dix_onze.compteur
2
>>> dix_dix.compteur
34
>>> dix_dix
Point2D:{'x': 10.0, 'y': 10.0, 'identifiant': 0, 'compteur': 34}

```

Les properties et la surcharde d'operateurs
===========================================

Nous aimerions utiliser Point2D.norm() comme si c'etait un attribut on utilise pour cela @property
Nous aimerions aussi pouvoir ajouter des points. Python permet de traiter cela avec elegance

``` python
>>> class Point2D:
...     ''' Définit un point en 2D avec x et y comme coordonnées '''
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...
...     @property
...     def norm(self):
...         return (self.x**2 + self.y**2) ** (0.5)
...
...     def __add__(self, other):
...         return Point2D(self.x + other.x, self.y + other.y)
...     def __iadd__(self, other):
...         [setattr(self, name, getattr(self, name) + getattr(other, name))
...          for name in ['x', 'y']] #J'illustre une astuce, ne pas le faire au travail.
...         return self

>>> point = Point2D(3,4)
>>> point.norm
5.0
>>> p1 = Point2D(3,0)
>>> p2 = Point2D(0,4)
>>> p3 = p2 + p1
>>> p3.norm
5.0
>>> sum([p1, p2], Point2D(0,0)).norm
5.0
>>> p2 += p1
>>> p2.norm
5.0

```

