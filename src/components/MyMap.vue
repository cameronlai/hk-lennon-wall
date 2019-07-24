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
            <div class="font-weight-thin my-2 body-1">{{item.likes}} Likes</div>
            <a :href="'https://www.instagram.com/p/' + item.shortcode" target="_blank">
              <v-img :src="'https://instagram.com/p/' + item.shortcode + '/media/?size=t'"></v-img>
            </a>
            <div class="font-weight-thin my-2 body-1">
              {{item.index}} / {{item.n}}
              <v-btn v-on:click="nextImage(item, -1)">{{ icons.mdiAccount }}</v-btn>
              <v-btn v-on:click="nextImage(item, 1)">Next</v-btn>
            </div>
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
  data() {
    return {
      zoom: 11,
      center: L.latLng(22.35, 114.1),
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      items: []
    };
  },
  mounted: function() {
    var done = false;
    var targetGroup = 0;
    for (var i = 0; i < mapData.length; i++) {
      var item = {};
      for (var k in mapData[i]) item[k] = mapData[i][k];
      if (item.group == targetGroup) {
        item.marker = L.latLng(item.lat, item.lng);
        item.index = 1;
        item.startPos = i;
        this.items.push(item);
        targetGroup++;
      }
    }
  },
  methods: {
    nextImage: function(selectedItem, dir) {
      var newIndex = selectedItem.index + dir;
      if (newIndex > selectedItem.n || newIndex == 0) {
        console.log("leave");
        return;
      }

      selectedItem.index = selectedItem.index + dir;
      var lookupIndex = selectedItem.index + selectedItem.startPos - 1;
      var newItem = mapData[lookupIndex];
      for (var k in newItem) selectedItem[k] = newItem[k];
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
