const player = document.querySelector('.player')
const player_pos = {
    x: parseInt(window.innerWidth /2),
    y: parseInt(window.innerHeight /2)
}
const player_vel = {
    x: 0,
    y: 0
}

function walk(){
    player_pos.x += player_vel.x;
    player_pos.y += player_vel.y;
    player.style.position = "absolute";
    player.style.left = player_pos.x +'px';
    player.style.bottom = player_pos.y +'px';
    requestAnimationFrame(walk)
}
walk()

window.addEventListener('keydown', function(e){
    if(e.key == "ArrowUp"){
        player_vel.y = 3
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
    player.classList.add('active')
})
window.addEventListener('keyup', function(){
    player_vel.x = 0
    player_vel.y = 0
    player.classList.remove('active')
})