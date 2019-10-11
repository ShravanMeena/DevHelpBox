function ValidateForm() {
	var name=document.getElementById("name");
	var email=document.getElementById("email");
	var username=document.getElementById("username");
	var password=document.getElementById("password");
	var confirm_password=document.getElementById("confirm_password");
	var age=document.getElementById("age");
	removeMessage();
	// pass();
	if (name.value.length==0){
		name.className="wrong-input";
		name.nextElementSibling.innerHTML="  name can't be blank";
		valid=false;}
	else{
		name.className="form-control";
		name.nextElementSibling.innerHTML="";
		valid=true;
	}
	if(valid==true){if (email.value.length==0){
		email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Email can't be blank";
		valid=false;}else if(email.value.indexOf('@')<=0){
		email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Invalid @ position";
		valid=false;
	}else if((email.charAt(email.length-4)!=".") || (email.charAt(email.length-3)!=".")){
		email.nextElementSibling.innerHTML="  Invalid . position";
		valid=false;
	}else{
		email.className="form-control";
		email.nextElementSibling.innerHTML="";
		valid=true;
	}}
	
	if (valid==true){if (username.value.length==0){
		username.className="wrong-input";
		username.nextElementSibling.innerHTML="  Username can't be blank";
		valid=false;}else{
		username.className="form-control";
		username.nextElementSibling.innerHTML="";
		valid=true;
	}}

	
	if (valid==true){if (password.value.length<6){
		password.className="wrong-input";
		password.nextElementSibling.innerHTML="  password can't be less than 6";
		valid=false;
	}else{
		password.className="form-control";
		password.nextElementSibling.innerHTML="";
		valid=true;
	}}
	

	
	if (valid==true){if (password.value!=confirm_password.value){
		confirm_password.className="wrong-input";
		confirm_password.nextElementSibling.innerHTML="  password does not match";
		valid=false;
	}else{
		confirm_password.className="form-control";
		confirm_password.nextElementSibling.innerHTML="";
		valid=true;
	}}
	


	 
	if (valid==true){if (age.value<18 || age.value>90){
		age.className="wrong-input";
		age.nextElementSibling.innerHTML="  Age should be in between 18-90";
		valid=false;
	 }else{
		age.className="form-control";
		age.nextElementSibling.innerHTML="";
		valid=true;
	}}


	if (valid==true){if (gender.value == "gender"){
		gender.className="wrong-input";
		gender.nextElementSibling.innerHTML=" Select the Gender";
		valid=false;
	 }else{
		gender.className="form-control";
		gender.nextElementSibling.innerHTML="";
		valid=true;
	}}

	if (valid==true){if (colour.value == "favourite_colour"){
		colour.className="wrong-input";
		colour.nextElementSibling.innerHTML=" Select your Favourite colour";
		valid=false;
	 }else{
		colour.className="form-control";
		colour.nextElementSibling.innerHTML="";
		valid=true;
	}}

	return valid;

}
function removeMessage(){
	var errorinput=document.querySelectorAll(".wrong-input");
	[].forEach.call(errorinput, function(el){
		el.classList.remove("wrong-input");
	});
	var errorpara=document.querySelectorAll(".error");
	[].forEach.call(errorinput, function(el){
		el.innerHTML="";
	});
}

function email_check(){
	if(email.indexOf("@")<=0){
		email.nextElementSibling.innerHTML="  Invalid @ position";
		valid=false;
	}
	else if((email.charAt(email.length-4)!=".") || (email.charAt(email.length-3)!=".")){
		email.nextElementSibling.innerHTML="  Invalid . position";
		valid=false;
	}
}