#!/usr/bin/node

const args = process.argv[2];
if (!args) {
  console.log('Missing size');
} else if (isNaN(args)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < args; i++) {
    line += '+';
  }
  for (let j = 0; j < args; j++) {
    console.log(line);
  }
}
