#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2])) {
	console.log('Missing size');
} else {
	const x = parseInt(argv[2]);
	const arr = [];
	for (let i = 0; i < x; i++) {
		console.log(arr.push('X'));
	}
	for (let j = 0; j < x; j++) {
		console.log(arr.join(''));
	}
}
