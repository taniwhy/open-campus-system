 <!-- 初回登録用コンポーネント -->
<template>
  <v-app>
    <v-content>
      <br />
      <!-- フォーム表示用カード -->
      <v-card ref="form" class="mx-auto" width="500px" max-width="90%" outlined>
        <v-card-text>
          <v-col align="center" justify="center">
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">初回参加票フォーム</v-list-item-title>
              <v-list-item-subtitle>※項目は全て入力・選択してください</v-list-item-subtitle>
            </v-list-item-content>
          </v-col>
          <!-- バリデーションチェックに通らなかったら表示 -->
          <div v-if="!success && initial">
            <p style="text-align: center; color: #FF3366	">※入力・選択に誤りがあります</p>
          </div>

          <v-container style="width: 90%;" fluid>
            <v-form ref="test_form">
              <!-- 氏名フォーム -->
              <v-row style="height: 5px;">
                <p style="text-align: left;color: #222222">氏名</p>
              </v-row>

              <v-row style="height: 45px;">
                <v-col>
                  <v-text-field
                    v-model="data.form.family_name"
                    :rules="nameRules"
                    placeholder="姓"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>

              <v-row style="height: 70px;">
                <v-col>
                  <v-text-field
                    v-model="data.form.first_name"
                    :rules="nameRules"
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
                    :rules="nameReadingRules"
                    placeholder="セイ"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col style="height: 70px;">
                  <v-text-field
                    v-model="data.form.first_name_reading"
                    :rules="nameReadingRules"
                    placeholder="メイ"
                    height="15px"
                  ></v-text-field>
                </v-col>
              </v-row>

              <!-- 生年月日フォーム -->
              <v-row style="height: 20px;">
                <p style="text-align: left;color: #222222">生年月日</p>
              </v-row>

              <v-row style="height: 60px;">
                <v-col>
                  <v-select
                    style="min-width: 150px"
                    v-model="data.form.birth_year"
                    :items="data.years_list"
                    :rules="birthdayRules"
                    label="年"
                    dense
                    solo
                  ></v-select>
                </v-col>
              </v-row>
              <v-row style="height: 60px;">
                <v-col>
                  <v-select
                    v-model="data.form.birth_month"
                    :items="data.months_list"
                    :rules="birthdayRules"
                    style="min-width: 150px"
                    label="月"
                    dense
                    solo
                  ></v-select>
                </v-col>
              </v-row>
              <v-row style="height: 70px;">
                <v-col>
                  <v-select
                    v-model="data.form.birth_day"
                    :items="data.days_list"
                    :rules="birthdayRules"
                    style="min-width: 150px"
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
              <v-radio-group v-model="data.picked" :rules="genderRules" row>
                <v-radio id="gender" value="false" label="男" @change="data.form.gender=false"></v-radio>
                <v-radio id="gender" value="true" label="女" @change="data.form.gender=true"></v-radio>
              </v-radio-group>

              <!-- 携帯電話番号フォーム -->
              <v-row style="height: 0px;">
                <p style="text-align: left;color: #222222">携帯電話番号</p>
              </v-row>
              <v-row style="height: 70px;">
                <v-col style="height: 70px;">
                  <v-text-field
                    v-model="data.form.phone_number"
                    :rules="phoneNumberRules"
                    placeholder="入力してください"
                    height="15px"
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
                    :rules="postalCodeRules"
                    placeholder="入力してください"
                    height="15px"
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
                    :rules="addressRules"
                    placeholder="入力してください"
                    height="15px"
                    counter
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
                    :rules="addressRules"
                    placeholder="入力してください"
                    height="15px"
                    counter
                  ></v-text-field>
                </v-col>
              </v-row>

              <!-- 職業フォーム -->
              <v-row style="height: 10px;">
                <p style="text-align: left;color: #222222">職業</p>
              </v-row>
              <v-radio-group v-model="data.picked_job" :rules="radioRules" row>
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
                  :rules="inputRules"
                  placeholder="入力してください"
                  height="15px"
                ></v-text-field>
                <v-row style="height: 25px;">
                  <p style="text-align: left;color: #222222">学年</p>
                </v-row>
                <v-select
                  v-model="data.form.school_year"
                  :items="data.school_year_list"
                  :rules="selectRules"
                  dense
                  solo
                  label="選択してください"
                ></v-select>
                <v-row style="height: 25px;">
                  <p style="text-align: left;color: #222222">卒業予定年</p>
                </v-row>
                <v-select
                  v-model="data.form.graduate_year"
                  :items="data.graduate_year_list"
                  :rules="selectRules"
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
                <v-radio-group row v-model="data.picked_guraduate_check" :rules="radioRules">
                  <v-radio label="はい" @change="data.form.graduate_check=true"></v-radio>
                  <v-radio label="いいえ" @change="data.form.graduate_check=false"></v-radio>
                </v-radio-group>
                <v-row style="height: 0px;">
                  <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                </v-row>
                <v-radio-group row v-model="data.picked_graduate_qualification" :rules="radioRules">
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
                    v-model="data.join_subject"
                    :items="data.subject_list"
                    :rules="selectRules"
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
                    v-on:click="submit"
                    class="white--text"
                    x-large
                    app
                    color="cyan"
                    dark
                    width="120px"
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
export default {
  props: {
    /**
     * バインディングデータ
     */
    data: Object
  },
  data() {
    return {
      nameRules: [
        v => !!v || "必ず入力してください",
        v => (v && v.length <= 15) || "15文字以内で入力してください"
      ],
      nameReadingRules: [
        v => !!v || "必ず入力してください",
        v =>
          (v && v.match(/^[ア-ン゛゜ァ-ォャ-ョー「」、]+$/)) ||
          "カタカナのみを入力してください",
        v => (v && v.length <= 15) || "15文字以内で入力してください"
      ],
      birthdayRules: [v => !!v || "必ず選択してください"],
      genderRules: [v => !!v || "必ず選択してください"],
      phoneNumberRules: [
        v => !!v || "必ず入力してください",
        v => (v && v.match(/^\d+$/)) || "半角数字のみを入力してください",
        v => (v && v.length == 11) || "11桁で入力してください"
      ],
      postalCodeRules: [
        v => !!v || "必ず入力してください",
        v => (v && v.match(/^\d+$/)) || "半角数字のみを入力してください",
        v => (v && v.length == 7) || "７桁で入力してください"
      ],
      addressRules: [
        v => !!v || "必ず入力してください",
        v => (v && v.length <= 30) || "30文字以内で入力してください"
      ],
      radioRules: [v => v != null || "必ず選択してください"],
      selectRules: [v => !!v || "必ず選択してください"],
      inputRules: [
        v => (v && v.length <= 30) || "30文字以内で入力してください"
      ],

      initial: false,
      success: false
    };
  },
  methods: {
    submit() {
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
        this.data.form.job != null &&
        this.data.join_subject != null
      ) {
        if (this.data.form.job == false) {
          if (
            this.data.form.school_name != "" &&
            this.data.form.school_year != "" &&
            this.data.form.graduate_year != ""
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

