<template>
  <v-app>
    <div>
      <v-app-bar color="light-blue lighten-3" dense dark>

        <v-btn
              x-large
              flat
              to="/Branch"
              class="ma-2"
              outlined
              color="#111111"
              width="120px"
            >??</v-btn>

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
