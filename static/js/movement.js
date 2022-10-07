const player = document.querySelector('.player')    //Selecciono la clase player del documento
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
    player.classList.add('active')                  //Activa el keyframe de la clase player para la animación
})
window.addEventListener('keyup', function(){
    player_vel.x = 0                                //activa el evento 'keyup' cuando no presionas ninguna tecla, la velocidad en x & y sera 0 y removera la animación.
    player_vel.y = 0
    player.classList.remove('active')
})