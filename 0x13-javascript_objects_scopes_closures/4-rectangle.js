#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 && (h = parseInt(h) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
  }

  rotate () {
    const w = this.width;
    const h = this.height;

    this.width = h;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
