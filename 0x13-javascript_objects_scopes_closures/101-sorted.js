#!/usr/bin/node

const dict = require('./101-data').dict;
let new_dict = {}
let lista = []
for (let key in dict)
{
    if (dict[key] in new_dict)
	new_dict[dict[key]].push(key);
    else
	new_dict[dict[key]] = [key];
} 
console.log(new_dict)
