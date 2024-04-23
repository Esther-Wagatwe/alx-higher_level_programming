#!/usr/bin/node

const Size = parseInt(process.argv[2]);

if (!isNaN(Size)) {
  for (let i = 0; i < Size; i++) {
    console.log('X'.repeat(Size));
  }
} else {
  console.log('Missing size');
}
