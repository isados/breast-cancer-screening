
function predict() {
  var xhttp = new XMLHttpRequest();
  var path = document.getElementById("myfile").value;
  path = path.replace("C:\\fakepath\\", "");
  //document.getElementById("two").innerHTML=path;
  url='http://127.0.0.1:5000/predict/'+path;
  xhttp.open("GET", url, true);
  xhttp.send();

//  var yhttp = new XMLHttpRequest();
//  yhttp.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200) {
//	 var myObj = this.responseText;

//     var new_msg = '<div class="chat friend"><div class="user-photo"><img src="bot.png"></div><p class="chat-message">'+myObj.reply+'</p></div>';
	// modconf=Math.round(myObj.intent.confidence*100)
//	 document.getElementById("result").innerHTML = "Confidence&nbsp;&nbsp;   <span style='font-size: 20px;color:red'>"+myObj +"%</span>";
   //document.getElementById("intent").innerHTML = "Intent    &nbsp;&nbsp;<span style='font-size: 20px;color:red'>"+modintent+"</span>";
   //document.getElementById("sentiment").innerHTML = "Sentiment    &nbsp;&nbsp;<span style='font-size: 20px;color:red'>"+sentiment+"</span>";
//};
}//
