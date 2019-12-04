<template>
  <v-app>
    <v-app-bar clipped-left color="light-blue lighten-3">
      <img src="../static/OIC.png" height="10px">
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  components: {},

  data: () => ({
    //
  })
};
</script>
