<template>
  <div id="app">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <div class="flex display-2 font-weight-black">HK Lenon Wall Map</div>
        </v-flex>
        <v-flex xs12>
          <my-map></my-map>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import MyMap from "./components/MyMap.vue";

export default {
  name: "app",
  components: {
    MyMap
  },
  data() {},
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

