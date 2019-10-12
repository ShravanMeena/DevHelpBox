		
	//Typewriter Effect Script
	$('#part-one h1').typeIt({
		 strings: ["Hi I am Sahil Singh", "I am a Frontend Engineer", "Scroll Down to Know More"],
		 speed: 120,
		 autoStart: false
	});
		
	//Smooth scroll
	$('a').click(function(){
		$('html, body').animate({scrollTop: $( $(this).attr('href') ).offset().top}, 500);
		return false;
	});	
		
	// Progress bar Script 
	$(window).scroll(function () {
		console.log($(window).scrollTop());
		var topDivHeight1 = $("#part-one").height();
		var topDivHeight2 = $("#part-two").height();
		var topDivHeight3 = $("#part-three").height();
		var viewPortSize = $(window).height();
				
		var triggerAt = 310;
		var triggerHeight = ((topDivHeight1 + topDivHeight2 + topDivHeight3) - viewPortSize) + triggerAt;

		if ($(window).scrollTop() >= triggerHeight) {		
			$('.div1').css('width','90%');
			$('.div2').css('width','80%');
			$('.div3').css('width','90%');
			$('.div4').css('width','70%');				
		}	
	});
	
	//Resume Download button pop-up
	$(document).ready(function () {   
		$("#myBtn").click(function(){
			 $('#myModal').modal('show');
		});
	});
	
	//Portfolio Filter		
	$(document).ready(function(){
		$(".filter-button").click(function(){
			var value = $(this).attr('data-filter');				
			if(value == "all")
			{
				$('.filter').show('1000');
			}
			else
			{
				$(".filter").not('.'+value).hide('3000');
				$('.filter').filter('.'+value).show('3000');					
			}
		});		
		if ($(".filter-button").removeClass("active"))
		{
			$(this).removeClass("active");
		}
			$(this).addClass("active");
	});
			