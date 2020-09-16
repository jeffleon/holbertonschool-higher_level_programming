#!/usr/bin/node

if (process.argv.length > 3) {
  const numb = process.argv.map((element) => parseInt(element, 10));
  const s = numb.slice(2).sort((a, b) => a - b);
  console.log(s[s.length - 2]);
} else { console.log(0); }
