
function predict() {
//  var xhttp = new XMLHttpRequest();
  var path = document.getElementById("myfile").value;
  path = path.replace("C:\\fakepath\\", "");
  document.getElementById("two").innerHTML=path;

}//  url='http://127.0.0.1:5000/predict/'+path;
//  xhttp.open("GET", url, true);
//  xhttp.send();
