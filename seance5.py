import time
import json

from bottle2 import response, request, Bottle


def time_call(fonction):
    """ Cette fonction appele `fonction` mais affiche en plus le temps pris """

    def timed_call(*args, **kwargs):
        t0 = time.time()
        result = fonction(*args, **kwargs)
        print(f"Temps pris par {fonction.__name__} {time.time() - t0:.2f}")
        return result

    return timed_call


class Gift:
    allowed_kinds = 'small medium large'.split()
    
    def __init__(self, kind):
        print(f"creating {kind} gift")
        if kind == "small":
            self.weight = 0.5
            self.duration = 1
            self.kind = kind
        elif kind == "medium":
            self.weight = 2
            self.duration = 2
            self.kind = kind
        elif kind == "large":
            self.weight = 5
            self.duration = 3
            self.kind = kind
        else:
            raise ValueError(f"Error {kind} is unknown")

    @time_call
    def wrap(self):
        print("Starting to wrap")
        time.sleep(self.duration)
        print(f"Wrapped a {self.kind} gift")

    def __str__(self):
        return f"{self.__class__.__name__}('{self.kind}')"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.kind}')"


@time_call
def create_gift(kind):
    return Gift(kind)


@time_call
def create_gifts(kinds):
    return [create_gift(kind) for kind in kinds]


@time_call
def onfly_create_gifts(kinds):
    for kind in kinds:
        yield create_gift(kind)


class Sledge:
    def __init__(self):
        self.gifts = []
        self.max_load = 12
        self.time_per_gift = 0.5

    @property
    def free_load(self):
        return self.max_load - sum(gift.weight for gift in self.gifts)

    @property
    def load(self):
        return sum(gift.weight for gift in self.gifts)

    def take_gift(self, gift):
        if gift.weight <= self.free_load:
            self.gifts.append(gift)
        return gift in self

    @time_call
    def ship(self):
        print(f"Shipping {len(self)}")
        print(f"{self.load} kg to be shipped")
        for gift in self:
            time.sleep(self.time_per_gift)
        print(f"Shipped  {len(self)}")
        self.gifts = []

    def __len__(self):
        return len(self.gifts)

    def __iter__(self):
        return iter(self.gifts)

    def __getitem__(self, key):
        return self.gifts[key]

    def __contains__(self, gift):
        return gift in self.gifts

    def __repr__(self):
        return str(self.__dict__)


sledge = Sledge()




app = Bottle()


from time import sleep

@app.get("/gift")
def gift_form():
    return """
        <form action="/gift" method="post">
            Type de cadeau: <input name="kind" type="text" />
            <input value="Ajouter" type="submit" />
        </form>
    """
#ici on renvoie un formulaire.

reroute_js = '''
    <script type="text/javascript">
    window.open('/gift', '_top')
    </script>
''' 
#astuce pour renvoyer dynamiquement vers une autre page

#Question 0L lancer le code et allez sur la page http://localhost:8080/gift
# recuperez le fichier bottle2.py sur le dépot et mettez la dans votre dossier

@app.post("/gift")  # or @route('/login', method='POST')
def process_gift():
    kind = request.forms.get("kind") or request.json.get("kind")
    #Question 1 
    
    if #question_2:
        yield f"{gift} added to sledge <br/> sledge is now {sledge.gifts}"
    else:
        message = f"sledge is full, shipping {sledge.gifts}<br>"
        yield message
        # Question 3
        message = f"sledge now has {sledge.gifts}"

        yield message
    time.sleep(2)
    yield reroute_js


@app.route("/sledge")
def view_sledge():
    response.content_type = "application/json"

    return json.dumps(sledge.__dict__, default=lambda o: o.__dict__)





@app.route("/ship")
def ship():
    #Question 4 implementer ici la livraison
    pass
    

"""Question5 ajouter un statut aux cadeaux est il new, wrapped, waiting
 ready, shipping ou delivered"""

 

"""Quesiton 6 Modifier le code pour mettre a jour le statut des cadeaux au fur et a mesure"
"""

""" question 7 creer une vue '/gifts' qui affiche tous les cadeaux depuis 
le départ avec les informations utiles.
vous pouves vous inspierer de : 
<ul>
<li>{gift}</li>
<li> </li>
<li> </li>
</ul>
"""


""" Question 8
Gerer le cas ou on n'envoie pas le bon type de cadeau à l'aide de try: except
dans la vue qui crée les cadeaux.
try:
    #creeer un cadeau
except ValueError as exc:
    #faire quelque chose avec str(exc)

Question 9 : Utiliser le code suivant pour voir un suivi en direct des cadeaux.
 à la place de 
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
    
    
copier coller :
    

from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn

class ThreadingWSGIServer(ThreadingMixIn, WSGIServer): 
    pass

if __name__ == "__main__":
    httpd =  make_server('', 8080, app, ThreadingWSGIServer)
    httpd.serve_forever()
    
    
Ajouter a la vue gift:   
    yield '''
    <script language="javascript">
setInterval(function(){
   window.location.reload(1);
}, 500);
</script>
    '''
 Dans deux fenetres creez et voyez l'evolution    
    
    
"""



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
