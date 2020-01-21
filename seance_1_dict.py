import time


def create_gift(kind):
    print(f"creating {kind} gift")
    if kind == "small":
        weight = 0.5
        duration = 1
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


def create_gifts(kinds):
    return [create_gift(kind) for kind in kinds]


sledge = {"gifts": [], "max_load": 12, "time_per_gift": 0.5}


def wrap_gift(gift):
    print("Starting to wrap")
    time.sleep(gift["duration"])
    print("Wrapped a %s gift" % gift["kind"])


def compute_free_load(sledge):
    return sledge["max_load"] - sum(gift["weight"] for gift in sledge["gifts"])


def sledge_load(sledge):
    return sum(gift["weight"] for gift in sledge["gifts"])


def take_gift(sledge, gift):
    if gift["weight"] <= compute_free_load(sledge):
        sledge["gifts"].append(gift)
        return 1
    else:
        return 0


# Tiends mais il faudrait qu'on puisse savoir si le cadeau a été pris
# Soit a la valeur de return
#  (exception)


def ship(sledge):
    print(f"Shipping {len(sledge['gifts'])}")
    print(f"{sledge_load(sledge)} kg to be shipped")

    for gift in sledge["gifts"]:
        time.sleep(sledge["time_per_gift"])
    print(f"Shipped  {len(sledge['gifts'])}")
    sledge["gifts"] = []


def process_gifts(gifts):
    for gift in gifts:
        wrap_gift(gift)
        taken = take_gift(sledge, gift)
        if taken == 1:
            print(f"current load {sledge_load(sledge)}")
            continue
        else:
            ship(sledge)
            taken = take_gift(sledge, gift)
            if taken == 0:
                print("Error, sledge should take the gift after shipping")
    else:
        ship(sledge)


def create_and_process(gift_types):
    process_gifts(create_gifts(gift_types))


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        n_gifts = int(sys.argv[1])
    else:
        n_gifts = 15
    from random import choices

    gift_types = choices(["small", "medium", "large"], k=n_gifts)
    create_and_process(gift_types)
