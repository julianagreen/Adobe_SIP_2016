window.onload= function() {
    $('.drop-item').on('click', resetDisplay)
    // $('.drop-item').each(clickListener);
}

function resetDisplay(event){
    $(".project-section").hide();
    var dropItem = event.target.innerHTML;
    if (dropItem == "Art Books"){
        $("#books").show();
    }
    if (dropItem == "letterpress"){
        $("#letterpress").show();
    }
    if (dropItem == "Wood Projects"){
        $("#wood").show();
    }
    // if (dropItem == "Architecture"){
    //     $("#architecture").show();
    // }
}

function myFunction(){
    document.getElementById("myDropdown").classList.toggle("show");
}