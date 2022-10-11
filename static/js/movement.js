   //Selecciono la clase player del documento
const player = document.getElementById("coach")
const bush1 =document.getElementById("buch1")
const bush2 =document.getElementById("buch2")
const bush3 =document.getElementById("buch3")
const bush4 =document.getElementById("buch4")
const bush5 =document.getElementById("buch5")
const player_pos = {
    x: parseInt(window.innerWidth /2),              //Posiciono el .player en mitad de alto y mitad de ancho del DOM
    y: parseInt(window.innerHeight /2)
}
const player_vel = {
    x: 0,                                           //Se crea constante de velocidad x = 0 & y=0
    y: 0
}

function walk(){
    player_pos.x += player_vel.x;
    player_pos.y += player_vel.y;                   //Funcion de caminar, suma a la posicion x o y la velocidad, posicion absoluta, movera en pixeles 'px' en la posicion x o y
    player.style.position = "absolute";
    player.style.left = player_pos.x +'px';
    player.style.bottom = player_pos.y +'px';
    requestAnimationFrame(walk)                     //Hace la funcion de la animación siempre se pasa de parametro la funcion
}
walk()

window.addEventListener('keydown', function(e){     //Añade el evento, 'keydown' indica el evento de cualquier tecla, la funcion(e) 'e' es el evento
    if(e.key == "ArrowUp"){                         //Si la key del evento es igual a tecla arriba
        player_vel.y = 3                            //Cambiara la velocidad hacia arriba en 3, (negativo es hacia abajo)
        player.style.backgroundImage = 'url("/RolGame/static/img/mov_back.png")'
    }
    if(e.key == "ArrowDown"){
        player_vel.y = -3
        player.style.backgroundImage = 'url("/RolGame/static/img/mov_front.png")'
    }
    if(e.key == "ArrowLeft"){
        player_vel.x = -3
        player.style.backgroundImage = 'url("/RolGame/static/img/mov_left.png")'
    }
    if(e.key == "ArrowRight"){
        player_vel.x = 3
        player.style.backgroundImage = 'url("/RolGame/static/img/mov_right.png")'
    }
    // const socket = io();
    if (in_bush(player)){
        // socket.emit('enemigo', {})
        console.log("inside")}
    else{console.log("outside")}
    player.classList.add('active')                  //Activa el keyframe de la clase player para la animación
})
window.addEventListener('keyup', function(){
    player_vel.x = 0                                //activa el evento 'keyup' cuando no presionas ninguna tecla, la velocidad en x & y sera 0 y removera la animación.
    player_vel.y = 0
    player.classList.remove('active')
})


function getCoords(elem) {
    let box = elem.getBoundingClientRect();
  
    return {
      top: box.top + window.pageYOffset,
      right: box.right + window.pageXOffset,
      bottom: box.bottom + window.pageYOffset,
      left: box.left + window.pageXOffset
    };
}

// console.log("bush1: ",bush1.offsetTop, bush1.offsetTop+bush1.offsetHeight ,bush1.offsetLeft,  bush1.offsetLeft+bush1.offsetWidth);
// console.log("bush2: ", bush2.offsetTop, bush2.offsetTop+bush2.offsetHeight ,bush2.offsetLeft,  bush2.offsetLeft+bush2.offsetWidth);
// console.log("bush3: ", bush3.offsetTop, bush3.offsetTop+bush3.offsetHeight ,bush3.offsetLeft,  bush3.offsetLeft+bush3.offsetWidth);
// console.log("bush4: ", bush4.offsetTop, bush4.offsetTop+bush4.offsetHeight ,bush4.offsetLeft,  bush4.offsetLeft+bush4.offsetWidth);
// console.log("bush5: ", bush5.getBoundingClientRect().top, bush5.getBoundingClientRect().bottom ,bush5.getBoundingClientRect().left,  bush5.getBoundingClientRect().right);
// // console.log("bush5: ", bush5.offsetTop, bush5.getBoundingClientRect().bottom ,bush5.offsetLeft,  bush5.getBoundingClientRect().right);
// console.log("plc: ", player.getBoundingClientRect().top, player.getBoundingClientRect().left);



function in_bush(player){
    //console.log("plc: ", player_pos, player_pos);
    // // console.log("plc: ", player.getBoundingClientRect().top, player.getBoundingClientRect().left);
    // console.log("plc: ",getComputedStyle(player).top , getComputedStyle(player).bottom ,getComputedStyle(player).left, getComputedStyle(player).right )
    console.log("bush1: ",getCoords(bush1).top, getCoords(bush1).left, getCoords(bush1).right, getCoords(bush1).bottom);
    console.log("bush2: ",getCoords(bush2).top, getCoords(bush2).left, getCoords(bush2).right, getCoords(bush2).bottom);
    console.log("bush3: ",getCoords(bush3).top, getCoords(bush3).left, getCoords(bush3).right, getCoords(bush3).bottom);
    console.log("bush4: ",getCoords(bush4).top, getCoords(bush4).left, getCoords(bush4).right, getCoords(bush4).bottom);
    console.log("bush5: ",getCoords(bush5).top, getCoords(bush5).left, getCoords(bush5).right, getCoords(bush5).bottom);
    console.log("player: ",getCoords(player).top, getCoords(player).left, getCoords(player).right, getCoords(player).bottom);


    console.log(getCoords(player).top, getCoords(player).left)
    if(player.offsetTop > bush1.offsetTop && player.offsetTop+player.offsetHeight < bush1.offsetTop+bush1.offsetHeight  && player.offsetLeft < bush1.offsetLeft  &&  player.offsetLeft+player.offsetWidth <  bush1.offsetLeft+bush1.offsetWidth){
        console.log("1")
        return true;        
    }
    if(player.offsetTop > bush2.offsetTop && player.offsetTop+player.offsetHeight < bush2.offsetTop+bush2.offsetHeight  && player.offsetLeft < bush2.offsetLeft  &&  player.offsetLeft+player.offsetWidth <  bush2.offsetLeft+bush2.offsetWidth){
        console.log("2")
        return true;        
    }
    if(player.offsetTop > bush3.offsetTop && player.offsetTop+player.offsetHeight < bush3.offsetTop+bush3.offsetHeight  && player.offsetLeft < bush3.offsetLeft  &&  player.offsetLeft+player.offsetWidth <  bush3.offsetLeft+bush3.offsetWidth){
        console.log("3")
        return true;        
    }
    if(player.offsetTop > bush4.offsetTop && player.offsetTop+player.offsetHeight < bush4.offsetTop+bush4.offsetHeight  && player.offsetLeft < bush1.offsetLeft  &&  player.offsetLeft+player.offsetWidth <  bush4.offsetLeft+bush4.offsetWidth){
        console.log("4")
        return true;        
    }
    if(player.offsetTop > bush5.offsetTop && player.offsetTop+player.offsetHeight < bush5.offsetTop+bush5.offsetHeight  && player.offsetLeft < bush5.offsetLeft  &&  player.offsetLeft+player.offsetWidth <  bush5.offsetLeft+bush5.offsetWidth){
        console.log("5")
        return true;        
    }
    return false;
    
    
}
// bush1
