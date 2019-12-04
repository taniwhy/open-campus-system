<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-col>
          <v-row align="center" justify="center">
            <div max-width="95%">
              <p style="font-size: 30px;color: #606060;">オープンキャンパスへの参加は初めてですか？</p>
            </div>
          </v-row>
          <v-row align="center" justify="center">
            <v-col>
              <v-btn
                class="white--text"
                flat
                to="/register"
                x-large
                color="light-blue lighten-3"
                width="120px"
              >はい</v-btn>
            </v-col>
            <v-col>
              <v-btn
                class="white--text"
                flat
                to="/branch"
                x-large
                color="light-blue lighten-3"
                width="120px"
              >いいえ</v-btn>
            </v-col>
          </v-row>
        </v-col>
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
