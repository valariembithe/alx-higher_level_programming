#!/usr/bin/node

const { argv } = require('process');

function add (a , b) {
	a = parseInt(a);
	b = parseInt(b);
	return (a + b);
}
console.log(add(argv[2], argv[3]));
