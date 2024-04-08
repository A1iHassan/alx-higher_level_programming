#!/usr/bin/node
let x;
if ((x = +process.argv[2])) {
  console.log(`My number: ${Math.floor(x)}`);
} else {
  console.log('Not a number');
}
