// jQuery script
$(document).ready(function() {
    // select the div
    const toggleDiv = $('DIV#toggle_header');
    const headerElement = $('header');

    // add a click event handler
    toggleDiv.click(function () {
        headerElement.toggleClass('red green');
    });
});
