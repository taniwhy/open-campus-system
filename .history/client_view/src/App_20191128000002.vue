<template>
  <v-app>
    <v-content>
      <router-link to="/">Home</router-link> |
      <router-link to="/page1">page1</router-link> |
      <router-link to="/page2">page2</router-link>
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
