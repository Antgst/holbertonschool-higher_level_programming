#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.legth < 2) {
  console.log(0);
} else {
  let max = args[0];
  let second = Number.MAX_SAFE_INTEGER;

  for (let i = 1; i < args.length; i++) {
    if (args[i] > max) {
      second = max;
      max = args[i];
    } else if (args[i] > second && args[i] < max) {
      second = args[i];
    }
  }

  console.log(second);
}
