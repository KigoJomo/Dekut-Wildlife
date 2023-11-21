const button = document.getElementById("button");
const body = document.querySelector("body");
var clicked = false;
button.addEventListener("click", () => {
    if (clicked) {
        body.style.backgroundColor = "white";
        clicked = false;
    } else {
        body.style.backgroundColor = "yellow";
        clicked = true;
    }
});
