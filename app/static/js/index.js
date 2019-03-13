let loaded_sec_1=false;
let loaded_sec_2=false;
let loaded_sec_3=false;

jQuery(window).scroll(function() {

var bottom_position = $(document).height() - ($(window).scrollTop() + $(window).height());

if (bottom_position<-300 && loaded_sec_1==false){
refresh('/container_explain','section-1-container')
loaded_sec_1=true;


}



if (bottom_position<-600 && loaded_sec_2==false){

loaded_sec_1=true;
document.getElementById("section-2-container").style["display"]="block";


}



if (bottom_position<-800 && loaded_sec_3==false){
refresh('/howitworks','section-3-container')
loaded_sec_3=true;


}

});







function refresh(url,container){

  var xhttp;
  if (window.XMLHttpRequest) {
    // code for modern browsers
    xhttp = new XMLHttpRequest();
    
    } else {
    // code for IE6, IE5
    xhttp = new ActiveXObject("Microsoft.XMLHTTP");
  }
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById(container).innerHTML = this.responseText;
      
      
    }
  };

  xhttp.open("GET" , url, true);
  
  xhttp.send();
 

}