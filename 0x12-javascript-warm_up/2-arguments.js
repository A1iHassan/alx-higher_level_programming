#!/usr/bin/node
const x = process.argv;
if (x.length === 2) {
  console.log('No argument');
} else if (x.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
