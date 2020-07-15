function getCookieValue(name) {
    let value = document.cookie.split('; ').find(c => c.startsWith(name)).split('=')[1];
    return value;
}

const clipboardId = getCookieValue('clipboard-id');

const clipSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/clipboard/'
    + clipboardId
    + '/'
);

let cloudClipboard = '';

function sendClipboard() {
    console.log('sending text');
    navigator.clipboard.readText().then(clipText => {
        if (clipText !== '') {
            clipSocket.send(JSON.stringify({
                clipboard: clipText
            }));
        } else {
            console.log('nothing to send.');
        }
    });
}

function receiveClipboard() {
    if (cloudClipboard !== '') {
        navigator.clipboard.writeText(cloudClipboard).then(() => {
            const local = document.querySelector("#local-clipboard");
            local.textContent = cloudClipboard;
        });
    } else {
        console.log("nothing to receive.");
    }
}

clipSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    cloudClipboard = data.clipboard;
    document.querySelector('#cloud-clipboard').textContent = data.clipboard;
}

clipSocket.onopen = function(e) {
    clipSocket.send(JSON.stringify({
        update: true
    }));
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

function readClipboard() {
    navigator.clipboard.readText().then(clipText => {
        console.log('text is undefined?', clipText === undefined);
        console.log(clipText);
        document.querySelector('#local-clipboard').textContent = clipText;
    });
}

readClipboard();

window.onfocus = readClipboard;
