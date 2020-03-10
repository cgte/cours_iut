"""
Solutions elegantes trouvées :

Génin:

"""

if fonction_name[1:5] == "puiss".lower():
    n = fonction_name[5:6]
    res = registre_fonction[fonction_name](registre_valeurs[dataset_name])


def pown(l):
    l=list(map(int, l))
    n=int(input("entrez un entier : "))
    l=[l[i-1]**n for i in l]
return l

def puiss1(l):
    l=list(map(int, l))
    n=1
    l=[l[i-1]**n for i in l]
return l ^     ^
 #       |     |-> une recherche de variable qui ne sert a rien
 #        \ Serieusement, un simple test vous aurait permis de savoir que c'est faux

-> Oui tout a fait, convertissez tout en int ....
