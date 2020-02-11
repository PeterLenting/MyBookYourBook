$(function() {
  
  // Get the form fields and hidden div
  var checkbox = $("#id_is_for_sale");
  var is_saleprice = $("#div_id_saleprice");
  
  // Hide the fields.
    is_saleprice.hide();
  
  // Setup an event listener for when the state of the 
  // checkbox changes.
  checkbox.change(function() {
    // Check to see if the checkbox is checked.
    if (checkbox.is(':checked')) {
      // Show the hidden fields.
      is_saleprice.show();
    } else {
      // Hidden fields hidden.
      is_saleprice.hide();
      // Clear the value of the 
      // hidden fields.      
      $("#id_saleprice").val("");
    }
  });
});