<template>
  <div id="app">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <h1 class="text-sm-left">HK Lenon Wall Map Visualization</h1>
        </v-flex>
        <v-flex xs12>
          <MyMap class="text-md-center" />
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
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
