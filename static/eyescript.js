function openLogin(){
document.getElementById("loginModal").style.display="flex";
}

function closeLogin(){
document.getElementById("loginModal").style.display="none";
}

function openRegister(){
document.getElementById("registerModal").style.display="flex";
}

function closeRegister(){
document.getElementById("registerModal").style.display="none";
}

function toggleTheme(){
document.body.classList.toggle("light");
}

window.onclick=function(e){

if(e.target==document.getElementById("loginModal")){
closeLogin();
}

if(e.target==document.getElementById("registerModal")){
closeRegister();
}
}