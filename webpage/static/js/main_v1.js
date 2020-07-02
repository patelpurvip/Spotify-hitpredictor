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
function filterdata() {
    event.preventDefault();

    // Select the input element id and its value
    var trackValue = d3.select("#song").property("value");
    var artistValue = d3.select("#artist").property("value");
    console.log(trackValue, artistValue);


    // Get information from api/flask
    var filterData = { "prediction": "1", "score":[0.1415, 0.8585] };
    console.log(filterData);


    // Show information from song/artist defined
    var result = d3.select("#prediction-result");
    var score = d3.select("#prediction-score");
    var score_value0 = Math.round(filterData.score[0]*100);
    var score_value1 = Math.round(filterData.score[1]*100);
    // console.log(score_value0);
    // console.log(score_value1);

    result.html("");
    score.html("");
    if (filterData.prediction = 1) {
        result.text("It's a HIT!");
        score.text(score_value1+"%");
    } else {
        result.text("It's a FLOP!");
        score.text(score_value0+"%");
    }

};
// filterdata();

// Show information from song/artist defined
result.html("");
score.html("");

// incluir code de microbios en su cuadro de texto



    // // Show information filtered in Web Table
    // tbody.html("");
    // // append rows and data info
    // filterData.forEach((ufoCase) => {
    //     // console.log(ufoCase)
    //     var row = tbody.append("tr");
    //     Object.entries(ufoCase).forEach(([key, value]) => {
    //         // console.log(key,value)
    //         var cell = row.append("td");
    //         cell.text(value);
    //     });
    // });