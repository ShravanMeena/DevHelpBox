/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/

var scores, roundScore, activePlayer, gamePlaying, prevRoll, winningScore;

init();

document.querySelector('.btn-score').addEventListener('click', function(){
  var scoreInput = document.getElementById('scoreInput').value;
  var validScore = parseInt(scoreInput);
  var isValid = isNaN(validScore);
  if (isValid || validScore === 0) {
    alert('Please enter a number.')
    init();
  } else {
      winningScore = validScore;
  }
   
});

document.querySelector('.btn-roll').addEventListener('click', function(){
  if (gamePlaying) {
    // 1. Random Number
    var dice1 = Math.floor(Math.random() * 6) + 1;
    var dice2 = Math.floor(Math.random() * 6) + 1;
    
    if(dice1 === 6 && prevRoll === 6) {
      nextPlayer();
    }
    // 2. Display Result
    var diceDOM1 = document.querySelector('.dice1');
    diceDOM1.style.display = 'block';
    diceDOM1.src = 'dice-' + dice1 + '.png';

    var diceDOM2 = document.querySelector('.dice2');
    diceDOM2.style.display = 'block';
    diceDOM2.src = 'dice-' + dice2+ '.png';

    // 3. Update the round score IF the rolled number was NOT a 1
    if (dice1 !== 1 && dice2 !== 1) {
      // Add Score
      roundScore += dice1 + dice2;
      document.querySelector('#current-' + activePlayer).textContent = roundScore;
    } else {
    //Next player
      nextPlayer();
    }
    prevRoll = dice1;
  }
});

document.querySelector('.btn-hold').addEventListener('click', function(){
  if (gamePlaying) {
    // Add current score to global score
    scores[activePlayer] += roundScore;

    // Update UI
    document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];
    // Check if player won the game
    if (scores[activePlayer] >= winningScore) {
      document.querySelector('#name-'+ activePlayer).textContent = 'Winner!';
      document.querySelector('.dice1').style.display = 'none';
      document.querySelector('.dice2').style.display = 'none';
      document.querySelector('.player-' + activePlayer +'-panel').classList.add('winner');
      document.querySelector('.player-' + activePlayer +'-panel').classList.remove('active');
      gamePlaying = false;
    } else {
    // Next Player 
      nextPlayer();
    }
  }
});

function nextPlayer(){
  //Next player
  activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
  roundScore = 0;

  document.getElementById('current-0').textContent = 0;
  document.getElementById('current-1').textContent = 0;

  document.querySelector('.player-0-panel').classList.toggle('active');
  document.querySelector('.player-1-panel').classList.toggle('active');

  // document.querySelector('.player-0-panel').classList.remove('active');
  // document.querySelector('.player-1-panel').classList.add('active');

 document.querySelector('.dice1').style.display = 'none';
 document.querySelector('.dice2').style.display = 'none';
}

document.querySelector('.btn-new').addEventListener('click', init);

function init(){
  scores = [0, 0];
  activePlayer = 0;
  roundScore = 0;
  gamePlaying = true;
  winningScore = 100;

  document.querySelector('.dice1').style.display = 'none';
  document.querySelector('.dice2').style.display = 'none';

  document.getElementById('score-0').textContent = '0';
  document.getElementById('score-1').textContent = '0';
  document.getElementById('current-0').textContent = '0';
  document.getElementById('current-1').textContent = '0';
  document.getElementById('name-0').textContent = 'Player 1';
  document.getElementById('name-1').textContent = 'Player 2';
  document.querySelector('.player-0-panel').classList.remove('winner');
  document.querySelector('.player-1-panel').classList.remove('winner');
  document.querySelector('.player-0-panel').classList.remove('active');
  document.querySelector('.player-1-panel').classList.remove('active');
  document.querySelector('.player-0-panel').classList.add('active');
  document.getElementById('scoreInput').value = '';
}





//document.querySelector('#current-' + activePlayer).textContent = dice;
//document.querySelector('#current-' + activePlayer).innerHTML = '<em>' + dice + '</em>';
//var x = document.querySelector('#score-0').textContent;