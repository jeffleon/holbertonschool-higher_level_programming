#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${c}`.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
