 <!-- 登録済み参加者向け確認コンポーネント -->
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
            <v-row style="height: 20px;">
              <p style="text-align: left;">お名前</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.family_name + " " +data.form.first_name}}</h3>
            </v-row>
            <br />

            <!-- 生年月日フォーム -->
            <v-row style="height: 20px;">
              <p style="text-align: left;">生年月日</p>
            </v-row>

            <v-row style="height: 20px;" justify="center">
              <h3
                style="text-align: left;"
              >{{data.form.birth_year + "年" + data.form.birth_month + "月" + data.form.birth_day + "日"}}</h3>
            </v-row>
            <br />

            <!-- 電話番号フォーム -->
            <v-row style="height: 20px;">
              <p style="text-align: left;">電話番号</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.phone_number}}</h3>
            </v-row>
            <br />

            <!-- 郵便番号フォーム -->
            <v-row style="height: 20px;">
              <p style="text-align: left;">郵便番号</p>
            </v-row>
            <v-row style="height: 20px;" justify="center">
              <h3 style="text-align: left;">{{data.form.postal_code}}</h3>
            </v-row>
            <br />

            <!-- 参加希望学科フォーム -->
            <v-row style="height: 25px;">
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
                <p style="font-size: 20px;color: #42A5F5; font-weight: 600;">※上記の入力内容でよろしいですか？</p>
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
                  >OK</v-btn>
                </v-col>
                <v-col>
                  <v-btn
                    class="white--text"
                    x-large
                    app
                    color="cyan"
                    dark
                    width="120px"
                    to="/entry"
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
          <div v-if="form_check">
            <v-progress-circular :size="50" color="light-blue lighten-3" indeterminate></v-progress-circular>
          </div>
          <div v-if="form_create">
            <h2>データが見つかりました</h2>
            <h2>確認してください</h2>
            <v-btn
              x-large
              flat
              to="/participant_confirmation"
              class="ma-2"
              app
              color="cyan"
              dark
              width="120px"
            >確認</v-btn>
          </div>
          <div v-if="form_error">
            <h2>登録データが見つかりませんでした</h2>
            <h2>新しく登録をしてください。</h2>
            <v-btn x-large flat to="/register" class="ma-2" app color="cyan" dark width="120px">OK</v-btn>
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
  data() {
    return {
      settings: settings,
      //送信用フォームのバインディングデータ
      form: {},
      //フォーム用生年月日変数
      birthday: null,
      overlay: false,
      overlay2: false,
      form_check: true,
      form_create: false,
      form_error: false
    };
  },
  //バインディングデータ
  props: {
    data: Object
  },
  methods: {
    //送信用フォームのフォーマット
    form_format: function() {
      this.birthday =
        this.data.form.birth_year +
        "-" +
        this.data.form.birth_month +
        "-" +
        this.data.form.birth_day;
      this.form = {
        family_name: this.data.form.family_name,
        first_name: this.data.form.first_name,
        birthday: this.birthday,
        phone_number: this.data.form.phone_number,
        postal_code: this.data.form.postal_code
      };
    },
    //登録完了処理
    form_post: function() {
      this.form_format();
      axios
        .get(
          "http://127.0.0.1:8000/api/participant/",
          {
            params: this.form
          },
          {
            auth: { username: settings["name"], password: settings["pass"] }
          }
        )
        .then(response => this.found_data(response))
        .catch(response => this.found_not_found(response));
    },
    //データが見つかる
    found_data: function(response) {
      console.log(response.data[0]);
      var birth_buf = response.data[0].birthday.split("-");
      this.data.form = response.data[0];
      this.data.form.birth_year = birth_buf[0];
      this.data.form.birth_month = birth_buf[1];
      this.data.form.birth_day = birth_buf[2];
      console.log(this.data.picked);
      if (response.data[0].gender == false) {
        this.data.picked = "false"
      } else {
        this.data.picked = "true"
      }
      if (response.data[0].job == false) {
        this.data.picked_job = "false"
      } else {
        this.data.picked_job = "true"
      }
      this.form_check = false;
      this.form_create = true;
    },
    //データが見つからない
    found_not_found: function(response) {
      console.log(response);
      this.form_check = false;
      this.form_error = true;
    }
  }
};
</script>