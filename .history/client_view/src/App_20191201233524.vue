<template>
  <v-app>
    <div>
      <v-app-bar absolute color="light-blue lighten-3" dense dark>
         <v-toolbar-title>テスト中</v-toolbar-title>
    </div>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  })
};
</script>
