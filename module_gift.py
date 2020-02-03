#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from itertools import count

counter = count()

def make_identifier():
    return next(counter)



from copy import copy
KIND2GIFT = {
        'small': {'duration': 0.5, 'weight': 1},
        '...': {'...': '...'},
        }


def create_gift(kind):
    gift = copy(KIND2GIFT.get(kind, {}))
    gift['identifier'] = make_identifier()
    return gift

sledge = {'gifts': [], 'time_per_gift': 0.2455, 'max_load': 12}

def process_gift(gift):
    #ajout d'un cadeau au traineau
    pass

def take_gift(sledge, gift):
    #est ce qu'on peut prendre le cadeau dans le traineau
    pass
    return True
    

    