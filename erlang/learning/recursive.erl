-module(recursive).
-export([fac/1,altfac/1,tail_fac/1,tail_fac/2,duplicate/2,tail_duplicate/2]).
 
fac(N) when N == 0 -> 1;
fac(N) when N > 0  -> N*fac(N-1).


altfac(0) -> 1;
altfac(N) when N > 0 -> N*fac(N-1).


tail_fac(N) -> tail_fac(N,1).
tail_fac(0,Acc) -> Acc;
tail_fac(N,Acc) when N > 0 -> tail_fac(N-1,N*Acc).


duplicate(0,_) -> [];
duplicate(N,Term) when N > 0 -> [Term|duplicate(N-1,Term)].


tail_duplicate(N,Term) ->
tail_duplicate(N,Term,[]).
 
tail_duplicate(0,_,List) -> List;
tail_duplicate(N,Term,List) when N > 0 ->
tail_duplicate(N-1, Term, [Term|List]).