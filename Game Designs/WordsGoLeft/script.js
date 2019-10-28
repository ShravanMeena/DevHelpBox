const words = ["about", "above", "add", "after", "again", "air", "all", "almost", "along", "also", "always", "America", "an", "and", "animal", "another", "answer", "any", "are", "around", "as", "ask", "at", "away", "back", "be", "because", "been", "before", "began", "begin", "being", "below", "between", "big", "book", "both", "boy", "but", "by", "call", "came", "can", "car", "carry", "change", "children", "city", "close", "come", "could", "country", "cut", "day", "did", "different", "do", "does", "don't", "down", "each", "earth", "eat", "end", "enough", "even", "every", "example", "eye", "face", "family", "far", "father", "feet", "few", "find", "first", "follow", "food", "for", "form", "found", "four", "from", "get", "girl", "give", "go", "good", "got", "great", "group", "grow", "had", "hand", "hard", "has", "have", "he", "head", "hear", "help", "her", "here", "high", "him", "his", "home", "house", "how", "idea", "if", "important", "in", "Indian", "into", "is", "it", "its", "it's", "just", "keep", "kind", "know", "land", "large", "last", "later", "learn", "leave", "left", "let", "letter", "life", "light", "like", "line", "list", "little", "live", "long", "look", "made", "make", "man", "many", "may", "me", "mean", "men", "might", "mile", "miss", "more", "most", "mother", "mountain", "move", "much", "must", "my", "name", "near", "need", "never", "new", "next", "night", "no", "not", "now", "number", "of", "off", "often", "oil", "old", "on", "once", "one", "only", "open", "or", "other", "our", "out", "over", "own", "page", "paper", "part", "people", "picture", "place", "plant", "play", "point", "put", "question", "quick", "quickly", "quite", "read", "really", "right", "river", "run", "said", "same", "saw", "say", "school", "sea", "second", "see", "seem", "sentence", "set", "she", "should", "show", "side", "small", "so", "some", "something", "sometimes", "song", "soon", "sound", "spell", "start", "state", "still", "stop", "story", "study", "such", "take", "talk", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "thought", "three", "through", "time", "to", "together", "too", "took", "tree", "try", "turn", "two", "under", "until", "up", "us", "use", "very", "walk", "want", "was", "watch", "water", "way", "we", "well", "went", "were", "what", "when", "where", "which", "while", "white", "who", "why", "will", "with", "without", "word", "work", "world", "would", "write", "year", "you", "young", "your"];

const typenWords = 0;

const input = $("input");
const gamePane = $(".gamePane");
const activeWords = [];
const startTime = new Date().getTime();

let wordsGotten = 0;
let xStep = gamePane.width() / 8;
let wpm = 60;
let millisInMinute = 60000;
let interval = setInterval(animate, millisInMinute/wpm);
setTimeout(increaseWpm, 2000);

input.on("change input keydown",function(evt){
    if (evt.keyCode == 32) {
        activeWords.forEach(word => {
            if (word.text() == input.val().replace(" ","")) {
                word.remove();
                wordsGotten++;
                activeWords.find((el, index) => {
                    if (word == el) {
                        activeWords.splice(index, 1);
                    }
                });
            }
        });
        input.val("");
    }
});

function addWord() {
    let word = getWord();
    let yPos = Math.round(Math.random() * gamePane.height());

    let span = $(`<span class="word">${word}</span>`, {
    }).css({right: 15,top: yPos,transition: "all 1s linear"})
    .appendTo(gamePane);

    activeWords.push(span);
}

function getWord() {
    return words[Math.floor(Math.random() * words.length)];
}

function animate() {
    addWord();
    activeWords.forEach(word => {
        const pos = word.position();
        word.css({left: pos.left - xStep});
        
        if (pos.left < xStep) {
            loseLive(word);
        }
    });
}

function loseLive(word) {
    word.remove();

    if ($(".live").length == 1) {
        activeWords.forEach(word => word.remove());
        clearInterval(interval);
        let timeDiff = (new Date().getTime() -  startTime) / millisInMinute;
        console.log(wordsGotten);
        console.log(timeDiff);        

        $(".gamePane").html(`<h1 style="margin: 0;">${wordsGotten/timeDiff} wpm<h1>`);
    }

    $(".live").first().remove();
    activeWords.find((el, index) => {
        if (word == el) {
            activeWords.splice(index, 1);
        }
    });
}

function increaseWpm() {
    console.log("IncreaseWpm");
    
    wpm++;
    $(".speedNumber").text(wpm);
    clearInterval(interval);
    if (!$(".live").length == 0) {
        interval = setInterval(animate,millisInMinute / wpm);
        setTimeout(increaseWpm, 2000);
    }
}