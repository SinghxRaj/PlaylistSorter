/*
  owner_sort.js provides functionality for the form in owner_sort.html. It will hide
  the input field for putting the name of the playlist if they choose not to create a
  new playlist.
*/
"use strict";

window.addEventListener("load", index);

/**
 * Adds a change event listener to the select dropdown `playlist-type`
 * which calls toggleInput when the value changes and a change event listener
 * on the input field in owner_sort.html which calls enableBtn when the input value
 * changes.
 */
function index() {
  let playlistType = document.getElementById("playlist-type");
  playlistType.addEventListener("change", toggleInput);
  let playlistName = document.getElementById("playlist-name");
  playlistName.addEventListener("input", enableBtn);

}

/**
 * Hides the `playlist-name` input field and label when the user
 * does not want to create a new playlist
 */
function toggleInput() {
  if (this.value !== "Create New Playlist") {
    document.getElementById("new-playlist-container").classList.add("hidden");
    document.getElementById("playlist-name").value = "";
  } else {
    document.getElementById("new-playlist-container").classList.remove("hidden");
  }
  enableBtn();
}

/**
 * Enable next button if the input field is not empty.
 */
function enableBtn() {
  let playlistName = document.getElementById("playlist-name");
  let newPlaylistContainer = document.getElementById("new-playlist-container");
  let nextBtn = document.getElementById("next-btn");
  if (playlistName.value === "" && !newPlaylistContainer.classList.contains("hidden")) {
    nextBtn.disabled = true;
    nextBtn.classList.add("button-disabled");
    nextBtn.classList.remove("button-enabled");
  } else {
    nextBtn.disabled = false;
    nextBtn.classList.remove("button-disabled");
    nextBtn.classList.add("button-enabled");
  }
}