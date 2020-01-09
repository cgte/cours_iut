#Intégreation dans un framework web

installer les bibliotheques bollle et httpie


Dans cette seance nous allons nous interesser mettre en place un serveur web afin que des utilisateurs
puissent utiliser notre code.

Pour cela nous allons utilier le cadriciel bottle qui est un micro framework.

Quand nous utilisons un navigateur celui ci envoie des requetes vers un serveut une premiere
facon de passer des parametres est de les mettre dans l'url, (requete GET) c'est ce que nous ferons en premier.

integration des vues:


```python
from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

run(app, host='localhost', port=8080)


```

copier le code dans le dépot et ensuite lancez le programme,
rendez vous a l'adresse http://localhost:8080

Modifiez le code afin de personaliser


```python
from bottle import route, run, template, response

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(app, host='localhost', port=8080)
```


implementez les vues suivantes:

```python
@route('/create/<kind>')
def create_gift(kind):
    #crée un cadeau, l'ajoute au traineau si possible.
    # dans ce cas utiliser return f"{gift} added to sledge <br/> sledge is now {sledge.gifts}"
    #si le cadeau n'est pas dans le traineau alors lancer la livraison
    # Afficher le nombre de ceadeaux qui ont été livrés.


@route('/ship')
def ship():
    #si le traineau est vide afficher "nothing to do"
    #sinon livrer et afficher le nombre de cadeaux livrés

```

#JSON

Renvoyer une page est pratique pour un humain mais dans ne ombreux cas ce sont des ordinteurs qui
communiquent entre eux, pour cela on utiliser le format JSON (JavaScript Object Notation).
Ajouter la route suivante, apres avoir relancé l'application crééz des cadeaux et consultez
le contenu du traineau.

```python
@route('/sledge')
def view_sledge():
    import json
    return json.dumps(sledge.__dict__, default=lambda o: o.__dict__)
```

Utilisation en ligne de commande

http localhost:8080/create/small
http localhost:8080/sledge


http --form POST :8080/gift kind=medium
http POST :8080/gift kind=medium


