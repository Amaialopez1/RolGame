var cards = document.querySelectorAll(".tipo_de_pokemon");
console.log(cards[0])
console.log(cards[2])
var slideIndex = 0;
 showDivs(slideIndex);
 
 function plusDivs(n) {
   showDivs(slideIndex += n);
 }
 function showDivs(n) {
   var i;
   var x = document.getElementsByClassName("scene");
   if (n == 0) { 
     document.querySelector(".left").style.visibility="hidden";
     cards[0].style.display = "grid";
     cards[1].style.display =  "none";
     cards[2].style.display =  "none";
    }
   else if (n == 2) { 
       document.querySelector(".right").style.visibility="hidden";
       cards[1].style.display = "grid";
       cards[0].style.display =  "none";
       cards[2].style.display =  "none";
   }
   else{
     document.querySelector(".left").style.visibility='visible '
     document.querySelector(".right").style.visibility="visible";
     cards[2].style.display = "grid";
     cards[1].style.display =  "none";
     cards[0].style.display =  "none";
   }
 }