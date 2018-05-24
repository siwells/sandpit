han.
anakin.
luke.
kylo.
leia.
padme.
shmi.
mother(anakin, shmi).
mother(luke,padme).
mother(leia,padme).
mother(kylo,leia).
father(luke,anakin).
father(leia,anakin).
father(kylo,han).
male(luke).
male(anakin).
male(kylo).
male(han).
female(leia).
female(padme).
female(shmi).
brother(X,Y) :- mother(X,Z), mother(Y,Z), male(X).
sister(X,Y) :- mother(X,Z), mother(Y,Z), female(X).
parent(X,Y) :- mother(X,Y); father(X,Y).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
people(L) :- findall(X, (male(X); female(X)), L).

