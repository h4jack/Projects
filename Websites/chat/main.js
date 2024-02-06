
const input_msg = document.getElementById("input-msg");
const output_div = document.getElementById("chat-output");

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
    preTag.textContent = DOMPurify.sanitize(input_msg.value);
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
