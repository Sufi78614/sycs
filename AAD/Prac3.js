#own module in node.js
var http = require('http');

function myDateTime() {
    return new Date();
}

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write("The Date And Time Are Currently: " + myDateTime());
    res.end();
}).listen(8081);

console.log("Server running at http://127.0.0.1:8081/");
console.log("Khan Faizan 5106");
