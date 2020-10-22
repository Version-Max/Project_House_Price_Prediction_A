function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.location;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}



function myFunction() {

/* -- A -- */
if (document.getElementById('Bed1').checked) {
  Bedrooms = 1;
}

else if (document.getElementById('Bed2').checked) {
  Bedrooms = 2;
}

else if (document.getElementById('Bed3').checked) {
  Bedrooms = 3;
}

/* -- B -- */
if (document.getElementById('Bath1').checked) {
  Bath = 1;
}

else if (document.getElementById('Bath2').checked) {
  Bath = 2;
}

else if (document.getElementById('Bath3').checked) {
  Bath = 3;
}

Price = 'Hello';

Sqft = document.getElementById('sqft').value

Location = document.getElementById('uiLocations').value
//alert('Before price predict')



/* Works for Sure!!!
var url = "http://127.0.0.1:5000/ask"; 
  $.post(url, { 
      Bed: 15
  },function(data, status) {
  	alert(data.beds)
  	alert('Inside atleast')
  	Price = data.beds
  	alert(Price)
  	document.getElementById("testd").innerHTML = "Price = " + Price;
  });
  */

  var url = "http://127.0.0.1:5000/price_predict"; 
  $.post(url, { 
      bed: Bedrooms,
      sqft: Sqft,
      bath: Bath,
      lcn: Location
  },function(data, status) {
  	Price = data.beds
  	document.getElementById("testd").innerHTML = "Price of the house is " + Price + " USD.";
  	//alert('Inside atleast')
  	//alert(Price)
  });



 /*document.getElementById("testa").innerHTML = "Bedrooms are = " + Bedrooms;
  document.getElementById("testb").innerHTML = "Bathrooms are = " + Bath;
  document.getElementById("testc").innerHTML = "SqFt are = " + Sqft; */
  //document.getElementById("testd").innerHTML = "Price = " + Price;
}

window.onload = onPageLoad;