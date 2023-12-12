#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(['School', 89, { id: 12 }, 'String']));

const listA = [1, 2, 3, 4, 5];
console.log(listA.length); // added this as a practice to understand how `.length` works
