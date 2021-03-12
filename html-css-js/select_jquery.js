$(document).ready(function () {
  var coutriesoption = " ";
  var stateoptions = " ";
  var cityoptions = "";

  $.getJSON("countries.json", function (data) {
    $.each(data, function (indexofcode, country) {
      coutriesoption +=
        '<option value = "' + country.code + '">' + country.name + "</option>";
        
    });
 
    $("#country").html(coutriesoption);

    $("#country").change(function () {
      
    //reset other two dropdown code starts
    // $("#state").prop('selectedIndex',0);
    $('#state option:first').prop('selected',true);
    // $("#city").prop('selectedIndex',0);
    $('#city option:first').prop('selected',true);

    // //reset other two dropdown code ENDS
    //   var val =$(this).val()
    //   switch (val) {
    //     case "IN":
          
    //       break;
      
    //     default:
    //       break;
    //   }
      if ($(this).val() == "IN") {
        $.getJSON("IndianStates.json", function (data) {
          stateoptions=""
          $.each(data, function (statecode, state) {
            stateoptions +=
              "<option value = " + statecode + ">" + state + "</option>";
          });
          $("#state").html(stateoptions);
        });
      }

      else if ($(this).val() == "US") {
        $.getJSON("us_state.json", function (data) {
          stateoptions=""
          $.each(data, function (statecode, state) {
            stateoptions +=
              "<option value = " + statecode + ">" + state + "</option>";
          });
          $("#state").html(stateoptions);
        });


      }
      else {
        stateoptions=""
  
      }
  
    });

   
    $("#state").change(function () {
      if ($(this).val() == "MP") {
        cityoptions = ""

        $.getJSON("mp.json", function (data) {
          $.each(data, function (indexofcode, city) {
            cityoptions +=
              "<option value = " + city.MP + ">" + city.MP + "</option>";
          });
          $("#city").html(cityoptions);
        });
      }

    else if ($(this).val() == ""){
      cityoptions = ""
      $.getJSON("mp.json", function (data) {
        $.each(data, function (indexofcode, city) {
          cityoptions +=
            "<option value = " + city.MP + ">" + city.MP + "</option>";
        });
        $("#city").html(cityoptions);
      });
    }


    

      
    });
  });
});

