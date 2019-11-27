<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/" class="ma-2" outlined color="primary">戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="height: 100%;">
      <v-row>
        <v-col>
          <v-row align="center" justify="center" style="width: 100%;">オープンキャンパスへの参加は初めてですか？</v-row>
        </v-col>
      </v-row>
      <v-row height="100px">
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/" class="ma-2" outlined color="primary" width="100px">はい</v-btn>
          </v-row>
        </v-col>
        <v-col cols="1"></v-col>
        <v-col>
          <v-row align="center" justify="start" style="width: 100%;">
            <v-btn flat to="/" class="ma-2" outlined color="primary" width="100px">いいえ</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
