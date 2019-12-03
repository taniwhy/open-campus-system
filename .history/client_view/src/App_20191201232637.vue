<template>
  <v-app>
    <div>
      <v-app-bar color="light-blue lighten-3" dense dark>

        <v-btn
              large
              flat
              class="ma-2"
              outlined
              color="white"
              v-on:click="$router.back()"
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
