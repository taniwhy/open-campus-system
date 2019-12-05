<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
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
