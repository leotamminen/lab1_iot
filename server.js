const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post('/test', (req, res) => {
    const body = req.body;

    // Access device name and decoded payload (assuming ChirpStack sends it this way)
    const devName = body.deviceName || 'unknown';
    const temperature = body.object?.temperature;

    const line = `${devName} ${JSON.stringify({ temperature })}\n`;

    fs.appendFile('data.txt', line, (err) => {
        if (err) console.error('Failed to write:', err);
        else console.log(`${line.trim()} written to file`);
    });

    res.sendStatus(200);
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/test`);
});
