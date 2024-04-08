#!/usr/bin/node
let x;
if ((x = +process.argv[2])) {
  for (let i = 0; i < x; i++) {
    console.log('X' * x);
  }
} else {
  console.log('Missing size');
}
