var buttons = document.getElementsByClassName("button-profile");
function changeClass(){
    for (var i =0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected')
    }
    this.classList.add('selected');
}

$(".button-profile").on("click", changeClass)