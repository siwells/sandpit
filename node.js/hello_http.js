var http = require('http');

var server = http.createServer(function(req, res) {
    console.log(req.headers)
    console.log(req.url)
    res.writeHead(200);
    res.end('Hello Http\n');
});
server.listen(8080);
