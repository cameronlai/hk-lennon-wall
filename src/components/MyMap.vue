<template>
  <div style="width: 100%; height: 500px;">
    <l-map :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker v-for="item in items" :lat-lng="item.marker" :key="item.shortCode">
        <l-popup>
          <div style="width: 250px;">
            <div class="font-weight-thin my-2 body-1">
              <a
                :href="'https://www.instagram.com/p/' + item.shortcode"
                target="_blank"
              >{{item.location}}</a> by
              <a
                :href="'https://www.instagram.com/' + item.username"
                target="_blank"
              >{{item.fullname}}</a>
            </div>
            <div class="font-weight-thin my-2 body-1">
              {{item.likes}} Likes
            </div>
            <a :href="item.webUrl" target="_blank">
              <v-img :src="'https://instagram.com/p/' + item.shortcode + '/media/?size=t'"></v-img>
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
      item.marker = L.latLng(item.lat, item.lng);
      item.mediaurl =
        "https://instagram.com/p/" + item.shortcode + "/media/?size=t";
      this.items.push(item);
    }
  },
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
