#!/usr/bin/node

if (process.argv.length === 2) { console.log('Missing size'); }
if (parseInt(process.argv[2]) && parseInt(process.argv[2]) > 0) {
  const args = parseInt(process.argv[2]);
  for (let i = 0; i < args; i++) {
    let cube = '';
    for (let j = 0; j < args; j++) { cube = cube.concat('x'); }
    console.log(cube);
  }
}
