#!/usr/bin/node
const x = [];
process.argv.splice(2).forEach(element => {
  x.push(+element);
});
x.splice(x.indexOf(Math.max(...x)));
console.log(Math.max(...x));
