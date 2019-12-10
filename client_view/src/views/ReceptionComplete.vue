 <!--
 受付終了確認コンポーネント

 参加表入力が済んだ参加者に事前アンケートに答えてもらうか
 このまま受付終了するか選択してもらう

 遷移元: ParticipantConfirmation, RegisterConfirmation, ChangingConfirmation
 遷移先: Home
  -->
<template>
  <v-app>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <div max-width="95%">
            <p style="font-size: 30px;color: #ff0000; ">※この画面を受付にご提示ください。</p>
            <p style="font-size: 30px;color: #606060;">
              受付が完了しました。
              <br />事前アンケートにご協力ください。
            </p>
          </div>
        </v-row>
        <v-row align="center" justify="center">
          <v-col align="end" cols="5">
            <v-btn class="white--text" to="/" x-large color="cyan" width="150px">終了</v-btn>
          </v-col>
          <v-col cols="1"></v-col>
          <v-col align="start" cols="5">
            <v-btn class="white--text" x-large color="cyan" width="150px">事前アンケート</v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-container>
  </v-app>
</template>

<script>

export default {
  data: () => ({}),
  mounted() {
    /**
     * ブラウザバックの無効化
     */
    history.pushState(null, null, null);
  },
};
</script>