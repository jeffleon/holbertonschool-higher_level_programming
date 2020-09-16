#!/usr/bin/node

let sentence = [];
sentence.push(process.argv[2]);
sentence.push(' is ');
sentence.push(process.argv[3]);
console.log(...sentence);

    