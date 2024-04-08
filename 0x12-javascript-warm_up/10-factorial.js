#!/usr/bin/node
function factorial (x) {
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}
let input;
if ((input = +process.argv[2])) {
  console.log(factorial(input));
} else {
  console.log(1);
}
