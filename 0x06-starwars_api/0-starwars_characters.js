#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// The base URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Make a request to the API for the film data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Function to fetch and print character names
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          reject(new Error(`Failed to fetch data. Status code: ${response.statusCode}`));
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      });
    });
  };

  // Fetch and print all character names in order
  (async () => {
    for (const url of characterUrls) {
      try {
        await fetchCharacter(url);
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  })();
});
