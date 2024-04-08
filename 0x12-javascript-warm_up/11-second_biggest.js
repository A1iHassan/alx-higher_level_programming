#!/usr/bin/node
const x = [];
process.argv.splice(2).forEach(element => {
  x.push(+element);
});
if (x.length <= 3) {
  console.log(0);
} else {
  x.sort((a, b) => b - a);
  console.log(x[1]);
}
