let canvas, ctx
let WIDTH = 480, HEIGHT = 320
let IS_KEY_PRESSED = {}

// キーイベントコールバック関数
// 32: space
// 37: ←
// 39: →
function keyDown (event) {
  IS_KEY_PRESSED[event.keyCode] = true
}

function keyUp (event) {
  IS_KEY_PRESSED[event.keyCode] = false
}

function spaceKey () {
  return IS_KEY_PRESSED[32]
}

function leftKey () {
  return IS_KEY_PRESSED[37]
}

function rightKey () {
  return IS_KEY_PRESSED[39]
}

function upKey () {
  return IS_KEY_PRESSED[38]
}

function downKey () {
  return IS_KEY_PRESSED[40]
}

// 初期化処理
function init () {
  canvas = document.getElementById('canvas')
  if (!canvas || !canvas.getContext) return
  ctx = canvas.getContext('2d')

  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'

  window.addEventListener('keydown', keyDown, true)
  window.addEventListener('keyup', keyUp, true)

  setTimeout(function () {
    if (window["main"]) {
      setInterval(main, 1000 / 60)
    }
  }, 10)
}

window.onload = init
