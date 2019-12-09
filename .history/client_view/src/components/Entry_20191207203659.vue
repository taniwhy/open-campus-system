 <!--
 登録済み参加者向けコンポーネント
 登録済み参加者は登録情報の

 遷移元: Register
 遷移先: Register, Home
  -->
<template>
  <v-app>
    <v-content>
      <br />
      <!-- フォーム用カード -->
      <v-card ref="form" class="mx-auto" width="500px" max-width="90%" outlined>
        <v-card-text>
          <v-col align="center" justify="center">
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">参加票フォーム</v-list-item-title>
              <v-list-item-subtitle>※項目は全て入力・選択してください</v-list-item-subtitle>
            </v-list-item-content>
          </v-col>

          <!-- カード配置用コンテナ -->
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
        this.$router.push({ path: "entry_confirmation" });
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
        this.data.form.birth_day != null
      ) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>