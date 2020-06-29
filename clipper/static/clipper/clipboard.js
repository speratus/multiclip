function getCookieValue(name) {
    let value = document.cookie.split('; ').find(c => c.startsWith(name)).split('=')[1];
    return value;
}

const roomId = getCookieValue('clipboard-id');

const clipSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/clipboard/'
    + roomId
    + '/'
);

clipSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#cloud-clipboard').textContent = data.clipboard;
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
});
