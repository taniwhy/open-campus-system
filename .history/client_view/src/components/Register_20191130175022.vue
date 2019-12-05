<template>
  <v-app>
    <!-- 戻るボタン配置用コンテナ -->
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
    <!-- カード配置用コンテナ -->
    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <!-- フォーム用カード -->
          <v-card ref="form" width="520px">
            <v-card-text>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
                <v-list-item-subtitle>※項目はすべて入力してください</v-list-item-subtitle>
              </v-list-item-content>

              <!-- カード配置用コンテナ -->
              <v-container style="width: 90%;" fluid>
                <!-- 名前用コンテナ -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">お名前</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="family_name"
                      ref="name"
                      :rules="[
              () => !!family_name || '※入力されていません',
              () => !!family_name && family_name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="姓"
                      required
                      width="100px"
                      height="15px"
                      style="vertical-align: top;"
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="first_name"
                      :rules="[
              () => !!first_name || '※入力されていません',
              () => !!first_name && first_name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="名"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- フリガナフォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">フリガナ</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="family_name_reading"
                      :rules="[
              () => !!family_name_reading || '※入力されていません',
              () => !!family_name_reading && family_name_reading.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="セイ"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="first_name_reding"
                      :rules="[
              () => !!first_name_reding || '※入力されていません',
              () => !!first_name_reding && first_name_reding.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="メイ"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 生年月日フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">生年月日</p>
                </v-row>

                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="birth_year"
                      :rules="[
              () => !!birth_year || '※入力されていません',
              () => 1900 <= birth_year && birth_year <= 2019 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="年"
                      required
                      height="15px"
                      width="100px"
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="birth_year"
                      :rules="[
              () => !!birth_year || '※入力されていません',
              () => 1 <= birth_year && birth_year <= 12 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="月"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="birth_day"
                      :rules="[
              () => !!birth_day || '※入力されていません',
              () => 1 <= birth_day && birth_day <= 31 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="日"
                      required
                      height="15px"
                      width="100px"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 郵便番号フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">郵便番号</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="postal_code"
                      :rules="[
              () => !!postal_code || '※入力されていません',
              () => postal_code.match(/^\d+$/) || '半角数字のみを入力してください',
              () => postal_code.length == 7 || '※7桁で入力してください',
              ]"
                      required
                      height="15px"
                      placeholder="入力してください"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 住所フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">住所</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="street_address"
                      :rules="[
              () => !!street_address || '※入力されていません',
              () => !!street_address && street_address.length <= 32 || '※32文字以内で入力してください',
            ]"
                      placeholder="入力してください"
                      counter
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 番地/建物名フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">番地/建物名</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="zip"
                      v-model="address"
                      :rules="[
              () => !!address || '※入力されていません',
              () => !!address && address.length <= 32 || '※32文字以内で入力してください',
            ]"
                      required
                      height="15px"
                      placeholder="入力してください"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 職業フォーム -->
                <v-row style="height: 10px;">
                  <p style="text-align: left;">職業</p>
                </v-row>
                <v-radio-group row>
                  <v-radio label="学生" value="yes1" @change="student_check = true"></v-radio>
                  <v-radio label="その他" value="no1" @change="student_check = false"></v-radio>
                </v-radio-group>

                <!-- 職業が学生なら表示 -->
                <div v-if="student_check">
                  <v-row style="height: 10px;">
                    <p style="text-align: left;">学校名</p>
                  </v-row>
                  <v-text-field
                    v-model="school_name"
                    :rules="[
              () => !!school_name || '※入力されていません',
              () => !!school_name && school_name.length <= 32 || '※32文字以内で入力してください',
            ]"
                    placeholder="入力してください"
                    counter
                    height="15px"
                    required
                  ></v-text-field>
                  <v-row style="height: 25px;">
                    <p style="text-align: left;">学年</p>
                  </v-row>
                  <v-select :items="gakunen_items" v-model="school_year" filled label="選択してください"></v-select>
                  <v-row style="height: 25px;">
                    <p style="text-align: left;">卒業予定年</p>
                  </v-row>
                  <v-select :items="yotei_items" filled label="選択してください"></v-select>
                </div>

                <!-- 職業がその他なら表示 -->
                <div v-if="!student_check">
                  <v-row style="height: 2px;">
                    <p style="text-align: left;">高校卒業済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="yes2"></v-radio>
                    <v-radio label="いいえ" value="no2"></v-radio>
                  </v-radio-group>
                  <v-row style="height: 0px;">
                    <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="radio-1"></v-radio>
                    <v-radio label="いいえ" value="radio-2"></v-radio>
                  </v-radio-group>
                </div>

                <!-- 参加希望学科フォーム -->
                <v-row style="height: 25px;">
                  <p style="text-align: left;">参加希望学科</p>
                </v-row>
                <v-select :items="gakka_items" filled label="選択してください"></v-select>

                <!-- 登録ボタン -->
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
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      family_name: "",
      first_name: "",
      family_name_reading: "",
      first_name_reding: "",
      birth_year: "",
      birth_month: "",
      birth_day: "a",
      postal_code: "a",
      street_address: "a",
      address: "a",
      job: "",
      school_year: "",

      student_check: true,
      gakunen_items: ["1学年", "2学年", "3学年", "4学年"],
      yotei_items: ["2020年", "2021年", "2022年", "2023年"],
      gakka_items: []
    };
  },
  mounted: function() {
    axios
      .get("http://127.0.0.1:8000/api/subject/")
      .then(response => this.subject_push(response.data))
  },
  methods: {
    subject_push: function(response) {
      for (key in obj) {
            strValue += getValue(obj[key]);
        }
    },
    register: function() {
      console.log(this.school_year);
    }
  }
};
</script>

