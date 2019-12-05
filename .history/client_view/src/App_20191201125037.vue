<template>
  <v-app>
    <div>
      <v-app-bar color="light-blue lighten-3" dense dark>

        <v-toolbar-title>テスト</v-toolbar-title>

      </v-app-bar>
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
