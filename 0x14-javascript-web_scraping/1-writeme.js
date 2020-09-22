#!/usr/bin/node
var fs = require('fs');
fs.writeFileSync(process.argv[2], process.argv[3], (err) => console.log(err));
