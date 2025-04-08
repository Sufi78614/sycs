const http = require('node:http');

const listener = function (request, response) {
    response.writeHead(200, { 'Content-Type': 'text/html' });
    response.end('<h2 style="text-align: center">Server is running here</h2>');
};

const server = http.createServer(listener);
server.listen(3000);
console.log('Mohammad Husain 5042');
console.log('Server Running at http://127.0.0.1:3000/');
