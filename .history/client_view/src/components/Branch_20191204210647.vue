<template>
  <v-app>
    <v-row align="center" justify="center" style="width: 100%;">
      <p style="font-size: 30px;color: #606060;">オープンキャンパスへの参加は初めてですか？</p>
    </v-row>
    <v-btn
      class="white--text"
      flat
      to="/register"
      x-large
      color="light-blue lighten-3"
      width="120px"
    >はい</v-btn>
    <v-btn
      class="white--text"
      flat
      to="/branch"
      x-large
      color="light-blue lighten-3"
      width="120px"
    >いいえ</v-btn>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
