var audio = document.getElementById("audio");
var rande = document.getElementById("range");

rande.value= 50;


range.onchange = function(){
    audio.volume = this.value/100;
}
