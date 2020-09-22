#!/usr/bin/node
const fs = require('fs')
function readfile(file)
{
  try {
      const data = fs.readFileSync(file, 'utf8')
      return data;
  } catch (err) {
      console.error(err);
  }
}
function writefile(path, content)
{
    try {
	const data = fs.writeFileSync(path, content);
    } catch (err) {
	console.error(err)
    }
}

data = readfile(process.argv[2]);
data1 = readfile(process.argv[3]);
content = data + '\n' + data1 + '\n';
writefile(process.argv[4], content)
