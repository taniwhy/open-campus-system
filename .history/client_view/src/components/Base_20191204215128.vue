<template>
  <v-app>
    <v-app-bar app color="cyan" dark>
      <v-toolbar-title>Application</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
    </v-app-bar>
    <router-view></router-view>
    <v-footer>
      <v-col class="text-center" cols="12">{{ new Date().getFullYear() }} - OIC</v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  components: {},

  data: () => ({
    drawer: false
  })
};
</script>
