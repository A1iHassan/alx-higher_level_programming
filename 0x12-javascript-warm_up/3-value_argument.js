#!/usr/bin/node
let x;
if ((x = process.argv[2])) {
  console.log(x);
} else {
  console.log('No argument');
}
