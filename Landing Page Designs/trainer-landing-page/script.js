

const menu = document.querySelector('.menu');
const icon = document.querySelector('.navbar__icon');
const humburger = document.querySelector('.navbar__humburger');
const list = document.querySelectorAll('.menu__item');
const listItems = Array.from(list);

icon.addEventListener('click', () => {
    menu.classList.toggle('menu-show');
    humburger.classList.toggle('humburger-click');
});

// listItem.addEventListener('click', () => {
//     menu.classList.toggle('menu-show');
//     humburger.classList.toggle('humburger-click');
// });

for(item of listItems){
    item.addEventListener('click', ()=> {
        menu.classList.toggle('menu-show');
        humburger.classList.toggle('humburger-click');
    })
}





