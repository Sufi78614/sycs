#read html file from node.js
var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
    fs.readFile('prac4.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        return res.end();
    });
}).listen(8081);
console.log("Mohammad Husain 5042");
