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

          else if (x.style.display === "none") {
            x.style.display = "block";

          } else {
            x.style.display = "none";

          }

    }



})