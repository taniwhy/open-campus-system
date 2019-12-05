<template>
  <v-app>
    <v-content>
      <v-btn
        class="white--text"
        flat
        to="/branch"
        x-large
        app
        color="cyan"
        dark
        width="220px"
        height="80px"
      >アンケート開始</v-btn>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
