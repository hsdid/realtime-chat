document.addEventListener('DOMContentLoaded', ()=> {

let isOpen = false;
var y = window.matchMedia("(max-width: 500px)")
var x = document.getElementById("rooms_area");
document.querySelector('#pick_room').onclick = (e) => {



        var z = document.getElementById("message_area");

          if(y.matches) {

             //z.style.display = "none";

              if (x.style.display === "none") {
                 x.style.display = "block";
                 z.style.display = "none";
              } else {
                x.style.display = "none";
                z.style.display = "block";
              }

          }

//          else if (x.style.display === "none") {
//            x.style.display = "block";
//
//          } else {
//            x.style.display = "none";
//
//          }

    }
//color pallet
var colors = ["#7F7FD5","#22C6E3","#07E4D2","#FC6A8F"]


document.body.style.background = colors[color];

// chat color picker
document.querySelector('#pick_color').onchange = (e) => {
    var i = document.querySelector('#color').value
     document.body.style.background = colors[i];
}


})