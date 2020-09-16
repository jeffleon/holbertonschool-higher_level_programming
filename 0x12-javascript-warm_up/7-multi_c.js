#!/usr/bin/node

if (process.argv.length == 2)
    console.log('Missing number of occurrences');
if (parseInt(process.argv[2]) && parseInt(process.argv[2]) > 0)
{
    let args = parseInt(process.argv[2]);
    for(;args > 0;args--)
       console.log("C is fun");
}