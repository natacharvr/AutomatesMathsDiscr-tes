# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from itertools import product
from automateBase import AutomateBase



class Automate(AutomateBase):

    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ (self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        l=set()
        for x in listStates :
            l.union(set(self.succElem(x,lettre)))
        return list(l)




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        l=[auto.getListInitialStates()]
        for lettre in mot:
            l=succ(l, lettre)
        for etat in l :
            if etat in auto.getListFinalStates() :
                return True
        return False


    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        for x in auto.listStates :
            list_t = auto.getListTransitionsFrom(x)
            for a in alphabet :
                temp =0
                for t in list_t :
                    if t.etiquette == a :
                        temp=1
                if temp ==0:
                    return False
        return True



    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        l=auto.getAlphabetFromTransitions()
        etat = auto.listStates
        for e in etat :
            for lettre in l :
                if len([e].succ([e], lettre))>1 :
                    return False
        return True



    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        """
        auto2 =copy.deepcopy(auto)
        auto2.prefixStates(0)
        if (estComplet(auto, alphabet)) :
            sp = State(label="Puits", id=1, fin=False,init= False)
            auto2.addState(sp)
        for x in auto.listStates :
            for a in alphabet :
                if a not in auto.getListTransitionsFrom(x):
                    auto2.addTransition(Transition(etiquette = a, stateSrc=x,stateDest=sp))
        return auto2



    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        finaux = set(auto.getListFinalStates())
        init = set(auto.getListInitialStates()) #premier état (on a vérifié c'est bon)

        alph = auto.getAlphabetFromTransitions()
        listeTransition = []
        listeEtat= []
        l=[] #liste des ensembles
        l.append(init) #l=[{0}]
        k=0
        j=-1
        print(init)
        for x in l :
            j+=1
            for lettre in alph :
                print(lettre)
                if (auto.succ(list(init), lettre)!=[]):
                    if (set(auto.succ(list(init), lettre)) not in l) : #si l'ensemble n'est pas dans la liste
                        l.append(set(auto.succ(list(init), lettre)))# on l'y ajoute
                        i = False
                        f = False
                        print("bonjour ", l[-1])
                        for s in l[-1] :
                            if s in finaux :
                                f=True
                            elif s in init:
                                i=True
                            listeEtat.append(State(label=k, id=k, fin=f, init= i)) # on ajoute l'etat crée avec le bon fin/initial
                            print("bonjour ", listeEtat)
                            listeTransition.append(Transition(etiquette = lettre, stateSrc=listeEtat[k],stateDest=ListeEtat[-1])) #transition de l'étiquette
                            k+=1
                    else : #ensemble dans la liste
                        indice = 0
                        while (indice <len(l)):

                            if l[indice] == set(auto.succ(list(init), lettre)) : #si l'ensemble est à cet endroit indice de la liste
                                e = indice #on trouve sa place dans la liste
                            indice+=1
                    listeTransition.append(Transition(etiquette = lettre, stateSrc=listeEtat[0],stateDest=listeEtat[0])) #on rajoute la bonne transition

        auto2 = Automate(listeTransition) #on cree l'automate à partir des transitions
        return auto2



    @staticmethod
    def complementaire(auto,alphabet ):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
        auto2 = determinisation(auto)
        auto2 = completeAutomate(auto2, alphabet)
        l= auto.listStates

        for x in l:
            if x.fin == True:
                x.fin = False
            else: x.fin = True
        return auto2


    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """

        #on récupère les transitions deux par deux et on crée un état à chaque fois sauf si l'état existe déjà ?

        auto2 = Automate(listeTransition) #on cree l'automate à partir des transitions
        return

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return





    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return


    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return
