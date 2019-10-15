function valid(){
   if(document.getElementById("username").value=="")
   {
        alert("Please enter username");
        document.getElementById("username").focus();
        return false;
   }
   if(document.getElementById("password").value=="")
   {
        alert("Please enter password");
        document.getElementById("password").focus();
        return false;
   }
}