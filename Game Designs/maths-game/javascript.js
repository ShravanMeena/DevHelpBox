var playing=false;
var score;
var timeremaining=60;
var action;
var correctanswer;
document.getElementById("startreset").onclick=function(){
    if(playing==true){
        location.reload();
    }else{
        hide("gameover")
        playing=true;
        score=0;
        document.getElementById("scorevalue").innerHTML=score;
        document.getElementById("timeremaining").style.display="block";

        timeremaining=60;
        document.getElementById("timeremainingvalue").innerHTML=timeremaining;

        startCountdown();
        generateQA();


        document.getElementById("startreset").innerHTML="Reset Game";
    }
}
for(i=1;i<5;i++){
    document.getElementById("box"+i).onclick=function(){
        if(playing=true){
            if(this.innerHTML==correctanswer){
            score++;
            document.getElementById("scorevalue").innerHTML=score;
            hide("wrong");
            show("correct");
            setTimeout(function(){hide("correct");},1000);
            generateQA();
            }else{
                hide("correct");
                show("wrong");
                setTimeout(function(){
                hide("wrong");},1000
                )
            }
        }
    }

}
function startCountdown(){
    action=setInterval(function(){
        timeremaining-=1;
        document.getElementById("timeremainingvalue").innerHTML=timeremaining;
        if(timeremaining==0){
            clearInterval(action)
            document.getElementById("gameover").innerHTML="<p>Game over!</p><p>Your score is "+score+".</p>";
            show("gameover");
            hide("timeremaining");
            hide("correct");
            hide("wrong");
            playing=false;
            document.getElementById("startreset").innerHTML="Start Game";
        }


    },1000)


}
function hide(Id){
    document.getElementById(Id).style.display="none";
}
function show(Id){
    document.getElementById(Id).style.display="block";
}
function generateQA(){
    var x=Math.round(Math.random()*9)+1;
    var y=Math.round(Math.random()*9)+1;
    correctanswer=x*y;
    document.getElementById("question").innerHTML=x+"X"+y;
    var correctpos=Math.round(Math.random()*3)+1;
    document.getElementById("box"+correctpos).innerHTML=correctanswer;
    var answers=[correctanswer];
    for(i=1;i<5;i++){
        if(i!=correctpos){
            var wrongans;
            do{
                wrongans=(Math.round(Math.random()*9)+1)*(Math.round(Math.random()*9)+1);}
            while(answers.indexOf(wrongans)>-1)
            document.getElementById("box"+i).innerHTML=wrongans;
            answers.push(wrongans);
            }


        }
    }
