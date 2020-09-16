#!/usr/bin/node

const sentence = [];
sentence.push(process.argv[2]);
sentence.push(' is ');
sentence.push(process.argv[3]);
console.log(...sentence);
