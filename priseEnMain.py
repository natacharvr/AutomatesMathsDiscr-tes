from automate import *

#s0 = State(id =0,label="0", fin=False,init= True)
#s1 = State(label="1",id=1, fin=False,init= False)
#s2 = State(label="2", id=2, fin=True,init= False)
#s3 = State(label="0bis", id=3, fin=False,init= True)

#t1= Transition(etiquette = "a", stateSrc=s0,stateDest=s0)
#t2= Transition(etiquette = "b", stateSrc=s0,stateDest=s1)
#t3= Transition(etiquette = "a", stateSrc=s1,stateDest=s2)
#t4= Transition(etiquette = "b", stateSrc=s1,stateDest=s2)
#t5= Transition(etiquette = "a", stateSrc=s2,stateDest=s0)
#t6= Transition(etiquette = "b", stateSrc=s2,stateDest=s1)

#auto = Automate([t1,t2,t3,t4,t5,t6])
#print(auto)
#t = Transition(etiquette = "a", stateSrc=s0, stateDest=s1)
#print(auto.removeTransition(t))
#auto.removeTransition(t1)

#print(auto.removeState(s1))
#auto.addState(s1)
#auto.addState(s3)
#print(auto)
#auto.show("A.ListeTrans")
#auto.addTransition(t1)
#print(auto)
#auto.show("A.ListeTrans")
#auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
#print(auto1.getListTransitionsFrom(s1))
#print(auto1)
#auto1.show("A1.ListeTrans")

#auto2 = Automate.creationAutomate("auto.txt")

#print(auto2)
#auto2.show("A2.ListeTrans")

s0 = State(0, True, False)
s1 = State(1, False, False)
s2 = State(2, False, True)

transitions = [Transition(s0, "a", s0),
               Transition(s0, "a", s1),
               Transition(s1, "a", s2),
               Transition(s1, "b", s2),
               Transition(s2, "b", s2),
               Transition(s2, "b", s0)]

a1 = Automate(transitions)
a2 = Automate.determinisation(a1)

#a2.show("testdeter")
