


function input(){

var a= document.getElementById("card-holder").value;
document.getElementById("card-name").innerHTML=a;
var b= document.getElementById("card-number").value;
if(b> 9999999999999999){
    alert("You are in earth !! not mars..")
    window.location.reload();
}
else{
 document.getElementById("card-display").innerHTML=b;
}
var c= document.getElementById("card-expiration-month").value;
document.getElementById("card-month").innerHTML=c;
var d= document.getElementById("card-expiration-year").value;
document.getElementById("card-year").innerHTML=d;
var e= document.getElementById("card-cvv").value;
document.getElementById("card-cvv-display").innerHTML=e;

}