document.addEventListener('DOMContentLoaded', ()=> {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.send("iam connected");
    });

    socket.on('message', data => {
        //        const p = document.createElement('p');
        //        const br = document.createElement('br')
        console.log(data)

    });

    socket.on('some-event', data => {

    console.log(data)
    })

    document.querySelector('#send_message').onclick = (event) => {
        event.preventDefault();
        socket.send(document.querySelector('#user_message').value);
        document.querySelector('#user_message').value = '';


    }

})