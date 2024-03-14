#!/usr/bin/node

const fs = require('fs');

// Extract file paths from command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read the content of the source files
const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

// Concatenate the content of the source files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFilePath, concatenatedContent);
