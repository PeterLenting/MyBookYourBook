$(document).ready(function() {
    // In productform is_saleprice is hidden untill checkbox is checked.
$(function() {
  
  // Get the form fields and hidden div
  var checkbox1 = $("#id_is_for_sale");
  var is_saleprice = $("#div_id_saleprice");
  
  // Hide the fields.
    is_saleprice.hide();
  
  // Setup an event listener for when the state of the 
  // checkbox changes.
  checkbox1.change(function() {
    // Check to see if the checkbox is checked.
    if (checkbox1.is(':checked')) {
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

$(function() {
  
  // Get the form fields and hidden div
  var checkbox2 = $("#id_is_for_rent");
  var is_rentprice = $("#div_id_rentprice");
  
  // Hide the fields.
    is_rentprice.hide();
  
  // Setup an event listener for when the state of the 
  // checkbox changes.
  checkbox2.change(function() {
    // Check to see if the checkbox is checked.
    if (checkbox2.is(':checked')) {
      // Show the hidden fields.
      is_rentprice.show();
    } else {
      // Hidden fields hidden.
      is_rentprice.hide();
      // Clear the value of the 
      // hidden fields.      
      $("#id_rentprice").val("");
    }
  });
})

});
