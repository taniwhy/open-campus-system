<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid  max-width="80%">
        <v-col>
          <v-row align="center" justify="center"  max-width="80%">
            <div max-width="95%">
              <p style="font-size: 30px;color: #606060;">オープンキャンパスへの参加は初めてですか？</p>
            </div>
          </v-row>
          <v-row align="center" justify="center">
            <v-col align="end">
              <v-btn
                class="white--text"
                flat
                to="/register"
                x-large
                color="cyan"
                width="120px"
              >はい</v-btn>
            </v-col >
            <v-col cols="1">
            </v-col>
            <v-col align="start">
              <v-btn
                class="white--text"
                flat
                to="/branch"
                x-large
                color="cyan"
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
