const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });

  const response = {
    status: 'healthy',
    service: 'node-api',
    nodeVersion: process.version,
    timestamp: new Date().toISOString(),
  };

  res.end(JSON.stringify(response));
});

const port = process.env.PORT || 8080;
server.listen(port, '0.0.0.0', () => {
  console.log(`Server started on port ${port}`);
});
