#!/usr/bin/node

const factorial = (number) => {
  if (number <= 1) { return 1; }
  return number * factorial(number - 1);
};
if (process.argv.length === 2) console.log(1);
else {
  if (parseInt(process.argv[2])) { console.log(factorial(parseInt(process.argv[2]))); }
}
