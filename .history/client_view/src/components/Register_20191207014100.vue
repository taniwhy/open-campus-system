<template>
  <v-app>
    <v-content>
      <br />
      <!-- フォーム用カード -->
      <v-card ref="form" class="mx-auto" width="500px" max-width="90%" outlined>
        <v-card-text>
          <v-col align="center" justify="center">
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
            </v-list-item-content>
          </v-col>

          <!-- カード配置用コンテナ -->
          <div v-if="!success && initial">
            <p style="text-align: center; color: #FF3366	">※入力されていない項目があります</p>
          </div>
          <v-container style="width: 90%;" fluid>
            <!-- 名前用コンテナ -->
            <v-form ref="test_form">
              <v-row style="height: 5px;">
                <p style="text-align: left;color: #222222">お名前</p>
              </v-row>

              <v-row style="height: 45px;">
                <v-col>
                  <v-text-field
                    v-model="data.form.family_name"
                    :rules="[required, limit_length_15
              ]"
                    placeholder="姓"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row style="height: 70px;">
                <v-col>
                  <v-text-field
                    v-model="data.form.first_name"
                    :rules="[required,limit_length_15
              ]"
                    placeholder="名"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>

              <!-- フリガナフォーム -->
              <v-row style="height: 5px;">
                <p style="text-align: left;color: #222222">フリガナ</p>
              </v-row>

              <v-row style="height: 45px;">
                <v-col>
                  <v-text-field
                    v-model="data.form.family_name_reading"
                    :rules="[required,limit_length_15
              ]"
                    placeholder="セイ"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col style="height: 70px;">
                  <v-text-field
                    v-model="data.form.first_name_reading"
                    :rules="[required,limit_length_15
              ]"
                    placeholder="メイ"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>

              <!-- 生年月日フォーム -->
              <v-row style="height: 20px;">
                <p style="text-align: left;color: #222222">生年月日</p>
              </v-row>

              <v-row style="height: 50px;">
                <v-col>
                  <v-select
                    style="min-width: 150px"
                    v-model="data.form.birth_year"
                    :items="data.years_list"
                    label="年"
                    dense
                    solo
                  ></v-select>
                </v-col>
              </v-row>
              <v-row style="height: 50px;">
                <v-col>
                  <v-select
                    style="min-width: 150px"
                    v-model="data.form.birth_month"
                    :items="data.months_list"
                    label="月"
                    dense
                    solo
                  ></v-select>
                </v-col>
              </v-row>
              <v-row style="height: 70px;">
                <v-col>
                  <v-select
                    style="min-width: 150px"
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
              <v-radio-group row v-model="data.picked">
                <v-radio id="gender" value="false" label="男" @change="data.form.gender=false"></v-radio>
                <v-radio id="gender" value="true" label="女" @change="data.form.gender=true"></v-radio>
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
                    height="15px"
                    placeholder="入力してください"
                    required
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
                    v-model="data.form.address"
                    :rules="[limit_length_30
            ]"
                    height="15px"
                    placeholder="入力してください"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>

              <!-- 職業フォーム -->
              <v-row style="height: 10px;">
                <p style="text-align: left;color: #222222">職業</p>
              </v-row>
              <v-radio-group row v-model="data.picked_job">
                <v-radio
                  label="学生"
                  value="false"
                  @change="data.student_check = true, data.form.job = false"
                ></v-radio>
                <v-radio
                  id="onna"
                  label="その他"
                  value="true"
                  @change="data.student_check = false, data.form.job = true"
                ></v-radio>
              </v-radio-group>

              <!-- 職業が学生なら表示 -->
              <div v-if="data.student_check">
                <v-row style="height: 10px;">
                  <p style="text-align: left;color: #222222">学校名</p>
                </v-row>
                <v-text-field
                  v-model="data.form.school_name"
                  :rules="[required, limit_length_30
            ]"
                  placeholder="入力してください"
                  height="15px"
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
                  v-model="data.form.graduate_year"
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
                <v-radio-group row v-model="data.picked_guraduate_check">
                  <v-radio label="はい" @change="data.form.graduate_check=true"></v-radio>
                  <v-radio label="いいえ" @change="data.form.graduate_check=false"></v-radio>
                </v-radio-group>
                <v-row style="height: 0px;">
                  <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                </v-row>
                <v-radio-group row v-model="data.picked_graduate_qualification">
                  <v-radio label="はい" @change="data.form.graduate_qualification=true"></v-radio>
                  <v-radio label="いいえ" @change="data.form.graduate_qualification=false"></v-radio>
                </v-radio-group>
              </div>

              <!-- 参加希望学科フォーム -->
              <v-row style="height: 10px;">
                <p style="text-align: left;color: #222222">参加希望学科</p>
              </v-row>
              <v-row>
                <v-col>
                  <v-select
                    :items="data.subject_list"
                    v-model="data.join_subject"
                    label="選択してください"
                    dense
                    solo
                  ></v-select>
                </v-col>
              </v-row>

              <!-- 登録ボタン -->
              <v-card-actions>
                <v-col align="center">
                  <v-btn
                    class="white--text"
                    x-large
                    app
                    color="cyan"
                    dark
                    width="120px"
                    v-on:click="submit"
                  >確認</v-btn>
                </v-col>
              </v-card-actions>
            </v-form>
          </v-container>
        </v-card-text>
      </v-card>
      <br />
    </v-content>
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
      initial: false,
      success: false
    };
  },
  props: {
    data: Object
  },

  methods: {
    submit() {
      console.log(this.data.form);
      try {
        if (this.$refs.test_form.validate() && this.form_check()) {
          this.success = true;
        } else {
          this.success = false;
          this.initial = true;
          window.scrollTo(0, 0);
        }
      } catch (error) {
        this.initial = true;
        this.success = false;
        window.scrollTo(0, 0);
      }
      if (this.success) {
        this.$router.push({ path: "register_confirmation" });
      }
    },
    scrollBehavior(to, from, savedPosition) {
      if (savedPosition) {
        return savedPosition;
      } else {
        return { x: 0, y: 0 };
      }
    },
    form_check() {
      if (
        this.data.form.birth_year != null &&
        this.data.form.birth_month != null &&
        this.data.form.birth_day != null &&
        this.data.form.gender != null &&
        this.data.form.job != null
      ) {
        if (this.data.form.job == false) {
          if (
            this.data.form.school_name != null &&
            this.data.form.school_year != null &&
            this.data.form.graduate_year != null
          ) {
            return true;
          } else {
            return false;
          }
        } else {
          if (
            this.data.form.graduate_check != null &&
            this.data.form.graduate_qualification != null
          ) {
            return true;
          } else {
            return false;
          }
        }
      } else {
        return false;
      }
    }
  }
};
</script>

