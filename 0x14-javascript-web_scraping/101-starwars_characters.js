#!/usr/bin/node

// Require the 'request' module
const request = require('request');

// Get movieID from command line args
const movieId = process.argv[2];
// Get the URL for SWAPI film API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make request to the SWAPI film API
request(apiUrl, function (error, response, body) {
  if (error) {
    // Check for errors in the request
    console.error(error);
  } else if (response.statusCode === 200) {
    // If statusCode is 200 (OK), proceed

    // Parse the JSON body response
    const movieData = JSON.parse(body);

    // Check if characters property exists and is an array
    if (
      Array.isArray(movieData.characters) &&
      movieData.characters.length > 0
    ) {
      // Iterate over each character in the movie
      for (let i = 0; i < movieData.characters.length; i++) {
        // Get the URL for each character
        const characterUrl = movieData.characters[i];

        // Make a request to fetch information about each character
        request(characterUrl, function (charError, charResponse, charBody) {
          if (charError) {
            // Check for errors in the request for character details
            console.error(charError);
          } else if (charResponse.statusCode === 200) {
            // If statusCode is 200 (OK), parse and print the character name
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            // If the response status code is not 200, output an error message
            console.log(`Error code: ${charResponse.statusCode}`);
          }
        });
      }
    } else {
      // If characters array is empty or does not exist, output an error message
      console.log(
        'Invalid movie ID or no characters found for the given movie.'
      );
    }
  } else {
    // If the response status code is not 200, output an error message
    console.log(`Error code: ${response.statusCode}`);
  }
});
