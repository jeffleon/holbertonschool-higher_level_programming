#!/usr/bin/node

if(process.argv.length > 3)
{
    let numb = process.argv.map((element)=> parseInt(element, 10));
    let s = numb.slice(2).sort((a,b)=>a-b);
    console.log(s[s.length - 2]);
}
else
    console.log(0);
