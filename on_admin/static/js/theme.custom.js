/* Add here all your JS customizations */

/*function initialize() {

var mapOptions =  {
    center: new google.maps.LatLng(1.340021, 103.825583),
    zoom: 12,
    zoomControl: true,
    zoomControlOptions: {
        style: google.maps.ZoomControlStyle.DEFAULT
    },
    disableDoubleClickZoom: false,
    mapTypeControl: true,
    mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
    },
    scaleControl: false,
    scrollwheel: true,
    panControl: false,
    streetViewControl: false,
    draggable : true,
    overviewMapControl: false,
    
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    styles: [{"featureType": "water","elementType": "geometry","stylers": [{ "color": "#193341" }]},{"featureType": "landscape","elementType": "geometry","stylers": [{ "color": "#2c5a71" }]},{"featureType": "road","elementType": "geometry","stylers": [{ "color": "#29768a" },{ "lightness": -37 }]},{"featureType": "poi","elementType": "geometry","stylers": [{ "color": "#406d80" }]},{"featureType": "transit","elementType": "geometry","stylers": [{ "color": "#406d80" }]},{"elementType": "labels.text.stroke","stylers": [{ "visibility": "on" },{ "color": "#3e606f" },{ "weight": 2 },{ "gamma": 0.84 }]},{"elementType": "labels.text.fill","stylers": [{ "color": "#ffffff" }]},{"featureType": "administrative","elementType": "geometry","stylers": [{ "weight": 0.6 },{ "color": "#1a3541" }]},{"elementType": "labels.icon","stylers": [{ "visibility": "off" }]},{"featureType": "poi.park","elementType": "geometry","stylers": [{ "color": "#2c5a71" }]}]
};

  var map = new google.maps.Map(document.getElementById('gmap'), mapOptions);

  var ctaLayer = new google.maps.KmlLayer({
    url: 'http://accessibility.place/static/SG_SUBZONE.kml'
  });
  ctaLayer.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);*/

var eventHandler = function(data) {

    console.log("success: content(scores) for subzone:" + data.name + " scores:" + data.scores.overall);

    $("#livability-total-score").text(data.scores.overall)
    $("#meterHousing").prev("svg").find("text tspan:first").text(data.scores.Housing);
    $("#meterNeighbourhood").prev("svg").find("text tspan:first").text(data.scores.Neighbourhood);
    $("#meterTransportation").prev("svg").find("text tspan:first").text(data.scores.Transportation);
    $("#meterEnvironment").prev("svg").find("text tspan:first").text(data.scores.Environment);
    $("#meterHealth").prev("svg").find("text tspan:first").text(data.scores.Health);
    $("#meterEngagement").prev("svg").find("text tspan:first").text(data.scores.Engagement);

};

var errorHandler = function(xhr) {
    switch (xhr.status) {
      //Shipping rate api error
      case 400:
      console.log("API error: inside xhr:" + xhr.status + " " + $.parseJSON(xhr.responseText)["error_msg"]);

    break;


  }
};

function getScores(){
  $.ajax("./get_subzone_score", {
    data: {
      subzone: $('#subzone-select').val(),
    },
    success: eventHandler,
    error: errorHandler
  });
  console.log("Inside function getScores");
}


$('#subzone-select').change(function() {
    getScores();
/*  alert('The option with value ' + $(this).val() + ' and text ' + $(this).text() + ' was selected.');
*/
});