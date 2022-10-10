var audio = document.getElementById("audio");
var rande = document.getElementById("range");

range.onchange = function(){
    audio.volume = this.value/100;
}
