function startTime()
{
var today=new Date()
var hr=today.getHours()
var min=today.getMinutes()
var sec=today.getSeconds()
var ap="AM";

//to add AM or PM after time
// Add IF statement using the above declared variables to display your clock in AM and PM

if(hr>11) ap="PM";
if(hr>12) hr=hr-12;
if(hr==0) hr=12;

//to add a zero in front of numbers<10

min=checkTime(min)
sec=checkTime(sec)

document.getElementById('clock').innerHTML=hr+":"+min+":"+sec+" "+ap
t=setTimeout('startTime()', 500)
}

function checkTime(i)
{
if (i<10)
{ i="0" + i}
return i
}
// Added window prompt to call the onload event to display the time when page loads
window.onload=startTime;
