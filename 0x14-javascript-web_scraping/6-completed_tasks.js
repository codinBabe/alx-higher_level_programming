#!/usr/bin/node

// import the mode
const request = require('request');

// The first argument is the url
const url = process.argv[2];

const content = {};

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // Check for errors during the request
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in content)) {
          content[userid] = 0;
        }
        content[userid] += 1;
      }
    });
    console.log(content);
  }
});
