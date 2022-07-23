addEventListener("DOMContentLoaded", function(){
    let commandButtons = document.querySelectorAll(".command");
    for (let i = 0, l = commandButtons.length; i < l; i++){
        let button = commandButtons[i];
        button.addEventListener("click", function(e) {
            e.preventDefault();

            let clickedButton = e.target;
            let command = clickedButton.value;

            let request = new XMLHttpRequest();
            request.onload = function() {
                alert(request.responseText);
            };

            request.open("GET", "/" + command, true);
            request.send();
        });
    }
}, true);

// window.addEventListener("keydown", function (event){
//     if (event.defaultPrevented){
//         return;
//     }
//     switch (event.key){
//         case "ArrowUp":
//             console.log(event.key);
//             break;
//         case "ArrowLeft":
//             console.log(event.key);
//             break;
//         case "ArrowRight":
//             console.log(event.key);
//             break;
//         case "ArrowDown":
//             console.log(event.key);
//             break;
//         case " ":
//             console.log(event.key);
//             break;
//     }
//     // event.preventDefault();
// }, true);