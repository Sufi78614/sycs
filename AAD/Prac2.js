#implement event module of node.js
var events = require('events');
var eventEmitter = new events.EventEmitter();

// Create an event handler
var connectHandler = function connected() {
    console.log('Connection successful.');
    eventEmitter.emit('data_received');
};

// Bind the connection event
eventEmitter.on('connection', connectHandler);

// Bind data_received event
eventEmitter.on('data_received', function () {
    console.log('Data received successfully.');
});

// Fire the connection event
eventEmitter.emit('connection');

console.log("Mohammad Husain 5042");
console.log("Program Ended.");
