const cl1 = document.getElementById("cl1");
const cl2 = document.getElementById("cl2");
const cl3 = document.getElementById("cl3");
const cl4 = document.getElementById("cl4");
const cl5 = document.getElementById("cl5");
const cl6 = document.getElementById("cl6");
const cl7 = document.getElementById("cl7");
const cl8 = document.getElementById("cl8");
const cl9 = document.getElementById("cl9");
const o = document.getElementById("o");
const x = document.getElementById("x");
const result = document.getElementById("resultdiv");
const restartbtn = document.getElementById("restart");

let isXorO = false;
let gameOver = false;
let isfil = [0, 0, 0, 0, 0, 0, 0, 0, 0];
let xscore = 0;
let oscore = 0;

cl1.onclick = function () { boxClicked(1); }
cl2.onclick = function () { boxClicked(2); }
cl3.onclick = function () { boxClicked(3); }
cl4.onclick = function () { boxClicked(4); }
cl5.onclick = function () { boxClicked(5); }
cl6.onclick = function () { boxClicked(6); }
cl7.onclick = function () { boxClicked(7); }
cl8.onclick = function () { boxClicked(8); }
cl9.onclick = function () { boxClicked(9); }
restartbtn.onclick = function () { restart(); }

const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];


function boxClicked(boxn) {
    if (gameOver) {
        return;
    }
    // alert("this");
    if (isfil[boxn - 1] == 0) {
        isfil[boxn - 1] = 1;
    } else {
        return;
    }
    if (isXorO) {
        text = 'X';
        isXorO = false;
    } else {
        text = 'O';
        isXorO = true;
    }

    switch (boxn) {
        case 1:
            cl1.innerText = text;
            break;
        case 2:
            cl2.innerText = text;
            break;
        case 3:
            cl3.innerText = text;
            break;
        case 4:
            cl4.innerText = text;
            break;
        case 5:
            cl5.innerText = text;
            break;
        case 6:
            cl6.innerText = text;
            break;
        case 7:
            cl7.innerText = text;
            break;
        case 8:
            cl8.innerText = text;
            break;
        case 9:
            cl9.innerText = text;
            break;
        default:
            alert("Error Occured...");
            console.log("Error...");
    }

    gameOver = checkForWinner();

    if (gameOver) {
        if (isXorO) {
            document.getElementById("winner").innerText = "O won the Game";
            oscore = oscore + 1;
            o.innerText = oscore;
        } else {
            document.getElementById("winner").innerText = "X won the Game";
            xscore = xscore + 1;
            x.innerText = xscore;
        }
        result.style.visibility = "visible";
        gameOver = true;
    } else if (isFullBoard()) {
        gameOver = true;
        document.getElementById("winner").innerText = "It's a draw!";
        result.style.visibility = "visible";
    }
}

function checkForWinner() {
    let squares = [
        cl1.innerText,
        cl2.innerText,
        cl3.innerText,
        cl4.innerText,
        cl5.innerText,
        cl6.innerText,
        cl7.innerText,
        cl8.innerText,
        cl9.innerText
    ];

    for (let combination of winningCombinations) {
        let [a, b, c] = combination;
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return true;
        }
    }

    return false;
}

function isFullBoard() {
    let squares = [
        cl1.innerText,
        cl2.innerText,
        cl3.innerText,
        cl4.innerText,
        cl5.innerText,
        cl6.innerText,
        cl7.innerText,
        cl8.innerText,
        cl9.innerText
    ];

    return squares.every(square => square);
}

function restart() {
    for(let i = 0; i < 9; i++){
        isfil[i] = 0;
    }
    cl1.innerText = cl2.innerText = cl3.innerText = cl4.innerText = cl5.innerText = cl6.innerText = cl7.innerText = cl8.innerText = cl9.innerText = "";
    isXorO = false;
    gameOver = false;
    document.getElementById("winner").innerText = "";
    result.style.visibility = "hidden";
    return;
}