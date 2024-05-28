#!/usr/bin/node

// import the module
const request = require('request');

// The first argument is the URL to request (GET)
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
