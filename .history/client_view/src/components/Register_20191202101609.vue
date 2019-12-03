<template>
  <v-app>
    <v-row style="height: 50px;"></v-row>
    <!-- カード配置用コンテナ -->
    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <!-- フォーム用カード -->
          <v-card ref="form" width="520px">
            <v-card-text>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
              </v-list-item-content>

              <!-- カード配置用コンテナ -->
              <div v-if="!success">
                  <p style="text-align: center;color: #FF3366	">※入力されていない項目があります</p>
                </div>
              <v-container style="width: 90%;" fluid>
                <!-- 名前用コンテナ -->
                <v-form ref="test_form">
                  <v-row style="height: 0px;">
                    <p style="text-align: left;color: #222222">お名前</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.family_name"
                        :rules="[required,limit_length_15
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
                        v-model="data.form.first_name"
                        :rules="[required,limit_length_15
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
                    <p style="text-align: left;color: #222222">フリガナ</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.family_name_reading"
                        :rules="[required,limit_length_15
              ]"
                        :error-messages="errorMessages"
                        placeholder="セイ"
                        height="15px"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.first_name_reading"
                        :rules="[required,limit_length_15
              ]"
                        :error-messages="errorMessages"
                        placeholder="メイ"
                        height="15px"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <!-- 生年月日フォーム -->
                  <v-row style="height: 15px;">
                    <p style="text-align: left;color: #222222">生年月日</p>
                  </v-row>

                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-select
                        v-model="data.form.birth_year"
                        :items="data.years_list"
                        label="年"
                        dense
                        solo
                      ></v-select>
                    </v-col>
                    <v-col style="height: 70px;">
                      <v-select
                        v-model="data.form.birth_month"
                        :items="data.months_list"
                        label="月"
                        dense
                        solo
                      ></v-select>
                    </v-col>
                    <v-col style="height: 70px;">
                      <v-select
                        v-model="data.form.birth_day"
                        :items="data.days_list"
                        label="日"
                        dense
                        solo
                      ></v-select>
                    </v-col>
                  </v-row>

                  <!-- 性別フォーム -->
                  <v-row style="height: 10px;">
                    <p style="text-align: left;color: #222222">性別</p>
                  </v-row>
                  <v-radio-group row>
                    <v-radio label="男" @change="dataform.gender=false"></v-radio>
                    <v-radio label="女" @change="data.form.gender=true"></v-radio>
                  </v-radio-group>

                  <!-- 電話番号フォーム -->
                  <v-row style="height: 0px;">
                    <p style="text-align: left;color: #222222">電話番号</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.phone_number"
                        :rules="[required,digit_check,limit_length_10
              ]"
                        required
                        height="15px"
                        placeholder="入力してください"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <!-- 郵便番号フォーム -->
                  <v-row style="height: 0px;">
                    <p style="text-align: left;color: #222222">郵便番号</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.postal_code"
                        :rules="[required,digit_check,limit_length_7
              ]"
                        required
                        height="15px"
                        placeholder="入力してください"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <!-- 住所フォーム -->
                  <v-row style="height: 0px;">
                    <p style="text-align: left;color: #222222">住所</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        v-model="data.form.street_address"
                        :rules="[required,limit_length_30
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
                    <p style="text-align: left;color: #222222">番地/建物名</p>
                  </v-row>
                  <v-row style="height: 70px;">
                    <v-col style="height: 70px;">
                      <v-text-field
                        ref="zip"
                        v-model="data.form.address"
                        :rules="[limit_length_30
            ]"
                        height="15px"
                        placeholder="任意"
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <!-- 職業フォーム -->
                  <v-row style="height: 10px;">
                    <p style="text-align: left;color: #222222">職業</p>
                  </v-row>
                  <v-radio-group row>
                    <v-radio
                      label="学生"
                      value="yes1"
                      @change="data.student_check = true, form.job=false"
                    ></v-radio>
                    <v-radio
                      label="その他"
                      value="no1"
                      @change="data.student_check = false, form.job=true"
                    ></v-radio>
                  </v-radio-group>

                  <!-- 職業が学生なら表示 -->
                  <div v-if="data.student_check">
                    <v-row style="height: 10px;">
                      <p style="text-align: left;color: #222222">学校名</p>
                    </v-row>
                    <v-text-field
                      v-model="data.form.school_name"
                      :rules="[required,limit_length_30
            ]"
                      placeholder="入力してください"
                      height="15px"
                      required
                    ></v-text-field>
                    <v-row style="height: 25px;">
                      <p style="text-align: left;color: #222222">学年</p>
                    </v-row>
                    <v-select
                      :items="data.school_year_list"
                      v-model="data.form.school_year"
                      dense
                      solo
                      label="選択してください"
                    ></v-select>
                    <v-row style="height: 25px;">
                      <p style="text-align: left;color: #222222">卒業予定年</p>
                    </v-row>
                    <v-select
                      :items="data.graduate_year_list"
                      v-model="data.form.school_graduate_year"
                      dense
                      solo
                      label="選択してください"
                    ></v-select>
                  </div>

                  <!-- 職業がその他なら表示 -->
                  <div v-if="!data.student_check">
                    <v-row style="height: 2px;">
                      <p style="text-align: left;color: #222222">高校卒業済み</p>
                    </v-row>
                    <v-radio-group v-model="row" row>
                      <v-radio label="はい" @change="data.form.graduate_check=true"></v-radio>
                      <v-radio label="いいえ" @change="data.form.graduate_check=false"></v-radio>
                    </v-radio-group>
                    <v-row style="height: 0px;">
                      <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                    </v-row>
                    <v-radio-group v-model="row" row>
                      <v-radio label="はい" @change="data.form.graduate_qualification=true"></v-radio>
                      <v-radio label="いいえ" @change="data.form.graduate_qualification=false"></v-radio>
                    </v-radio-group>
                  </div>

                  <!-- 参加希望学科フォーム -->
                  <v-row style="height: 25px;">
                    <p style="text-align: left;color: #222222">参加希望学科</p>
                  </v-row>
                  <v-select
                    :items="data.subject_list"
                    v-model="data.join_subject"
                    label="選択してください"
                    dense
                    solo
                  ></v-select>

                  <!-- 登録ボタン -->
                  <v-card-actions>
                    <v-col align="center" justify="start">
                      <v-btn
                        class="white--text"
                        x-large
                        color="light-blue lighten-3"
                        width="120px"
                        v-on:click="submit"
                      >確認</v-btn>
                    </v-col>
                  </v-card-actions>
                </v-form>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    {{success}}
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      is_null: value => value == null || "必ず選択してください",
      required: value => !!value || "必ず入力してください",
      digit_check: value =>
        value.match(/^\d+$/) || "半角数字のみを入力してください",
      limit_length_7: value => value.length == 7 || "7桁で入力してください",
      limit_length_10: value => value.length == 10 || "10桁で入力してください",
      limit_length_11: value =>
        value.length <= 11 || "11文字以内で入力してください",
      limit_length_15: value =>
        value.length <= 15 || "15文字以内で入力してください",
      limit_length_30: value =>
        value.length <= 30 || "30文字以内で入力してください",
      success: false
    };
  },

  props: {
    data: Object
  },
  mounted: function() {
    this.create_birth();
    axios
      .get("http://127.0.0.1:8000/api/subject/")
      .then(response => this.subject_push(response.data));
  },
  methods: {
    create_birth: function() {
      for (var y = 2019; y > 1900; y--) {
        this.data.years_list.push(y);
      }
      for (var m = 1; m < 13; m++) {
        this.data.months_list.push(m);
      }
      for (var d = 1; d < 32; d++) {
        this.data.days_list.push(d);
      }
    },
    subject_push: function(response) {
      for (var key in response) {
        this.data.subject_list.push(response[key].subject_name);
      }
    },
    submit() {
      if (this.$refs.test_form.validate()) {
        this.success = true;
      } else {
        this.success = false;
      }
    }
  }
};
</script>

