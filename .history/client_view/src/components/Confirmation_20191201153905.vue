<template>
  <v-app>
    <!-- カード配置用コンテナ -->
    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <!-- フォーム用カード -->
          <v-card ref="form" width="520px">
            <v-card-text>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">確認画面</v-list-item-title>
              </v-list-item-content>

              <!-- カード配置用コンテナ -->
              <v-container style="width: 90%;" fluid>
                <v-row style="height: 20px;">
                  <p style="text-align: left;">お名前</p>
                </v-row>
                 <v-row style="height: 20px;">
                  <h2 style="text-align: left;">お名前</h2>
                </v-row>

                <!-- フリガナフォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">フリガナ</p>
                </v-row>

                <!-- 生年月日フォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">生年月日</p>
                </v-row>

                <!-- 郵便番号フォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">郵便番号</p>
                </v-row>

                <!-- 住所フォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">住所</p>
                </v-row>

                <!-- 番地/建物名フォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">番地/建物名</p>
                </v-row>

                <!-- 職業フォーム -->
                <v-row style="height: 20px;">
                  <p style="text-align: left;">職業</p>
                </v-row>

                <!-- 職業が学生なら表示 -->
                <div v-if="data.student_check">
                  <v-row style="height: 20px;">
                    <p style="text-align: left;">学校名</p>
                  </v-row>

                  <v-row style="height: 20px;">
                    <p style="text-align: left;">学年</p>
                  </v-row>
                  <v-row style="height: 20px;">
                    <p style="text-align: left;">卒業予定年</p>
                  </v-row>
                </div>

                <!-- 職業がその他なら表示 -->
                <div v-if="!data.student_check">
                  <v-row style="height: 20px;">
                    <p style="text-align: left;">高校卒業済み</p>
                  </v-row>

                  <v-row style="height: 20px;">
                    <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                  </v-row>
                </div>

                <!-- 参加希望学科フォーム -->
                <v-row style="height: 25px;">
                  <p style="text-align: left;">参加希望学科</p>
                </v-row>

                <!-- 登録ボタン -->
                <v-card-actions>
                  <v-col align="center" justify="start">
                    <v-btn
                      class="white--text"
                      x-large
                      color="light-blue lighten-3"
                      width="120px"
                      v-on:click="$router.push('/confirmation')"
                    >確認</v-btn>
                  </v-col>
                </v-card-actions>
                <v-card-actions>
                  <v-col align="center" justify="start">
                    <v-btn
                      class="white--text"
                      x-large
                      color="light-blue lighten-3"
                      width="120px"
                      v-on:click="$router.push('/confirmation')"
                    >確認</v-btn>
                  </v-col>
                </v-card-actions>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  props: {
    data: Object
  }
};
</script>