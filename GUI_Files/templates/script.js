window.addEventListener("keydown", function (event){
    if (event.defaultPrevented){
        return;
    }
    switch (event.key){
        case "ArrowUp":
            console.log(event.key);
            break;
        case "ArrowLeft":
            console.log(event.key);
            break;
        case "ArrowRight":
            console.log(event.key);
            break;
        case "ArrowDown":
            console.log(event.key);
            break;
        case " ":
            console.log(event.key);
            break;
    }
    // event.preventDefault();
}, true);