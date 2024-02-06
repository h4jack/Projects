const input_msg = document.getElementById("input-msg");
const output_div = document.getElementById("chat-output");

const name = document.getElementById("input-name");
const rkey = document.getElementById("input-rkey");

function scrolltobottom() {
    const newScrollHeight = output_div.scrollHeight;
    const currentScrollPosition = output_div.scrollTop;
    const newScrollPosition =
        newScrollHeight > output_div.clientHeight
            ? newScrollHeight - output_div.clientHeight
            : currentScrollPosition;
    output_div.scrollTop = newScrollPosition;
}

function send() {
    const preTag = document.createElement("pre");
    preTag.textContent = name.value + `:
` + DOMPurify.sanitize(input_msg.value);
    preTag.classList.add("message-content");

    const divTag = document.createElement("div");
    divTag.classList.add("message-container", "sender");

    if (input_msg.value == "") {
        return;
    }
    divTag.appendChild(preTag);
    const chatOutput = document.getElementById("chat-output");
    chatOutput.appendChild(divTag);

    input_msg.value = "";
    scrolltobottom();
}


function loadFun() {
    document.getElementById("user-rkey-name").style.visibility = "visible";
    document.getElementById("send-btn").style.visibility = "hidden";
}
function submit_rkey_name() {
    if (rkey.value == "") {
        alert("Room Key fireld is NULL");
        return;
    } else if (name.value == "") {
        alert("Name Field is NULL");
        return;
    }
    document.getElementById("send-btn").style.visibility = "visible";
    document.getElementById("user-rkey-name").style.visibility = "hidden";
}