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
}

module.exports = Rectangle;
