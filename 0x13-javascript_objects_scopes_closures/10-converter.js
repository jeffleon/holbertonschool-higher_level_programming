#!/usr/bin/node

exports.converter = function (base) {
  return function (exp) {
    return exp.toString(base);
  };
};
