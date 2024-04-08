#!/usr/bin/node
let x = [];
process.argv.splice(2).forEach(element => {
	x.push(+element);
});
x.splice(x.indexOf(Math.max(...x)))
if (x.length === 0 || x.length === 1) {
	console.log(0);
} else {
	console.log(Math.max(...x));
}
