#!/usr/bin/node

exports.nbOccurences = function (list, searchElement)
{
    let nvar = 0;
    for (let i = 0; i < list.length; i++)
	if (list[i] === searchElement)
	    nvar+=1
    return nvar
}
