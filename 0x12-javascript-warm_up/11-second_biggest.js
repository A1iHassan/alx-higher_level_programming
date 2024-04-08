#!/usr/bin/node
const x = process.argv;
x.pop(Math.max(...x));
console.log(Math.max(...x));
