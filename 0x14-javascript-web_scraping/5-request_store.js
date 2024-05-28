#!/usr/bin/node

// import the mode
const fs = require('fs');
const request = require('request');

// The first argument is the url
const url = process.argv[2];

// The second argument is the file path
const file = process.argv[3];

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf-8', error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
