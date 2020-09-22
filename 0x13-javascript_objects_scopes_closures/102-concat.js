#!/usr/bin/node

const fs = require('fs');
function readfile (file) {
  const data = fs.readFileSync(file, 'utf8');
  return data;
}
function writefile (path, content) {
  const data = fs.writeFileSync(path, content, (err) => console.log(err));
  return data;
}

const data = readfile(process.argv[2]);
const data1 = readfile(process.argv[3]);
const content = data + data1;
writefile(process.argv[4], content);
