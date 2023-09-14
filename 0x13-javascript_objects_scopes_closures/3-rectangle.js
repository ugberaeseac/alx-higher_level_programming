#!/usr/bin/node

class Rectangle {
  /* class that defines a Rectangle object */
  constructor (w, h) {
  /* constructor */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
