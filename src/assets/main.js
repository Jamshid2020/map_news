$(function() {

  $('.ui.search')
  .search({
    // change search endpoint to a custom endpoint by manipulating apiSettings
    apiSettings: {
      url: 'search/?q={query}'
    },
    fields: {
     results : 'items'
   },
   searchFields   : [
         'title'
       ],
    
  })
;

//   var
//   content = [
//     {
//       title: 'Horse',
//       description: 'An Animal',
//     },
//     {
//       title: 'Cow',
//       description: 'Another Animal',
//     }
//   ]
// ;
// $('.ui.search')
//   .search({
//     source : content,
//     searchFields   : [
//       'title'
//     ],
//     fullTextSearch: truex
//   })
// ;


});
mapboxgl.accessToken = 'pk.eyJ1IjoiYm90aXJkZXZlbG9wZXIiLCJhIjoiY2l0d3ZwbHh6MDAyNzNubjJtOG12aGVpcCJ9.vhds9A1UCzV5w-Cy2v198A';
  var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/botirdeveloper/ckhwz3mpz05b019lt3yrbmfif',
      center:[65.105, 41.804],
      zoom:5.5
  });

  var size = 200;

  // implementation of CustomLayerInterface to draw a pulsing dot icon on the map
  // see https://docs.mapbox.com/mapbox-gl-js/api/#customlayerinterface for more info
  var pulsingDot = {
      width: size,
      height: size,
      data: new Uint8Array(size * size * 4),

      // get rendering context for the map canvas when layer is added to the map
      onAdd: function () {
          var canvas = document.createElement('canvas');
          canvas.width = this.width;
          canvas.height = this.height;
          this.context = canvas.getContext('2d');
      },

      // called once before every frame where the icon will be used
      render: function () {
          var duration = 1000;
          var t = (performance.now() % duration) / duration;

          var radius = (size / 2) * 0.3;
          var outerRadius = (size / 2) * 0.7 * t + radius;
          var context = this.context;

          // draw outer circle
          context.clearRect(0, 0, this.width, this.height);
          context.beginPath();
          context.arc(
              this.width / 2,
              this.height / 2,
              outerRadius,
              0,
              Math.PI * 2
          );
          context.fillStyle = 'rgba(255, 200, 200,' + (1 - t) + ')';
          context.fill();

          // draw inner circle
          context.beginPath();
          context.arc(
              this.width / 2,
              this.height / 2,
              radius,
              0,
              Math.PI * 2
          );
          context.fillStyle = 'rgba(255, 100, 100, 1)';
          context.strokeStyle = 'white';
          context.lineWidth = 2 + 4 * (1 - t);
          context.fill();
          context.stroke();

          // update this image's data with data from the canvas
          this.data = context.getImageData(
              0,
              0,
              this.width,
              this.height
          ).data;

          // continuously repaint the map, resulting in the smooth animation of the dot
          map.triggerRepaint();

          // return `true` to let the map know that the image was updated
          return true;
      }
  };

var pointsjson = {
  "type": "FeatureCollection",
  "features": []
};

  map.on('load', function () {
      map.addImage('pulsing-dot', pulsingDot, { pixelRatio: 2 });

      map.addSource('points', {
          'type': 'geojson',
          'data': pointsjson
      });
      map.addLayer({
          'id': 'points',
          'type': 'symbol',
          'source': 'points',
          'layout': {
              'icon-image': 'pulsing-dot'
          }
      });
      map.setLayerZoomRange('points', 2, 15);
  });

var regions = document.querySelectorAll('.region');

for(var i=0; i<regions.length; i++){
  var el = document.createElement('div');
  el.className = "markers";
  el.id = 'marker_'+i

  var popup = new mapboxgl.Popup({ offset: 25 }).setHTML(
  regions[i].getAttribute('data-title')+
  '<br/><a href="'+regions[i].getAttribute('data-link')+'" target="__BLANK">Batafsil</a>'
  );

  var lon_lat = regions[i].getAttribute('data-loc').split(",");
  new mapboxgl.Marker(el)
  .setLngLat(lon_lat)
  .setPopup(popup) // sets a popup on this marker
  .addTo(map);


  regions[i].onclick = function(){


      lon_lat = this.getAttribute('data-loc').split(",");
      //console.log(lon_lat);
      new_point = {
          'type': 'Feature',
          'geometry': {
              'type': 'Point',
              'coordinates': lon_lat
          }
      };
      is_new = true;

      for(var j=0; j < pointsjson.features.length; j++){
        var a = pointsjson.features[j]['geometry']['coordinates'];
        console.log(a);
        if (a[0] == lon_lat[0] && a[1] == lon_lat[1]){
          pointsjson.features.splice(j, 1);
          is_new = false;
        }
      }
      if (is_new){
          pointsjson.features.push(new_point);
      }

      map.getSource('points').setData(pointsjson);

  }
}
