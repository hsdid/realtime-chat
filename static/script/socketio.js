
document.addEventListener('DOMContentLoaded', ()=> {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    let room ;
    //joinRoom("room 1");

    // Display incoming message
    socket.on('message', data => {


        const msg_body = document.querySelector("#msg");
        if (typeof data.username === 'undefined') {
            printSysMsg(data.msg)
        } else if  (data.username == username) {
             msg_body.insertAdjacentHTML("beforeend",`<div class="d-flex justify-content-end mb-4">
                                                       <div class="msg_cotainer_send message">
                                                            ${data.msg}
                                                            <span class="msg_time_send">${data.time_stamp}</span>
                                                        </div>
                                                   </div>`)

        } else if (data.username != username ) {
            msg_body.insertAdjacentHTML("beforeend",`<div class="d-flex justify-content-start mb-4">
                                                       <div class="msg_cotainer message">
                                                            ${data.msg}
                                                            <span class="msg_time_send">${data.time_stamp}</span>
                                                        </div>
                                                   </div>`)

        }


        //Automatically scroll down chat after display msg
        msg_body.scrollTop = msg_body.scrollHeight;

    });


    //// Send message

    // Send message on click enter
    document.addEventListener('keypress', (e) => {
        console.log(rooms);
        if (e.key === 'Enter') {

            sendMsg()
        }
    });
    // Send mesage on click virtual button
    document.querySelector('#send_message').onclick = (e) => {

        sendMsg();
    }

    //Room selection
    document.querySelectorAll('.room_info').forEach(div => {
        div.onclick = () => {

            //change chat room name
            document.querySelector('#chats').innerHTML = div.innerHTML;


            let newRoom = div.innerHTML;
            if (newRoom == room) {
                msg = `You are already in ${room} room`

                printSysMsg(msg);
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }

            var y = window.matchMedia("(max-width: 500px)")

            var x = document.getElementById("rooms_area");
            var z = document.getElementById("message_area");
            // if max-width: 500px add function toggle hide/show rooms-area
            if(y.matches) {


                 if (x.style.display === "none") {

                    x.style.display = "block";
                    z.style.display = "none";
                  } else {

                    x.style.display = "none";
                    z.style.display = "block";
                  }

            }

        }


    });
    // Leve room
    function leaveRoom(room) {
        // sending username and name of room to name of event(left) in python
        socket.emit('leave', {'username': username, 'room': room})
    }

    // Join room
    function joinRoom(room) {
     // sending username and name of room to name of event (join) in python
        socket.emit('join', {'username': username, 'room': room})

        // Clear message area
        document.querySelector('#msg').innerHTML = '';
        // Autofocus on text box
        document.querySelector('#user_message').focus();
    }
    // Print system message
    function printSysMsg(msg) {
        const p = document.createElement('p');
        p.innerHTML = msg;
        document.querySelector('#msg').append(p);
    }

    function sendMsg() {
        //e.preventDefault();

        if (document.querySelector('#user_message').value.length == 0) {
            return;
        }
        socket.send({'msg':document.querySelector('#user_message').value,
        'username': username, 'room': room });
        document.querySelector('#user_message').value = '';
    }

})



//        const search_room = document.querySelector('#search_room');
//        search_room.addEventListener('change', updateValue);
//
//
//
////        find_user: '',
////        users: []
////             filteredList(){
////                    return this.users.filter(user => {
////                        return user.name.toLowerCase().includes(this.find_user.toLowerCase());
////                    });
////            }
////        },

