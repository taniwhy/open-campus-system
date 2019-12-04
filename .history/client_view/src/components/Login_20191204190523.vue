<template>
  <v-app>
    <v-container fluid>
      <v-row style="height: 35px;"></v-row>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn
              x-large
              flat
              to="/"
              class="ma-2"
              outlined
              color="light-blue lighten-3"
              width="120px"
            >戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="height: 50%;">
      <v-row align="center" justify="center" style="height: 100%;">
        <v-col>
          <v-row>
            <v-card width="400px" class="mx-auto mt-5">
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="username"
                    :counter="70"
                    :rules="rules.username"
                    prepend-icon="mdi-account-circle"
                    label="ユーザ名"
                    required
                  />
                  <v-text-field
                    v-model="password"
                    :counter="20"
                    :rules="rules.password"
                    v-bind:type="showPassword ?'text' : 'password'"
                    prepend-icon="mdi-lock"
                    append-icon="mdi-eye-off"
                    label="パスワード"
                    @click:append="showPassword = !showPassword"
                    required
                  />
                  <v-card-actions>
                    <v-col align="center" justify="start">
                      <v-btn
                        x-large
                        class="info"
                        color="light-blue lighten-3"
                        :disabled="!valid"
                        @click="login"
                      >ログイン</v-btn>
                    </v-col>
                  </v-card-actions>
                </v-form>
              </v-card-text>
            </v-card>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <div class="text-center">
      <v-overlay :value="overlay" color="grey darken-4">
        <div v-if="form_check">
          <v-progress-circular :size="50" color="light-blue lighten-3" indeterminate></v-progress-circular>
        </div>
        <div v-if="form_create">
          <h2>ログイン完了</h2>
          <v-btn
            x-large
            flat
            class="ma-2"
            color="light-blue lighten-3"
            width="120px"
            @click="overlay=false"
          >OK</v-btn>
        </div>
        <div v-if="form_error">
          <h2>ログインできませんでした</h2>
          <h2>確認して下さい</h2>
          <v-btn
            x-large
            flat
            class="ma-2"
            color="light-blue lighten-3"
            width="120px"
            @click="overlay=false"
          >戻る</v-btn>
        </div>
      </v-overlay>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";
import settings from "..//local_settings.json";

export default {
  name: "Login",
  data: () => ({
    username: null,
    password: null,
    valid: true,
    loading: false,
    showPassword: false,
    overlay: false,
    overlay2: false,
    form_check: false,
    form_create: false,
    form_error: false,
    form: {},
    rules: {
      username: [
        v => !!v || "ユーザー名は必須です",
        v => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
        v => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
      ],
      password: [
        v => !!v || "パスワードは必須です",
        v => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません"
      ]
    }
  }),
  methods: {
    login() {
      this.overlay = true;
      this.form_check = true;
      this.form_error = false;
      this.form = {
        username: this.username,
        password: this.password
      };
      axios
        .post("http://127.0.0.1:8000/auth/", this.form, {
          auth: { username: settings["name"], password: settings["pass"] }
        })
        .then(response => this.form_created(response))
        .catch(response => this.create_error(response));
    },
    form_created: function(response) {
      console.log(response)
      this.form_check = false;
      this.form_create = true;
      this.$router.push({ path: "admin" });
    },
    create_error: function(response) {
      console.log(response)
      this.form_check = false;
      this.form_error = true;
    }
  }
};
</script>
