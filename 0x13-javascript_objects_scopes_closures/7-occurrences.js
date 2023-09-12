#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	const filteredElement = list.filter(item => item === searchElement);
	return filteredElement.length;
}
