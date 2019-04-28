let playerW = 24, playerH = 16
let playerX = 0, playerY = HEIGHT - 16

let enemyW = 24, enemyH = 16
let enemyX = 0, enemyY = 0, enemyV = 2

let shotW = 8, shotH = 16
let shotX = 0, shotY = -100, shotV = -8

function main () {
    ctx.clearRect(0, 0, WIDTH, HEIGHT)
    
    ctx.fillRect(playerX, playerY, playerW, playerH)
    ctx.fillRect(enemyX, enemyY, enemyW, enemyH)
    
    if (shotY + shotH > 0) {
        shotY += shotV
    } else {
        if (spaceKey()) {
            shotX = playerX + playerW / 2 - shotW / 2
            shotY = playerY
        }
    }
    
    enemyX += enemyV
        
    if (rightKey()) {
        playerX += 3
    }

    if (leftKey()) {
        playerX -= 3
    }
    
    if (upKey()) {
        playerY -= 2
    }
    if (downKey()) [
        playerY += 2
    ]

    if (playerX < 0) {
        playerX = 0
    }
    if (playerX > WIDTH - 24) {
        playerX = WIDTH - 24
    }
    if (playerY < 0) {
        playerY = 0
    }
    if (playerY > HEIGHT - 16) {
        playerY = HEIGHT - 16
    }
    
    if (enemyX > WIDTH - 24) {
        enemyX = WIDTH -24
        enemyY += 4
        enemyV = -2
    }
    if (enemyX < 0) {
        enemyX = 0
        enemyY += 4
        enemyV = 2
    }
}