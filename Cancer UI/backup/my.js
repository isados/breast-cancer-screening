
function predict() {
  var xhttp = new XMLHttpRequest();
  var path = document.getElementById("myfile").value;
  path = path.replace("C:\\fakepath\\", "");
  //document.getElementById("two").innerHTML=path;
  document.getElementById("lll").innerHTML=path;
  url='http://127.0.0.1:5000/predict/'+path;
  xhttp.open("GET", url, true);
  xhttp.send();
  var xhttpans = new XMLHttpRequest();
  xhttpans.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {


//     var new_msg = '<div class="chat friend"><div class="user-photo"><img src="bot.png"></div><p class="chat-message">'+this.responseText+'</p></div>';


//	 document.getElementById("chat_logs").innerHTML += (new_msg);
	 document.getElementById("kkk").innerHTML = this.responseText;
    }
  };
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

function getResult() {

  var xhttpans = new XMLHttpRequest();
  xhttpans.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {


//     var new_msg = '<div class="chat friend"><div class="user-photo"><img src="bot.png"></div><p class="chat-message">'+this.responseText+'</p></div>';


//	 document.getElementById("chat_logs").innerHTML += (new_msg);
	 document.getElementById("kkk").innerHTML = this.responseText;
    }
  };
  url='http://127.0.0.1:5000/haans/';
  xhttpans.open("GET", url, true);
  xhttpans.send();

  document.getElementById("msg").value = "";
}
