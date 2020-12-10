function onClickedEstimatedPrice() {
    console.log('Estimated price button clicked');
    var sqmeter = document.getElementById("sqmeter");
    var bhk = getBHKValue();
    var bath = getBathValue();
    var location = document.getElementById("selectLocation");
    var estimatedPrice = document.getElementById("result");

    //  var url = "http://127.0.0.1:5000/predict_price";
     var url = "/api/predict_price";

  $.post(url, {
      total_sqmeter: parseFloat(sqmeter.value),
      bhk: bhk,
      bath: bath,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estimatedPrice.innerHTML = data.estimated_price.toString() + "$";
      console.log(status);
  });
}

function getBathValue() {
    var rBath = document.getElementsByName("rBath");
    for (var i in rBath) {
        if (rBath[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function getBHKValue() {
    var rBHK = document.getElementsByName("rBHK");
    for (var i in rBHK) {
        if (rBHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/getLocationNames";
    var url = "/api/getLocationNames";
    $.get(url,function(data, status) {
      console.log("got response for getLocationNames request");
      if(data) {
          var locations = data.locations;
          
          var selectLocation = document.getElementById("selectLocation");
          $('#selectLocation').empty();
          for(var i in locations) {
              var option = new Option(locations[i].toUpperCase());
              $('#selectLocation').append(option);
          }
      }
  });
}

window.onload = onPageLoad;