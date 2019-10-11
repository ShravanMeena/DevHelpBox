function ValidateForm() {
	var email=document.getElementById("email");
	var username=document.getElementById("username");

	
	var letter=/^[a-z0-9]+$/;
	
	var f=0;
	if (email.value.length==0){
		email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Email can't be blank";
		}else if(email.value.indexOf('@',0)<=0){
		email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Invalid @ position";
		}else if(email.value.indexOf('.',0)<0){
			email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Invalid . position";
		}else if(emailvalid()==false){
			email.className="wrong-input";
		email.nextElementSibling.innerHTML="  Enter valid E-mail id";
		}
		else if(f==1){
		name.className="form-control";
		name.nextElementSibling.innerHTML="";
		
	}else{
		email.className="form-control";
		email.nextElementSibling.innerHTML="";
		f=f+1;
	}
	if (password.value.length==0){
		password.className="wrong-input";
		password.nextElementSibling.innerHTML="Password can't be blank";
	}
	else if(f==2){
		password.className="form-control";
		password.nextElementSibling.innerHTML="";
		
		}else{
		password.className="form-control";
		password.nextElementSibling.innerHTML="";
		f=f+1;
	}
	
	if (f==2){
		valid=true;
	}else{valid=false;}
	return valid;
}
	function emailvalid(){
		var emailfilter=/^\w+[\+\.\w-]*@([\w-]+\.)*\w+[\w-]*\.([a-z]{2,4}|\d+)$/i
var b=emailfilter.test(email.value);
if(b==false)
{

		return false;

}
	}
	