<template>
  <v-app>
    <div>
      <v-app-bar absolutecolor="light-blue lighten-3" dense dark>
         <v-toolbar-title>テスト中</v-toolbar-title>
         <v-spacer></v-spacer>
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
