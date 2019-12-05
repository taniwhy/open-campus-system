<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn
              x-large
              flat
              to="/Branch"
              class="ma-2"
              outlined
              color="light-blue lighten-3"
              width="120px"
            >戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <v-card ref="form" width="550px">
            <v-card-text>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
                <v-list-item-subtitle>※項目はすべて入力してください</v-list-item-subtitle>
              </v-list-item-content>

              <v-container style="width: 90%;" fluid>
                <v-row >
                  <p style="text-align: left;">お名前</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col >
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="姓"
                      required
                      width="100px"
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="名"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <p style="text-align: left;">フリガナ</p>
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="セイ"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <br />
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="メイ"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <p style="text-align: left;">生年月日</p>
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="年"
                      required
                      width="100px"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <br />
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="月"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <br />
                    <v-text-field
                      ref="name"
                      v-model="name"
                      :rules="[
              () => !!name || '※入力されていません',
              () => !!name && name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="日"
                      required
                      width="100px"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <p style="text-align: left;">郵便番号</p>
                <v-text-field
                  v-model="post"
                  :rules="[
              () => !!post || '※入力されていません',
              () => post.match(/^\d+$/) || '半角数字のみを入力してください',
              () => post.length == 7 || '※7桁で入力してください',
              ]"
                  required
                  placeholder="入力してください"
                ></v-text-field>
                <p style="text-align: left;">住所</p>
                <v-text-field
                  v-model="address"
                  :rules="[
              () => !!address || '※入力されていません',
              () => !!address && address.length <= 32 || '※32文字以内で入力してください',
            ]"
                  placeholder="入力してください"
                  counter
                  required
                ></v-text-field>
                <p style="text-align: left;">番地/建物名</p>
                <v-text-field
                  ref="zip"
                  v-model="zip"
                  :rules="[
              () => !!zip || '※入力されていません',
              () => !!zip && zip.length <= 32 || '※32文字以内で入力してください',
            ]"
                  required
                  placeholder="入力してください"
                ></v-text-field>
                <p style="text-align: left;">職業</p>
                <v-radio-group v-model="row" row>
                  <v-radio label="学生" value="yes1" @change="student_check = true"></v-radio>
                  <v-radio label="その他" value="no1" @change="student_check = false"></v-radio>
                </v-radio-group>
                <p style="text-align: left;">学校名</p>
                <v-text-field
                  v-model="address"
                  :rules="[
              () => !!address || '※入力されていません',
              () => !!address && address.length <= 32 || '※32文字以内で入力してください',
            ]"
                  placeholder="入力してください"
                  counter
                  required
                ></v-text-field>
                <div v-if="student_check">
                  <p style="text-align: left;">学年</p>
                  <v-select :items="gakunen_items" filled label="選択してください"></v-select>
                  <p style="text-align: left;">卒業予定年</p>
                  <v-select :items="yotei_items" filled label="選択してください"></v-select>
                </div>
                <div v-if="!student_check">
                  <p style="text-align: left;">高校卒業済み</p>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="yes2"></v-radio>
                    <v-radio label="いいえ" value="no2"></v-radio>
                  </v-radio-group>
                  <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="radio-1"></v-radio>
                    <v-radio label="いいえ" value="radio-2"></v-radio>
                  </v-radio-group>
                </div>
                <p style="text-align: left;">参加希望学科</p>
                <v-select :items="gakka_items" filled label="選択してください"></v-select>
                <v-card-actions>
                  <v-col align="center" justify="start">
                    <v-btn
                      class="white--text"
                      x-large
                      color="light-blue lighten-3"
                      width="120px"
                      v-on:click="register"
                    >登録</v-btn>
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
  name: "Register",
  data() {
    return {
      student_check: true,
      gakunen_items: ["1学年", "2学年", "3学年", "4学年"],
      yotei_items: ["2020年", "2021年", "2022年", "2023年"],
      gakka_items: [
        "医療福祉事務学科",
        "診療情報管理士学科",
        "ホテルブライダル学科",
        "経営アシスト学科",
        "公務員・公務員速修学科",
        "保育学科",
        "情報スペシャリスト学科",
        "情報システム学科",
        "ゲームクリエイター・ゲームプログラマー学科",
        "データマーケター学科",
        "ネット動画クリエイター学科",
        "CGデザイン学科"
      ],
      form: []
    };
  },
  methods: {
    register: function() {
      console.log(this.yes2);
    }
  }
};
</script>

