#!/usr/bin/node
const list = require('./100-data').list;

new_list = list.map((element, index)=>{
    return element * index
})
console.log(list)
console.log(new_list);
