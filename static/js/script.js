$(document).ready(function() {
    // In productform is_saleprice is hidden untill checkbox is checked.
$(function() {
  
  // Get the form fields and hidden div
  var checkbox1 = $("#id_is_for_sale");
  var is_saleprice = $("#div_id_saleprice");
  var is_saleprice_input = $("#id_saleprice");
  
  // Hide the fields.
  $(function() {
    if (checkbox1.is(':checked')) {
        is_saleprice.show();
        is_saleprice_input.prop("required", true);
    } else {
        is_saleprice.hide();
        is_saleprice_input.prop("required", false);
    }}); 
  
  // Setup an event listener for when the state of the 
  // checkbox changes.
  checkbox1.change(function() {
    // Check to see if the checkbox is checked.
    if (checkbox1.is(':checked')) {
      // Show the hidden fields.
      is_saleprice.show();
      is_saleprice_input.prop("required", true);
    } else {
      // Hidden fields hidden.
      is_saleprice.hide();
      is_saleprice_input.prop("required", false);
      // Clear the value of the 
      // hidden fields.      
      $("#id_saleprice").val("");
    }
  });
});

$(function() {
  
  // Get the form fields and hidden div
  var checkbox2 = $("#id_is_for_rent");
  var is_rentprice = $("#div_id_rentprice_per_week");
  var is_rentprice_input = $("#id_rentprice_per_week");
  
  // Hide the fields.
  $(function() {
    if (checkbox2.is(':checked')) {
        is_rentprice.show();
        is_rentprice_input.prop("required", true);
    } else {
        is_rentprice.hide();
        is_rentprice_input.prop("required", false);
    }}); 
  
  // Setup an event listener for when the state of the 
  // checkbox changes.
  checkbox2.change(function() {
    // Check to see if the checkbox is checked.
    if (checkbox2.is(':checked')) {
      // Show the hidden fields.
      is_rentprice.show();
      is_rentprice_input.prop("required", true);
    } else {
      // Hidden fields hidden.
      is_rentprice.hide();
      is_rentprice_input.prop("required", false);
      // Clear the value of the 
      // hidden fields.      
      $("#id_rentprice_per_week").val("");
    }
  });
});

$(function() {
    var checkbox1 = $("#id_is_for_sale");
    var checkbox2 = $("#id_is_for_rent");
    $(function() {
    if (checkbox1.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);
    } else if (checkbox2.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);  
    } else {
      checkbox2.prop("required", true);
      checkbox1.prop("required", true);
    }});
    checkbox2.change(function() {
    // Check to see if checkbox1 is checked.
    if (checkbox1.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);
    } else if (checkbox2.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);
        } else {  
      checkbox2.prop("required", true);
      checkbox1.prop("required", true); 
    }});
    checkbox1.change(function() {
    // Check to see if checkbox1 is checked.
    if (checkbox2.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);
    } else if (checkbox2.is(':checked')) {
      checkbox2.prop("required", false);
      checkbox1.prop("required", false);
        } else {  
      checkbox2.prop("required", true);
      checkbox1.prop("required", true); 
    }});
});

});
