-module(hello).
-export([hello/0]).
-author("Simon Wells").

hello() -> io:fwrite("Hello World\n", []).