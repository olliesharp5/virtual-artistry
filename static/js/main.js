// JQuery Code 

$(document).ready(function(){
    $(".loading-item1").hide().fadeIn(500);
});

$(document).ready(function(){
    $(".loading-item2").hide().fadeIn(1000);
});

$(document).ready(function(){
    $(".loading-item3").hide().fadeIn(2000);
});

$(document).ready(function(){
    $(".loading-item4").hide().fadeIn(2500);
});

$(document).ready(function(){
    $(".nav-link").hover(
        function(){
            $(this).css({
                "background-color": "#5e3c58",
                "color": "#bfb5b2"
            });
        }, 
        function(){
            $(this).css({
                "background-color": "transparent",
                "color": "black"
            });
        }
    );
});