addEventListener("DOMContentLoaded", function(){
    let commandButtons = document.querySelectorAll(".command");
    for (let i = 0, l = commandButtons.length; i < l; i++){
        let button = commandButtons[i];
        button.addEventListener("click", function(e) {
            e.preventDefault();

            let clickedButton = e.target;
            let command = clickedButton.id;

            let request = new XMLHttpRequest();

            request.open("GET", "/" + command, true);
            request.send();
        });
    }
}, true);

window.addEventListener("keydown", function (event){
    let request = new XMLHttpRequest();
    switch (event.key){
        case "ArrowUp":
            request.open("GET", "/" + "up", true);
            request.send();
            break;
        case "ArrowLeft":
            request.open("GET", "/" + "left", true);
            request.send();
            break;
        case "ArrowRight":
            request.open("GET", "/" + "right", true);
            request.send();
            break;
        case "ArrowDown":
            request.open("GET", "/" + "down", true);
            request.send();
            break;
        case " ":
            request.open("GET", "/" + "fire", true);
            request.send();
            break;
    }
}, true);