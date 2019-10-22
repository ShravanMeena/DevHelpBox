const factory = document.getElementById("factory");
const score = document.getElementById("score");
const overlay = document.getElementById("overlay");
const timerDisplay = document.querySelector(".timer");
const scoreDisplay = document.querySelector(".results-score");
const keybaordHint = document.querySelector(".keyboard-hint");

let playing = false;
let ready = false;
let keyboardUsed = false;
let points = 0;
let active, filling, half, full, current, check, targetColor, currentTimer, timer;

let close = document.getElementById("popup-close");
let popup = document.getElementById("popup");

function openPopup() {
  popup.style.opacity = "1";
  overlay.style.opacity = "0.8";
  popup.style.display = "block";
  overlay.style.display = "block";
}

function closePopup() {
  popup.style.opacity = "0";
  overlay.style.opacity = "0";
  popup.style.display = "none";
  overlay.style.display = "none";
}

function startTimer() {
  factory.innerHTML = "";
  points = 0;
  score.innerHTML = points;
  addNewBottle();
  currentTimer = 60;
  playing = true;
  closePopup();
  timerDisplay.innerHTML = currentTimer;
  timer = setInterval(function() {
    updateTimer();
  }, 1000);
}

function updateTimer() {
    currentTimer--;
    timerDisplay.innerHTML = currentTimer;
    if (currentTimer === 0){
        playing = false;
        endGame();
    }
}

function endGame() {
    clearInterval(timer);
    scoreDisplay.innerHTML = points;
    popup = document.getElementById("results");
    close = document.getElementById("close-results");
    if (keyboardUsed) {
      keybaordHint.classList.add('hidden');
    }
    openPopup();
}

window.addEventListener('keyup', (e) => {
  if (e.key === 'a' || e.key === 's' || e.key === 'd') {
    keyboardUsed = true;
    if (e.key === 'a') {
      fillPaint('red');
    }
    else if (e.key === 's') {
      fillPaint('blue');
    }
    else if (e.key === 'd') {
      fillPaint('yellow');
    }
  }
});

function fillPaint(choice) {
  if (ready && playing) {
    if (choice === 'red') {
      current.classList.add('red');
      filling.classList.add('red');
    }
    else if (choice === 'blue') {
      current.classList.add('blue');
      filling.classList.add('blue');
    }
    else if (choice === 'yellow') {
      current.classList.add('yellow');
      filling.classList.add('yellow');
    }

    if (half.classList.contains('current')) {
      half.classList.remove('current');
      full.classList.add('current');
    }
    else if (full.classList.contains('current')) {
      if (half.classList.contains('red')) {
        if (full.classList.contains('red')) {
          filledColor = "red";
        }
        else if (full.classList.contains('blue')) {
          filledColor = "purple";
        }
        else if (full.classList.contains('yellow')) {
          filledColor = "orange";
        }
      }
      else if (half.classList.contains('blue')) {
        if (full.classList.contains('red')) {
          filledColor = "purple";
        }
        else if (full.classList.contains('blue')) {
          filledColor = "blue";
        }
        else if (full.classList.contains('yellow')) {
          filledColor = "green";
        }
      }
      else if (half.classList.contains('yellow')) {
        if (full.classList.contains('red')) {
          filledColor = "orange";
        }
        else if (full.classList.contains('blue')) {
          filledColor = "green";
        }
        else if (full.classList.contains('yellow')) {
          filledColor = "yellow";
        }
      }
      filling.classList.add('mixed-' + filledColor);
      if (targetColor === filledColor) {

        points += 100;

      }
      else {
        points -= 100;
      }
      full.classList.remove('current');
      active.classList.add('finished');
      ready = false;
      active.classList.remove('active');
      score.innerHTML = points;
      addNewBottle();
    }
    current = document.getElementsByClassName('current')[0];
  }
}

function addNewBottle() {
  const newBottle = document.createElement("div");
  const newHighlight = document.createElement("div");
  const newfilling = document.createElement("div");
  const newHalf = document.createElement("span");
  const newFull = document.createElement("span");

  // Define the target colours
  const targets = ["red","yellow","blue","purple","orange","green"];

  function randomiser(min, max) {
   let random_number = Math.random() * (max-min) + min;
    return Math.floor(random_number);
  }

  function random_target(array) {
    return array[randomiser(0,array.length)];
  }

  targetColor = random_target(targets);
  let newTarget = 'target-' + targetColor;

  // Define the class names
  newBottle.classList.add("bottle", "active", "start", newTarget);
  newHighlight.classList.add("highlight");
  newfilling.classList.add("filling");
  newFull.classList.add("full");
  newHalf.classList.add("half", "current");

  // Create new bottle and append each item
  factory.appendChild(newBottle);
  newBottle.appendChild(newHighlight);
  newBottle.appendChild(newfilling);
  newBottle.appendChild(newFull);
  newBottle.appendChild(newHalf);

  // Update variables
  active = factory.getElementsByClassName('active')[0];
  filling = active.getElementsByClassName('filling')[0];
  full = active.getElementsByClassName('full')[0];
  half = active.getElementsByClassName('half')[0];
  current = active.getElementsByClassName('current')[0];
  check = "";
  setTimeout(function() {
    document.getElementsByClassName('start')[0].classList.remove('start');
  }, 200);
  setTimeout(function(){
    ready = true;
  }, 1500);
}

document.addEventListener("DOMContentLoaded", function(event) {
  openPopup();
});