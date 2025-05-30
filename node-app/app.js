const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.use(express.json());

// Health check endpoint
app.get('/', (req, res) => {
  res.json({
    status: 'healthy',
    service: 'node-express-api',
    timestamp: new Date().toISOString(),
    version: '1.0.0'
  });
});

// Info endpoint
app.get('/api/info', (req, res) => {
  res.json({
    service: 'GC Secure Artifacts Node.js Demo',
    description: 'Minimal Express API for Chainguard/JFrog POC',
    features: [
      'Chainguard base image',
      'JFrog Artifactory integration',
      'Xray vulnerability scanning',
      'SBOM generation'
    ],
    nodeVersion: process.version,
    platform: process.platform
  });
});

// Echo endpoint
app.post('/api/echo', (req, res) => {
  res.json({
    received: req.body,
    timestamp: new Date().toISOString()
  });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on port ${port}`);
});
