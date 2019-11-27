<template>

  <v-app>
    <v-toolbar>
      <img src="./static/logo.png">
    </v-toolbar>
    <v-content>
      <Home/>
    </v-content>
  </v-app>
</template>

<script>
import Home from './components/Home';

export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>
