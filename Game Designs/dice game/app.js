/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/






var scores, roundScore, activePlayer, gamePlaying;

init();

var roll = document.querySelector('.btn-roll'); // button roll
var hold = document.querySelector('.btn-hold'); // button hold
var newBtn = document.querySelector('.btn-new'); // button new
//var currentScore = document.querySelector('#current-' + activePlayer);

roll.addEventListener('click', function(){

    if(gamePlaying){
        var dice = Math.floor(Math.random() * 6) + 1; // random number store in dice variable
        var diceDom = document.querySelector('.dice');
        diceDom.style.display = 'block';
        diceDom.src = 'dice-' + dice + '.png'; 
    
        if(dice !== 1){ // if the dice value is not the 1 then continue
            roundScore += dice; // dice value store in roundScore
            document.querySelector('#current-' + activePlayer).textContent = roundScore; // current active value is equal to roundscore
            
        }
        else{ // if the dice value is 1 the contiue
            nextPlayer(); // next player turn
        }
    }


});


hold.addEventListener('click', function(){ // clicked on hold button

    if(gamePlaying){ // if gamePlaying is true then continue 
        scores[activePlayer] += roundScore; // current player score is equal to round score

        // update user inerface

        document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer]; // update current player score

        //check if the player won the game

        var score = document.querySelector(".score").value;
        var winScore;

        if(score){
            winScore = score;
        }else{
            winScore = 10;
        }

        if(scores[activePlayer] >= winScore){ // if the player score is reached 50 or more then continue
            document.querySelector('#name-' + activePlayer).textContent = 'winner';
            document.querySelector('.dice').style.display = 'none';
            document.querySelector('.player-' + activePlayer + '-panel').classList.toggle('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');

            gamePlaying = false;  // game is begian stop after a player reach score 50;
            //roll.style.display = 'none';
            //hold.style.display = 'none';
        }
        else{
            // next player
            nextPlayer();
        }
    }
    
});


function nextPlayer(){
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0; // if active player === 0 then activeplayer = 1 else activeplayer = 0
    roundScore = 0 
    document.querySelector('#current-0').textContent = 0;
    document.querySelector('#current-1').textContent = 0;

    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');

    document.querySelector('.dice').style.display = 'none';
}

function init(){
    gamePlaying = true;

    scores = [0,0];
    roundScore = 0;
    activePlayer = 0; // game start from player 0
    document.querySelector('.dice').style.display = 'none';

    document.querySelector('#name-0').textContent = 'Player 1';
    document.querySelector('#name-1').textContent = 'Player 2';
    document.querySelector('#current-0').textContent = 0;
    document.querySelector('#current-1').textContent = 0;
    document.querySelector('#score-0').textContent = 0;
    document.querySelector('#score-1').textContent = 0;
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');


    //roll.style.display = 'block';
    //hold.style.display = 'block';
}

newBtn.addEventListener('click', init); // if clicked on new game then game start again.


