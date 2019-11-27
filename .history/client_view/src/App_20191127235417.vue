<template>
  <v-app>
    <v-content>
      <router-link to="/">Home</router-link>
    </v-content>
  </v-app>
</template>

<script>
import Home from "./components/Home";
import Home from '../components/Home.vue'

export default {
  name: "App",

  components: {
    Home
  },

  data: () => ({
    //
  })
};
</script>
