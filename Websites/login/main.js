const uname = document.getElementById('username');
const email = document.getElementById('email');
const passwd = document.getElementById('password');
const msg = document.getElementById('log-msg');

function onLoad() {
    if (isSigned()) {
        window.open('home.html');
    }
}
function sign() {
    if (isPasswd()[0]) {

    } else {
        showError(isPasswd()[1]);
    }
}
function showError(str) {
    msg.innerHTML = str;
}

function isEmail(email) {
    return
}
function isPasswd() {
    if (passwd.value.length < 8) {
        return [false, 'Length should be more then 8']
    } else {
        return [true, 'Everythong is Fine.']
    }
}
function isUname(uname) {

}

function isSigned() {
    return false;
}