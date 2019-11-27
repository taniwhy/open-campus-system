<template>
  <v-app>
    <header id="header">
      <img src='./static/logo.png' height="1000">
    </header>
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
