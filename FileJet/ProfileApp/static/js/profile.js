var buttons = document.getElementsByClassName("button-profile");
function changeClass(){
    if ( $(this).val() === "files" ){
        $("#files").css("display", "flex")
        $("#your-messages").css("display", "none")
        $("#messages-to-you").css("display", "none")
    }
    else if ( $(this).val() === "your-messages" ){
        $("#files").css("display", "none")
        $("#your-messages").css("display", "flex")
        $("#messages-to-you").css("display", "none")
    }
    else if ( $(this).val() === "messages-to-you" ){
        $("#files").css("display", "none")
        $("#your-messages").css("display", "none")
        $("#messages-to-you").css("display", "flex")
    }
    for (var i =0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected')
    }
    this.classList.add('selected');
}

$(".button-profile").on("click", changeClass)