/**
 * Selection.js will provide functionality to the selection.html
 * template. It will keep track of which playlist the user is
 * selecting to sort.
 */
"use strict";

window.addEventListener("load", init);

/**
 * Adds event listeners to all playlists which
 * will call selectedPlaylist when clicked.
 */
function init() {
  let playlistCards = document.querySelectorAll(".playlist-card");
  for (let i = 0; i < playlistCards.length; i++) {
    playlistCards[i].addEventListener("click", function(e) {
      selectedPlaylist(e.target);
    })
  }
}

/**
 * Selects the playlist that was clicked on and unselected
 * any previous playlist that was selected
 *
 * @param {HTMLElement} elem - the element that was selected
 */
function selectedPlaylist(elem) {
  let prevSelectedPlaylist = document.querySelector(".selected-card");
  if (prevSelectedPlaylist) {
    prevSelectedPlaylist.classList.remove("selected-card");
  }
  if (elem.parentElement.nodeName === "LI") {
    elem = elem.parentElement;
  }
  elem.classList.add("selected-card");
  document.getElementById("selected-playlist").value = elem.id;
  let nextBtn = document.getElementById("next-btn");
  if (nextBtn.classList.contains("button-disabled")) {
    nextBtn.classList.remove("button-disabled");
    nextBtn.classList.add("button-enabled");
    document.getElementById("next-btn").disabled = false;
  }
}