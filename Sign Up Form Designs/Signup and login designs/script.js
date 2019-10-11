var row=1;
var submit=docment.getElementById("submit");
submit.addEventListner("click",display);

function display()
{

			var Username = document.getElementById('user').value;
			var Email = document.getElementById('Email').value;
			var Pass=document.getElementById('Pass').value;
			var conpass=document.getElementById('conpass').value;
			var mobileno=document.getElementById('mobileno').value;


var display=document.getElementById("display");
var newRow=display.insertRow(row);
var cell1=newRow.insertCell(0);
var cell1=newRow.insertCell(1);
var cell1=newRow.insertCell(2);
var cell1=newRow.insertCell(3);
var cell1=newRow.insertCell(4);
cell1.innerHtml=Username;
cell2.innerHtml=Email;
cell3.innerHtml=Pass;

cell4.innerHtml=conpass;

cell5.innerHtml=mobileno;
row++;
}