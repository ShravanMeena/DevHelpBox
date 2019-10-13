// Show an element
var show = function (elem) {
	elem.style.display = 'block';
};

// Hide an element
var hide = function (elem) {
	elem.style.display = 'none';
};

var toggle = function (elem) {

    console.log(elem)
	// Hide all elements
    hide(document.getElementById("about"));
    hide(document.getElementById("portf"));
    hide(document.getElementById("contact"));

	// Otherwise, show it
	show(document.getElementById(elem));

};

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
};

function URLStuff() {
    var location = getUrlVars()["x"]
    if (location != undefined) {
        hide(document.getElementById("about"));
        hide(document.getElementById("portf"));
        hide(document.getElementById("contact"));
	    // Otherwise, show it
        show(document.getElementById(location));
    }
}
document.addEventListener('DOMContentLoaded', function() {
    URLStuff();
}, false);
