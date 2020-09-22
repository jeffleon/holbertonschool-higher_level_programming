#!/usr/bin/node

const fs = require('fs');
function readfile (file) {
  try {
    const data = fs.readFileSync(file, 'utf8');
    return data;
  } catch (err) {
    console.error(err);
  }
}
function writefile (path, content) {
  try {
    const data = fs.writeFileSync(path, content);
    return data;
  } catch (err) {
    console.error(err);
  }
}

const data = readfile(process.argv[2]);
const data1 = readfile(process.argv[3]);
const content = data + '\n' + data1 + '\n';
writefile(process.argv[4], content);
