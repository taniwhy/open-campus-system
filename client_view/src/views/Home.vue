 <!--
 初期表示画面コンポーネント

 アンケートの開始と管理者ログイン画面に移行できる

 遷移元:
 遷移先: Entry, Register
  -->
<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-col>
          <v-row align="center" justify="center">
            <div max-width="95%">
              <p style="font-size: 30px;color: #606060; ">オープンキャンパスへの参加は初めてですか？</p>
            </div>
          </v-row>
          <v-row align="center" justify="center">
            <v-col align="end" cols="5">
              <v-btn class="white--text" to="/register" x-large color="cyan" width="120px">はい</v-btn>
            </v-col>
            <v-col cols="1"></v-col>
            <v-col align="start" cols="5">
              <v-btn class="white--text" to="/entry" x-large color="cyan" width="120px">いいえ</v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  mounted: function() {
    /**
     * ブラウザバックの無効化
     */
    history.pushState(null, null, null);
  }
};
</script>