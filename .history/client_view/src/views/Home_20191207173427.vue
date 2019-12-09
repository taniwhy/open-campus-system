<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-col>
          <v-row align="center" justify="center">
            <div max-width="95%">
              <p style="font-size: 30px;color: #606060; font-family: 'kokoro';">オープンキャンパスへの参加は初めてですか？</p>
            </div>
          </v-row>
          <v-row align="center" justify="center">
            <v-col align="end" cols="5">
              <v-btn class="white--text" to="/register" x-large color="cyan" width="120px">はい</v-btn>
            </v-col>
            <v-col cols="1"></v-col>
            <v-col align="start" cols="5">
              <v-btn class="white--text" to="/re_register" x-large color="cyan" width="120px">いいえ</v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-container>
    </v-content>
  </v-app>
</template>


<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

<script>
export default {
  data: () => ({}),
  mounted: function() {
  /**
   * ブラウザバックの無効化
   */
    history.pushState(null, null, null);
    window.addEventListener("popstate", function() {
      history.pushState(null, null, null);
    });
  }
};
</script>