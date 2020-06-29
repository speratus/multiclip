function getCookieValue(name) {
    let value = document.cookie.split('; ').find(c => c.startsWith(name)).split('=')[1];
    return value;
}

function createButton(parentId, text, clickFunction) {
    const button = document.createElement('button');
    button.textContent = text;
    button.onclick = clickFunction;
    const parent = document.getElementById(parentId);
    parent.appendChild(button);
}

const clipboardId = getCookieValue('clipboard-id');

const clipSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/clipboard/'
    + clipboardId
    + '/'
);

function sendClipboard() {
    console.log('sending text');
    navigator.clipboard.readText().then(clipText => {
        console.log('read clipboard.');
        console.log('what is Clipsocket?', typeof clipSocket);
        clipSocket.send(JSON.stringify({
            clipboard: clipText
        }));
    });
}

function receiveClipboard(clipboardText) {
    navigator.clipboard.writeText(clipboardText).then(() => {
        const local = document.querySelector("#local-clipboard");
        local.textContent = clipboardText;
    });
}

clipSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log('received data', data)
    document.querySelector('#cloud-clipboard').textContent = data.clipboard;
    createButton('cloud-container', 'Paste from Cloud', () => {receiveClipboard(data.clipboard)});
}

clipSocket.onerror = function(e) {
    console.log('encountered error:', e)
}

clipSocket.onclose = function(e) {
    console.error('Clip socket closed unexpectedly.');
}

navigator.permissions.query({name:'clipboard-read'}).then(function(result) {
    if (result.state === 'granted') {
        console.log('has permission to use the clipboard');
    } else if (result.state === 'prompt') {
        console.log('prompting user for permission to use the clipboard');
    }
});

navigator.clipboard.readText().then(clipText => {
    console.log('text is undefined?', clipText === undefined);
    console.log(clipText);
    document.querySelector('#local-clipboard').textContent = clipText;
    if (clipText !== "") {
        createButton('local-container', 'Copy to Cloud', sendClipboard);
    }
});