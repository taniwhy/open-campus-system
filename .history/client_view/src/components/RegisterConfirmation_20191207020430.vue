<template>
  <v-app>
    <v-content>
      <br />
      <!-- フォーム用カード -->
      <v-card class="mx-auto" width="500px" max-width="90%" outlined>
        <v-card-text>
          <v-col align="center" justify="center">
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">※ご確認ください</v-list-item-title>
            </v-list-item-content>
          </v-col>

          <!-- カード配置用コンテナ -->
          <v-container style="width: 95%;" fluid>
            <v-row style="height: 30px;">
              <p style="text-align: left;">お名前</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.family_name + " " +data.form.first_name}}</h3>
            </v-row>
            <br />
            <!-- フリガナフォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">フリガナ</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3
                style="text-align: left;"
              >{{data.form.family_name_reading + " " + data.form.first_name_reading}}</h3>
            </v-row>
            <br />

            <!-- 生年月日フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">生年月日</p>
            </v-row>

            <v-row style="height: 20px;" justify="center">
              <h3
                style="text-align: left;"
              >{{data.form.birth_year + "年" + data.form.birth_month + "月" + data.form.birth_day + "日"}}</h3>
            </v-row>
            <br />

            <!-- 性別フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">性別</p>
            </v-row>
            <div v-if="data.form.gender">
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">女</h3>
              </v-row>
              <br />
            </div>
            <div v-if="!data.form.gender">
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">男</h3>
              </v-row>
              <br />
            </div>

            <!-- 電話番号フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">電話番号</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.phone_number}}</h3>
            </v-row>
            <br />

            <!-- 郵便番号フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">郵便番号</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.postal_code}}</h3>
            </v-row>
            <br />

            <!-- 住所フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">住所</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.street_address}}</h3>
            </v-row>
            <br />

            <!-- 番地/建物名フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">番地/建物名</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.address}}</h3>
            </v-row>
            <br />

            <!-- 職業フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">職業</p>
            </v-row>
            <div v-if="data.student_check">
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">学生</h3>
              </v-row>
              <br />
            </div>
            <div v-if="!data.student_check">
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">その他</h3>
              </v-row>
              <br />
            </div>

            <!-- 職業が学生なら表示 -->
            <div v-if="data.student_check">
              <v-row style="height: 30px;">
                <p style="text-align: left;">学校名</p>
              </v-row>
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">{{data.form.school_name}}</h3>
              </v-row>
              <br />

              <v-row style="height: 30px;">
                <p style="text-align: left;">学年</p>
              </v-row>
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">{{data.form.school_year}}</h3>
              </v-row>
              <br />

              <v-row style="height: 30px;">
                <p style="text-align: left;">卒業予定年</p>
              </v-row>
              <v-row style="height: 20px;" justify="center">
                <h3 style="text-align: left;">{{data.form.graduate_year}}</h3>
              </v-row>
              <br />
            </div>

            <!-- 職業がその他なら表示 -->
            <div v-if="!data.student_check">
              <v-row style="height: 30px;">
                <p style="text-align: left;">高校卒業済み</p>
              </v-row>
              <div v-if="data.form.graduate_check">
                <v-row style="height: 20px;" justify="center">
                  <h3 style="text-align: left;">はい</h3>
                </v-row>
                <br />
              </div>
              <div v-if="!data.form.graduate_check">
                <v-row style="height: 20px;" justify="center">
                  <h3 style="text-align: left;">いいえ</h3>
                </v-row>
                <br />
              </div>
              <v-row style="height: 30px;">
                <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
              </v-row>
              <div v-if="data.form.graduate_qualification">
                <v-row style="height: 20px;" justify="center">
                  <h3 style="text-align: left;">はい</h3>
                </v-row>
                <br />
              </div>
              <div v-if="!data.form.graduate_qualification">
                <v-row style="height: 20px;" justify="center">
                  <h3 style="text-align: left;">いいえ</h3>
                </v-row>
                <br />
              </div>
            </div>

            <!-- 参加希望学科フォーム -->
            <v-row style="height: 30px;">
              <p style="text-align: left;">参加希望学科</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.join_subject}}</h3>
            </v-row>
            <br />
            <br />
            <br />

            <v-row align="center" justify="center">
              <div max-width="95%">
                <p style="font-size: 20px;color: #FF5252; font-weight: 600;">※こちらでよろしいですか？</p>
              </div>
              <v-card-actions>
                <v-col>
                  <v-btn
                    class="white--text"
                    x-large
                    app
                    color="cyan"
                    dark
                    width="120px"
                    v-on:click="form_post"
                    @click="overlay = true"
                  >登録する</v-btn>
                </v-col>
                <v-col>
                  <v-btn
                    class="white--text"
                    x-large
                    app
                    color="cyan"
                    dark
                    width="120px"
                    v-on:click="$router.back()"
                  >編集する</v-btn>
                </v-col>
              </v-card-actions>
            </v-row>
            <!-- 登録ボタン -->
          </v-container>
        </v-card-text>
      </v-card>
      <div class="text-center">
        <v-overlay :value="overlay" color="grey darken-4">
          <div v-if="loading">
            <v-progress-circular :size="50" color="light-blue lighten-3" indeterminate></v-progress-circular>
          </div>
          <div v-if="succeeded_register">
            <h2>登録完了しました!</h2>
            <v-btn x-large flat to="/" class="ma-2" app color="cyan" dark width="120px">OK</v-btn>
          </div>
          <div v-if="failed_register">
            <h2>登録が成功しませんでした。</h2>
            <h2>もう一度最初からお願いします。</h2>
            <v-btn x-large flat to="/" class="ma-2" app color="cyan" dark width="120px">戻る</v-btn>
          </div>
        </v-overlay>
      </div>
      <br />
    </v-content>
  </v-app>
