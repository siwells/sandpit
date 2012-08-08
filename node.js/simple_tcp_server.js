// Execute the script with:
// 	$ node simple_tcp_server.js
// Connect to the script with CURL:
//	$ curl 127.0.0.1:7000

var net = require('net');
var sys = require('sys');
var server = net.createServer(function (socket)
{
	socket.addListener("connect", function () 
	{
		sys.puts("Connection from " + socket.remoteAddress);
		socket.end("Hello World\n");
	});

});

server.listen(7000, "localhost");

console.log("TCP server listening on port 7000 at localhost.");
