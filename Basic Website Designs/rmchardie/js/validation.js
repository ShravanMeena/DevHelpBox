function validate() {
  let emailValidation = document.getElementById("email");
  let validationMessage = document.getElementById("feedback");
  let mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  
  if(emailValidation.value.match(mailformat)) {
    emailValidation.classList.remove("is-invalid");
    emailValidation.classList.add("is-valid");
    validationMessage.classList.remove("invalid-feedback");
    validationMessage.classList.add("valid-feedback");
    validationMessage.innerHTML = "That's a fine looking e-mail address!";
  } else {
    emailValidation.classList.add("is-invalid");
    validationMessage.classList.add("invalid-feedback");
    validationMessage.innerHTML = "Please enter a valid e-mail address!";
  }
}

function validateMsg() {
  let msgValidation = document.getElementById("message");
  let validationMessage = document.getElementById("msgFeedback");
  if(msgValidation.value != "") {
    msgValidation.classList.remove("is-invalid");
    msgValidation.classList.add("is-valid");
    validationMessage.classList.remove("invalid-feedback");
    validationMessage.classList.add("valid-feedback");
    validationMessage.innerHTML = "That's a good query!";
  } else {
    msgValidation.classList.add("is-invalid");
    validationMessage.classList.add("invalid-feedback");
    validationMessage.innerHTML = "Please give a small description of your query!";
  }
}