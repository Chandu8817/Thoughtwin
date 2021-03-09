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

    //reset other two dropdown code ENDS


      if ($(this).val() == "IN") {
        $.getJSON("IndianStates.json", function (data) {
          $.each(data, function (statecode, state) {
            stateoptions +=
              "<option value = " + statecode + ">" + state + "</option>";
          });
          $("#state").html(stateoptions);
        });
      }

      else if ($(this).val() == "US") {
        $.getJSON("us_state.json", function (data) {
          $.each(data, function (statecode, state) {
            stateoptions +=
              "<option value = " + statecode + ">" + state + "</option>";
          });
          $("#state").html(stateoptions);
        });
      }
    });

    $("#state").change(function () {
      if ($(this).val() == "MP") {
        x = "";

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

{
  /* <script>

      $(document).ready(function () {

         

          $("#country").change(function () {



                 
                 var val = $(this).val();
                

                if (val == "India") {   
                    $.getJSON('IndianStates.json',function(result){

                        $.each(result,function(statecode,statename){
                            stateoptions += "<option value='"+statecode+"'>"+statename+"</option>";
                        });
                   })
                   $('#state').html(stateoptions);
                }
                else if (val == "England") {

                  $("#state").html("<option value='Northern Ireland'>Northern Ireland</option>\
               <option value='Scotland'>Scotland</option>\
               <option value='Wales'>Wales</option> ");
                }
                else if (val == "Australia") {

                    $("#state").html("<option value='New South Wales'>New South Wales</option>\
                                    <option value='Queensland'>Queensland</option>\
                                    <option value='South South Australia'>South Australia</option> ");
                }
            });

            $("#state").change(function () {
                var sval = $(this).val();
                if (sval == "MadhyaPradesh") {
                    $('#city').html("<option value='select-city'>select-city</option>\
                    <option value='Indore'>Indore</option>\
                <option value='Bhopal'>Bhopal</option>\
                <option value='khandwa'>khandwa</option>\
                <option value='khargone'>khargone</option> ");
                }

               else if (sval == "uttar Pradesh") {
                    $('#city').html("<option value='select-city'>select-city</option>\
                    <option value='kanpur'>kanpur</option>\
                <option value='varanasi'>varanasi</option>\
                <option value='lucknow'>lucknow</option>\
                <option value='amethi'>amethi</option> ");
                };
            });
        });
    </script>   */
}
