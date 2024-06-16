// jquery script
$(document).ready(function () {
  // use jquery selector
  const element = $('header');

  // Check if element was found
  if (element) {
    // set color
    element.css = ('color', '#FF0000');
  } else {
    console.error('Header element not found');
  }
});
