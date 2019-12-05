<template>
  <v-app>
    <div>
      <v-app-bar color="light-blue lighten-3" dense dark>

        <v-btn
              x-large
              flat
              class="ma-2"
              outlined
              color="#111111"
              v-on:click="$router.back()"
              width="120px"
            >戻る</v-btn>

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
