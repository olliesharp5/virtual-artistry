// Changes the opacity of the elements to 1 (completely opaque) when the document is ready. CSS handles fade in.

$(document).ready(function(){
    $(".loading-item1, .loading-item2, .loading-item3, .loading-item4").css('opacity', '1');
});

// JQuery Code 

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