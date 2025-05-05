const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8765 });

console.log('✅ WebSocket server running on ws://localhost:8765');

wss.on('connection', function connection(ws) {
  console.log('Client connected');

  ws.on('message', function incoming(message) {
    console.log('Received:', message.toString());
  });

  ws.send('Hello from the server!');
});
