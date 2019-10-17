const listenerEvent = () => {
	const btnPlay = document.getElementsByClassName('play')[0];
	btnPlay.addEventListener('click', startSlider);
}

const displayScore = () => {
	const scoreResultElm = document.getElementsByClassName('scoreResult')[0];
	scoreResultElm.classList.remove('d-none');
	const arrListEl = document.getElementsByClassName('screen-wrapper');
	setTimeout(function(){
		const arrList = Array.prototype.map.call( arrListEl, el => parseInt(el.getAttribute('data-val')));
		let res = 0;
		const list1 = arrList.pop();
		if(arrList.includes(list1) || arrList[0] === arrList[1]) {
			res = 60;
			if( list1 === arrList[0] && list1 === arrList[1] ) {
				res = 100;
				if(list1 === 6) {
					res = "YEAAAYYYY Jackpot!!!!...."
				}
			}
		}
		const scoreResNum = scoreResultElm.getElementsByClassName('score')[0];
		scoreResNum.innerHTML = res;
		scoreResNum.classList.add('zoom');
		setTimeout(function(){
			scoreResNum.classList.remove('zoom');
		}, 500);
	}, 1000);

}

const checkAllStopBtn = () => {
	const arrBtnStop = $('.screen-wrapper .stop.is-disabled');
	if(arrBtnStop.length  === 3){
		$('.bottom-bar .play').removeClass('is-disabled');
		displayScore();
	}
}

const startSlider = () => {
	$('.play').addClass('is-disabled');	// disabled button start
	$('.scoreResult').addClass('d-none');

	//configuration
	const width = 150;						//image wrapper width 150px
	const animationSpeed = 500;		//slide speed
	const paused = 500;						//pause before change image
	
	//DOM selector
	const $slider = $('.slider');
	const $slideContainer = $slider.find('.slides');

	//slider run
	$slideContainer.each(function(el, idx){
		let currentSlide = 1;					//variable for buffering slider image
		$(this).addClass("slide-run");
		const $slides = $(this).find('.slide');
		const $btnStop = $(this).closest('.screen-wrapper').find('.stop');

		$btnStop.removeClass('is-disabled');

		const interval = setInterval(() => {
			$(this).animate({'margin-top': '-='+width}, animationSpeed, () => {
				$(this).closest('.screen-wrapper').attr('data-val', currentSlide);
				currentSlide++;				
				if(currentSlide === $slides.length) {			//reset to 1st image
					currentSlide = 1;
					$(this).css('margin-top', 0);
				}
			});
		}, paused);

		$btnStop.bind('click', (ev) => {
			clearInterval(interval);
			const isRun = $(this).closest('.screen-wrapper').find('.slide-run');
			if (isRun) isRun.removeClass('slide-run');
			$(this).closest('.screen-wrapper').find('.stop').addClass('is-disabled');
			checkAllStopBtn();
		});
	})
}

document.addEventListener("DOMContentLoaded", listenerEvent);