<template>
  <div>
    <l-map style="width: 500px; height: 500px;" :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker v-for="item in items" :lat-lng="item.marker">
        <l-popup>
          <div style="width: 200px;">
            <h2>{{item.location}} by {{item.author}}</h2>
            <a :href="item.webUrl" target="_blank">
            <v-img :src="item.photoUrl"></v-img>
            </a>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
import L from "leaflet";
import mapData from "@/data/MapData.json";

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
      text2: "this is a marker 2",
      items: []
    };
  },
  mounted: function() {
    for (var i = 0; i < mapData.length; i++) {
      var item = mapData[i];
      console.log(item);
      item.marker = L.latLng(item.lat, item.long);
      this.items.push(item);
    }
    console.log(mapData);
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
