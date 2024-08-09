let on = localStorage.getItem("on") === "true";
let swipeSound = new Audio(
  "https://zvukipro.com/index.php?do=download&id=16753"
);

const bulbEL = document.getElementById("bulb");
const toggleEl = document.getElementById("toggle");
const btnEl = toggleEl.querySelector("button");

function toggleLight(on) {
  document.body.classList.toggle("on", on);
  bulbEL.classList.toggle("bulb_on", on);
  toggleEl.classList.toggle("toggle_on", on);
}

function playSwipeSound() {
  swipeSound.play();
}

btnEl.addEventListener("click", () => {
  on = !on;
  toggleLight(on);
  localStorage.setItem("on", on);
  playSwipeSound();
});

toggleLight(on);


document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.toggle__btn');
    const room = document.querySelector('.room5-walls');
    const clock = document.querySelector('.clock');

    toggleButton.addEventListener('click', function() {
        room.classList.toggle('on');
        clock.classList.toggle('clock_on');
    });
});