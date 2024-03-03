// Changes the opacity of the elements to 1 (completely opaque) when the document is ready. CSS handles fade in.

$(document).ready(function(){
    $(".loading-item1, .loading-item2, .loading-item3, .loading-item4").css('opacity', '1');
});

// Gives each card a transition delay that increases by 0.2 seconds, creating a cascading effect.
$(document).ready(function(){
    $(".loading-cards").each(function(i) {
        $(this).css({
            'opacity': '1',
            'transition': 'opacity 2.5s ease-in-out',
            'transition-delay': (i * 0.2) + 's' // delay increases by 0.2s for each card
        });
    });
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