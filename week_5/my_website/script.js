$(document).ready(function(){
    $('.drop-item').on('click', resetDisplay);
    $(".nav_item").on("click", nav_to_page);

    fade_now();
});

function resetDisplay(event){
    $(".project-section").hide();
    var dropItem = $(this).html();
    // var dropItem = event.target.innerHTML;
    if (dropItem == "Art Books"){
        $("#books").show();
    }
    if (dropItem == "Letterpress"){
        $("#letterpress").show();
    }
    if (dropItem == "Wood Projects"){
        $("#wood").show();
    }
    if (dropItem == "Architecture"){
        $("#architecture").show();
    }
    if (dropItem == "Bracelets"){
        $("#bracelets").show();
    }
    if (dropItem == "Other"){
        $("#other").show();
    }
}

function myFunction(){
    document.getElementById("myDropdown").classList.toggle("show");
}


function fade_now(){
    var hover_target = $(".project").children("img");
    $(hover_target).mouseenter(function(){
        $(this).fadeTo("slow", .3);
        // $("#date").show();
    });

    $(hover_target).mouseleave(function(){
        $(this).fadeTo("slow", 1);
        // $("#date").hide();
    });
}

function nav_to_page(){
    $(".page").hide();
    var which_page = "#" + $(this).html();
    $(which_page).show();
}