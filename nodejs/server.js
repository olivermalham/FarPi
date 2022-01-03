const express = require('express');
const app = express(),
      bodyParser = require("body-parser");
      port = 8080;

const users = [];

app.use(bodyParser.json());
app.use(express.static(process.cwd()+"/../marvin_ui2/dist/farpi2"));

app.get('/', (req,res) => {
  res.sendFile("index.html", {root:"../marvin_ui2/dist/farpi2"})
});

app.listen(port, () => {
    console.log(`Server listening on the port::${port}`);
});
