#!/usr/bin/node
const request = require('request');
const url = "https://swapi-api.hbtn.io/api/films/:id" + process.argv[2];
let resultDict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultDict = JSON.parse(body);
    console.log(resultDict.title);
  }
});
