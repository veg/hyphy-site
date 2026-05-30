const express = require('express'),
  path = require('path');


const port = process.env.PORT || 8003;
const app = express();

app.use(express.static('site'));

app.listen(port, ()=>{
  console.log('Listening on port', port, '...');
});
