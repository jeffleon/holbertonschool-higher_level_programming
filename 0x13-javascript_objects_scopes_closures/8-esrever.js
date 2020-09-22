#!/usr/bin/node

exports.esrever = function (list) {
  let inrev = list.length - 1;
  const newList = [];
  for (let i = 0; i < list.length; i++, inrev--) {
    newList[inrev] = list[i];
  }
  return newList;
};
