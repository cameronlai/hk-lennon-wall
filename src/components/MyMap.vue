<template>
  <div>
    <l-map style="width: 500px; height: 500px;" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker :lat-lng="marker">
        <l-popup :content="text">
        </l-popup>
      </l-marker>
      <l-marker :lat-lng="marker2">
        <l-popup :content="text2"></l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
import L from "leaflet";

const markers1 = [
  { position: { lng: 22.35, lat: 114.1 } },
  { position: { lng: -1.571045, lat: 47.457809 } },
  { position: { lng: -1.560059, lat: 47.739323 } }
];

export default {
  name: "MyMap",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  props: {
    msg: String
  },
  data() {
    return {
      zoom: 11,
      center: L.latLng(22.35, 114.1),
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      marker: L.latLng(22.35, 114.1),
      text: "this is a marker",
      marker2: L.latLng(22.35, 114.2),
      text2: "this is a marker 2"
    };
  },
  mounted: function() {
    //console.log('mounted');
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
