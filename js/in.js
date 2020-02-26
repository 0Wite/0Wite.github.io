function typing(str = ""){
    let buf = document.getElementById("top").innerHTML;
    let writed = buf.length; 
    let write = "";
    if(writed < str.length){
        write = str.charAt(writed); //1文字だけ取得する
    }else{
        buf = ""; //今回は何度も繰り返すために内容を消去します
    }
    document.getElementById("top").innerHTML = buf + write;
}

const str = document.getElementById("top").innerHTML;
const delay = 200 

document.getElementById("top").innerHTML = "";
window.setInterval(function(){typing(str);}, delay);
