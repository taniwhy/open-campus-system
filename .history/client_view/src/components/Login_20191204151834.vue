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
                  <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" />
                  <v-text-field
                    v-bind:type="showPassword ?'text' : 'password'"
                    prepend-icon="mdi-lock"
                    append-icon="mdi-eye-off"
                    label="パスワード"
                    @click:append="showPassword = !showPassword"
                  />
                  <v-card-actions>
                    <v-col align="center" justify="start">
                      <v-btn x-large class="info" color="light-blue lighten-3">ログイン</v-btn>
                    </v-col>
                  </v-card-actions>
                </v-form>
              </v-card-text>
            </v-card>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      credentials: {},
      valid: true,
      loading: false,
      showPassword: false
    };
  }
};
</script>
