<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <div max-width="95%">
          <p style="font-size: 30px;color: #606060;">オープンキャンパスへの参加は初めてですか？</p>
        </div>
        <v-row justify="center">
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
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