</template>

<script>
import axios from "axios";
import settings from "..//local_settings.json";

export default {
  props: {
    /**
     * バインディングデータ
     */
    data: Object
  },
  data() {
    return {
      /**
       * ヘッダーに付与する認証情報
       * @type {json}
       */
      settings: settings,
      /**
       * POST送信時に付与するパラメタ
       * @type {json}
       */
      form: {},
      /**
       * POST送信時のフォームに付与する生年月日フィールド
       * @type {String}
       */
      birthday: null,
      /**
       * POST送信時のローディング用オーバーレイ表示判定
       * @type {Boolean}
       */
      overlay: false,
      /**
       * ローディングアニメーション表示判定
       * @type {Boolean}
       */
      loading: true,
      /**
       * 登録成功表示判定
       * @type {Boolean}
       */
      succeeded_register: false,
      /**
       * 登録失敗表示判定
       * @type {Boolean}
       */
      failed_register: false
    };
  },
  methods: {
    /**
     * POST送信時に付与するパラメタのフォーマット
     */
    form_format() {
      this.birthday =
        this.data.form.birth_year +
        "-" +
        this.data.form.birth_month +
        "-" +
        this.data.form.birth_day;
      this.form = {
        family_name: this.data.form.family_name,
        first_name: this.data.form.first_name,
        family_name_reading: this.data.form.family_name_reading,
        first_name_reading: this.data.form.first_name_reading,
        birthday: this.birthday,
        gender: this.data.form.gender,
        phone_number: this.data.form.phone_number,
        postal_code: this.data.form.postal_code,
        street_address: this.data.form.street_address,
        address: this.data.form.address,
        job: this.data.form.job,
        school_name: this.data.form.school_name,
        school_year: this.data.form.school_year,
        graduate_year: this.data.form.graduate_year,
        graduated_check: this.data.form.graduate_check,
        graduate_qualification: this.data.form.graduate_qualification
      };
    },
    /**
     * 参加者情報のbhgbbbbbbbbb５６ＭＭＭＭＭPOST送信
     */
    form_post() {
      this.form_format();
      console.log(this.form);
      axios
        .post("http://127.0.0.1:8000/api/participant/", this.form, {
          auth: { username: settings["name"], password: settings["pass"] }
        })
        .then(response => this.succeeded_registerd(response))
        .catch(error => this.failed_register(error));
        F
    },
    succeeded_registerd(response) {
      console.log(response);
      this.loading = false;
      this.succeeded_register = true;
    },
    failed_register(error) {
      console.log(error);
      this.loading = false;
      this.failed_register = true;
    }
  }
};
</script>