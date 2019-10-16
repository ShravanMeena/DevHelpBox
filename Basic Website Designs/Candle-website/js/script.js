$(function () {
    new WOW().init();

    /*************************************************************************
                                WORK SECTION
    *************************************************************************/
    $('#work').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        // other options
        gallery: {
            enabled: true
        },
        zoom: {
            enabled: true, // By default it's false, so don't forget to enable it

            duration: 300, // duration of the effect, in milliseconds
            easing: 'ease-in-out', // CSS transition easing function

            // The "opener" function should return the element from which popup will be zoomed in
            // and to which popup will be scaled down
            // By defailt it looks for an image tag:
            opener: function (openerElement) {
                // openerElement is the element on which popup was initialized, in this case its <a> tag
                // you don't need to add "opener" option if this code matches your needs, it's defailt one.
                return openerElement.is('img') ? openerElement : openerElement.find('img');
            }
        }
    });

   
    
    $("a.smooth-scroll").click(function(event){
        //prevents to perform the default operation
        event.preventDefault();
        
        var section = $(this).attr("href");
        $("html, body").animate({
            scrollTop: $(section).offset().top-69,
        }, 1250, "easeInOutExpo");
    });
   

});