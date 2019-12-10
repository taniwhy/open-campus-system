<!-- ホーム画面のベース -->
<template>
  <v-app>
    <v-app-bar app color="cyan" dark>
      <v-toolbar-title>Okayama Information College</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon to="/login">
        <v-icon>mdi-lock</v-icon>
      </v-btn>
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {};
</script>
