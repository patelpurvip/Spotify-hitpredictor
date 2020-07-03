(function ($) {
    "use strict";

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });
})(jQuery);



//  FILTER INFORMATION 
var button = d3.select("#filter-btn");
button.on("click", filterdata);

var form = d3.select("form");
form.on("submit", filterdata);


//  Filterdata function
function filterdata(hit_predict, hit_score) {
    event.preventDefault();

    // // Select the input element id and its value
    var trackValue = d3.select("#song").property("value");
    var artistValue = d3.select("#artist").property("value");
    console.log(trackValue, artistValue);

    // Get information from api/flask

    console.log(hit_predict, hit_score);
    var score_value0 = Math.round(hit_score[0]*100);
    var score_value1 = Math.round(hit_score[1]*100);
    
    
    var result = d3.select("#prediction-result");
    var score = d3.select("#prediction-score");

    result_info.html("");
    score_info.html("");
    if (hit_predict = 1) {
        result.text("It's a HIT!");
        score.text(score_value1+"%");
    } else {
        result.text("It's a FLOP!");
        score.text(score_value0+"%");
    }

};

