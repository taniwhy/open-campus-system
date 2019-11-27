<template>
<v-toolbar>
      <v-toolbar-title>Title</v-toolbar-title>
    </v-toolbar>
  <v-app>
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
