#!/usr/bin/node

const dict = require('./101-data').dict;
const NewDict = {};
for (const key in dict) {
  if (dict[key] in NewDict) {
    NewDict[dict[key]].push(key);
  } else {
    NewDict[dict[key]] = [key];
  }
}
console.log(NewDict);
