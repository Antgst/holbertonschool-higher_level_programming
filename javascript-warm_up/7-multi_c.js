#!/usr/bin/node

const occurences = parseInt(process.argv[2]);

if (isaNan(occurences)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
}
