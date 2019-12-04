<template>
  <v-app>
    <v-app-bar clipped-left color="light-blue lighten-3">
      <v-toolbar-title><p style="color: white; font-size: 30px;">­
        もちもちしたい</p></v-toolbar-title>
    </v-app-bar>
    <router-view></router-view>
    <v-footer padless color="blue-grey lighten-5">
      <v-col class="text-center" cols="12">{{ new Date().getFullYear() }}</v-col>
    </v-footer>
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
