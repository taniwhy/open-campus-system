<template>
  <v-app>
    <header id="header">
    <h1>This is the header.</h1>
    <nav id="header-nav">
    </nav>
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
