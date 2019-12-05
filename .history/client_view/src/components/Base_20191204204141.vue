<template>
  <v-app>
    <v-app-bar
      app
      color="cyan"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>
    <router-view></router-view>
    <v-footer app>
      <v-col class="text-center" cols="12">{{ new Date().getFullYear() }} - OIC</v-col>
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
