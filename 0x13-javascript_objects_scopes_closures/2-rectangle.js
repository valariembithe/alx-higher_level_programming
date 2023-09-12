#!/usr/bin/node
/* A class named Rectangle with w & h */

class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
                return this;
        }
		this.width = w;
		this.height = h;
	}
}
module.exports = Rectangle;
