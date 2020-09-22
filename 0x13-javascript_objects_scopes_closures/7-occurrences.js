#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let ocurren = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      ocurren++;
    }
  }
  return ocurren;
};
