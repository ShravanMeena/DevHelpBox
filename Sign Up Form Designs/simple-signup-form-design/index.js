// Made by @Aldhanekaa, copyright 2020


// selecting all inputs
const inputs = document.querySelectorAll('.input');

// submit button
const submitBtn = document.querySelector('.submitBtn');


// regex for email
const reg = /^\w.*@.*[.].*/i

// if submit button is on click, run this below:
submitBtn.addEventListener('click', function () {
    // here we iterate all inputs
    inputs.forEach(element => {
        // here we trim the input value
        const ev = element.value.trim();

        // here we check if the empty or not by calling function
        checkIfInputEmpty(ev, element)
        if (element.classList.contains('email')) {
            // here we check the input email value, if the email value is valid email it return true to this variable
            const result = reg.test(ev);

            // if result is false we run this code below
            if (!result) {
                element.style.border = '1px solid red'
                element.nextElementSibling.textContent = 'please enter valid email address';
                makeNextElementSiblingEmpty(element)
            }
        }
    });

})

// here we change the status textContent (red text or warning text) become empty
function makeNextElementSiblingEmpty(element) {
    // so here we must wait 5 seconds, after that we change the status textContent (red text or warning text) become empty
    setTimeout(() => {
        element.style.border = '0px solid transparent'
        element.nextElementSibling.textContent = '';
    }, 5000);
}

// here we check if the input empty or not
function checkIfInputEmpty(ev, element) {
    // if empty then we run this below
    if (ev == '') {
        element.style.border = '1px solid red'
        element.nextElementSibling.textContent = 'please fill this input';
        // here we change the status textContent (red text or warning text) become empty by calling function
        makeNextElementSiblingEmpty(element);
    }
}