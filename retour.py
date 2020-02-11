Erreurs commises:
class TestGift(unittest.TestCase):
    def wrap_gift(gift):
        print("Starting to wrap")
        time.sleep(gift["duration"])
        print("Wrapped a %s gift" % gift["kind"])
           
unittest.main()

class TestGift1(unittest.TestCase):
    def create_gift2(kind):
        print(f"creating {kind} gift")
        time.sleep(1)
        if kind == "small":
            weight = 0.5
            duration = 
            return {"kind": kind, "duration": duration, "weight": weight}
        elif kind == "medium":
            weight = 2
            duration = 2
            return {"kind": kind, "duration": duration, "weight": weight}
    
        elif kind == "large":
            weight = 5
            duration = 3
            return {"kind": kind, "duration": duration, "weight": weight}
    
        else:
            print(f"Error {kind} is unknown")

unittest.main()

-> que testez vous ?
-> pourquoi lancer les tests à chaque import ?

class TestGift(unittest.TestCase):
    def __init__(self, type_gift):
        print(f"creating {type_gift} gift")
        time.sleep(1)
        if type_gift == "small":
            self.weight = 0.5
            self.duration = 1
        
        elif type_gift == "medium":
            self.weight = 2
            self.duration = 2

        elif type_gift == "large":
            self.weight = 5
            self.duration = 3
        
        else:
            print(f"Error {type_gift} is unknown")
unittest.main()

