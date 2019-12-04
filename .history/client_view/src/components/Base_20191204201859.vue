<template>
  <v-app>
    <v-app-bar clipped-left color="cyan accent-2">
      <v-toolbar-title><p style="color: white;">テスト中</p></v-toolbar-title>
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
