-module(misc).
-export([greet/2,head/1,second/1,third/1,same/2,beach/1,talking/1]).

greet(male, Name) -> io:format("Hello, Mr. ~s!~n", [Name]);
greet(female, Name) -> io:format("Hello, Mrs. ~s!~n", [Name]);
greet(_, Name) -> io:format("Hello, ~s!~n", [Name]).

head([H|_]) -> H.

second([_,X|_]) -> X.

third([_,_,X|_]) -> X.

same(X,X) -> true;
same(_,_) -> false.

beach(Temperature) ->
case Temperature of
{celsius, N} when N >= 20, N =< 45 ->
'favorable';
{kelvin, N} when N >= 293, N =< 318 ->
'scientifically favorable';
{fahrenheit, N} when N >= 68, N =< 113 ->
'favorable in the US';
_ ->
'avoid beach'
end.

talking(Animal) ->
Talk = if Animal == cat  -> "meow";
Animal == beef -> "mooo";
Animal == dog  -> "bark";
Animal == tree -> "bark";
Animal == pig   -> "oink";
true -> "fnarf fnarf"
end,
{Animal, "says " ++ Talk ++ "!"}.