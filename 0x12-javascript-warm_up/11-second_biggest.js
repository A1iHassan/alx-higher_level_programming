#!/usr/bin/node
const x = new Set();
process.argv.splice(2).forEach(element => {
  x.add(+element);
});
x.splice(x.indexOf(Math.max(...x)));
console.log(Math.max(...x));
