<template>
  <v-app>
    <div>
      <v-app-bar color="deep-purple accent-4" dense dark>

        <v-toolbar-title>OIC open campus</v-toolbar-title>

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
