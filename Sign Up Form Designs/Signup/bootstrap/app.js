$(document).ready(function(){

    $('.hamburger').on("click", function(){

        $('.menu').toggleClass('hidden');
        if ($('.menu').hasClass('hidden')) {
            $('span, i').show();
            $('.close').hide();
        } else {
            $('span, i').hide();
            $('.close').show();
        }

    });


//slideshow
    var slideIndex = 0;


function showSlides() {
    var i;
    var slides = document.getElementsByClassName("bg");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 4000); // Change image every 2 seconds
}

//new code
function showText(){

    var btn = document.getElementById('submit');
    btn.disabled = true;
    btn.innerHTML='Sending...';
}

});
