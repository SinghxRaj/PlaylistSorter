/**
 * sort.js provides functionality for the playlist card when it
 * is clicked in sort.html.
 */
"use strict";

window.addEventListener("load", init);

/**
 * Adds a click event listener to the playlistCard in "sort.html"
 * which calls toggleTracks.
 */
function init() {
  let playlistCard = document.getElementById("playlist-container");
  playlistCard.addEventListener("click", toggleTracks);
}

/**
 * Toggles the hide class for the container that contains the tracks.
 */
function toggleTracks() {
  let trackContainer = document.getElementById("track-container");
  let playlistCard = document.getElementById("playlist-container");
  trackContainer.classList.toggle("hidden");
  playlistCard.classList.toggle("expand");
}