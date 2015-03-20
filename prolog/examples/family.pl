mother(luke,padme).
mother(leia,padme).
father(luke,anakin).
father(leia,anakin).
male(luke).
female(leia).
brother(X,Y) :- mother(X,Z), mother(Y,Z), male(X).
sister(X,Y) :- mother(X,Z), mother(Y,Z), female(X).

