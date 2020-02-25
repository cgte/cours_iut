#Découvere de git


  - Creer un compte sur gitlab.com
    - Register
  - creer un projet iut
    - privé
  - Lancer l'invite de commande bash sur votre machine
    -  lancer les commandes suggerées: dans la section git global setup
  -
  - cloner le projet avec l'invite de commande de git sur votre machine
  -
  - creer un dossier td6, créer un fichier rendu.py dedans
  - git add rendu.py

  - lancer la commande `git add td6/rendu.py`
  - lancer la commande `git commit -m "Ajout du rendu du tp"` puis git push
  - vérifiez que le fichier apparait bien en ligne.

# À la découverte de fonctions

Durant ce tp nous allons implémenter différentes fonctions et demander
au programme d'opérer ces fonctions sur des listes de nombres.

On souhaite faire quelque chose ce de type

```
python3 truc.py

donnez un nom ou quittez en tapant exit dataset1
Entrez les valeurs
1,2,3,4,5,6
Donnez le nom de la fonction a utiliser sum
21.0
donnez un nom ou quittez en tapant exit dataset1
Donnez le nom de la fonction a utiliser moyenne
Traceback (most recent call last):
  File "truc.py", line 13, in <module>
KeyError: 'moyenne'

```


remplissez le code suivant pour
  - Question  1 :avoir deux dictionnaires qui contiendront les noms: valeurs des dataset ansi que des fonctions
  - Question 2 : Bien convertir les saisies en suite de nombres de type float.
  - Utilisez la fonction split  regardez de ce `'qwer,tyu,de'.split(',')` vaut
  - Utilisez si possible une liste en conprehension. `exemple = [fonction(x) for x in valeurs]`


```python

registre_valeurs =
registre_fonction =
#Ajouter la fonction sum au registre

def loop():
    dataset_name = input("Entrz le nom du dataset")
    if dataset_name not in registre_valeurs:
        valeurs = input("Entrez les valeurs séparées par une virgule ")
        registre_valeurs[dataset_name] =
    fonction = input("Donnez le nom de la fonction a utiliser")
    #Afficher le résulat


if __name__ == "__main__":
  while True:
      message = input("entrée pour continuer, quittez en tapant exit puis entrée ")
      if message == "exit":
          break
      loop()

```

  - Question 3: implementez remplissez le registe avec les fonctions 'max', 'min', 'moyenne' et 'ecart-type'


Nous souhaiterions pouvoir obtenir les puissances de n des elements d'une liste en saisissant puiss(n)
comme entrée.


premiere implémentation:


  - Question 4:  faire 4 fonctions, puiss1, puiss2, puiss3 et puiss4 qui renvoient x à la puissance correspondante

Nous voyons que le code se repete beaucoup, nous aimerions pouvoir arbitrairement fabriquer une fonction qui serait renvoyée pour qu'on puisse l'utiliser.

par exemple pour afficher le temps pris par une fonction on peut faire la chose suivante:

```python
from time import time, sleep
def mafonction():
  sleep(0.4)
  print 1

def chronomafonction():
    t = time()
    res = mafonction()
    print("%2f" % time - t)
    return res
```
en fait on pourrait passer mafonction en parametre à chronomafonction pour pouvoir utiliser
n'importe quelle autre fonction. On peut définir des fonctions dans d'autres fonctions.


```python
def chorno(fonction):
    def chronometree():
      t = time()
      res = fonction()
      print("%2f" % time - t)
      return
   return chronometree

fonction_chrono = chrono(mafonction)
fonction2_chorno = chrono(uneautrefonction)

```

Si la fonction prends un paramètre il faut que la fonction que nous allons renvoyer en prenne aussi un

```python
def mafonction(n):
  print(n)


def chorno(fonction):
    def chronometree(n_nouveau):
      t = time()
      res = fonction(n_nouveau)
      print("%2f" % time - t)
      return
   return chronometree

fonction_chrono = chrono(mafonction)
#ou encore
mafonction = chrono(mafonction) # ce qui permet de changer la fonction utilisée a chaque appel dans notre code
fonction2_chorno = chrono(uneautrefonction)

```

```
#un exemple dans ipython

In [6]: def modn(n):
   ...:     def monmodulo(p):
   ...:         return p % n
   ...:     return monmodulo
   ...:

In [7]: modn(5)(10)
Out[7]: 0

In [8]: modn(5)(11)
Out[8]: 1

```

5/Utilisez ceci pour renvoyer une fonction qui renvoie la fonction puissance n-ième
appelez la `pow_n_1`

6/continuez sur cette lancée pour creer une fonction `pown(n)` qui prend un parametre une liste et revoie une liste avec ses elements à la puissance n et integrez les deux fonctions précedentes dans les registres

Nous aimerions automatiquement enregister les fonctions dans le registre, au moment ou nous les écrivons.
une premiere approche serait la suivante.

``` python
def fonction():
  pass

registre[fonction.__name__] = fonction
```

7/ecrivez une fonction register_function qui enregistre la fonction dans le registre.

Il existe en fait une possibilité plus élégante de de faire register_function(function), on peut utiliser ce que l'on appelle un décorateur.

``` python
import time


def time_call(fonction):
    """ Cette fonction appele `fonction` mais affiche en plus le temps pris """

    def timed_call(a,b,c):
        t0 = time.time()
        result = fonction(a, b, c)
        print(f"Temps pris par {fonction.__name__} {time.time() - t0:.2f}")
        return result

    return timed_call

@time_call
def dodo(a, b, c):
  sleep(sum(a,b,c))

```

8/changer le code pour que register function renvoie la fonction prise en entrée, que celle ci soit
mise dans le registre et utilissez la syntaxe avec un arobase

#Les parametres generiques `*args` et `**kwargs`

Il arrive parfois que l'on puisse avoir un nombre variable de paramètres, par exemple la fonction print
```
print('q', 3, 4,5, 'n')
```


```python
def mafonction(param1, param2, param3=None, *options, **kw_options):
  print(options)
  print(kw_options)

mafonction(1,2,3,4,5, oui='oui', 'peut_etre'='None')
liste = [1,2,3,4,5]
dico = dict( oui='oui', peut_etre='None') # Tenez donc, dict prend aussi un nombre variable de parametres nommes
mafonction(*liste, **dico)

```

Avec cet appel on peut transmettre directement des parametres à la fonction sans se soucier de son prototype.
Ce qui est pratique par exemple quand on ne souhaite pas se poser de question sur le nombre de parametres d'une fonction sur laquelle on souhaite modififier un comporement.

9/ Changer la methode time_call pour prendre en compte n'importe quel type de parametre en entrée et les faire passer a la fonction dont on souhaite mesurer le temps d'execution.



