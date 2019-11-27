<template>
  <v-app>
    v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/login" class="ma-2" outlined color="primary">管理者ログイン</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="height: 80%;">
      <v-row align="center" justify="center" style="height: 100%;">
        <v-col>
          <v-row >
            <v-card width="400px" class="mx-auto mt-5">
              <v-card-title>
                <h1 class="display-1">管理者ログイン</h1>
              </v-card-title>
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
                    <v-btn class="info">ログイン</v-btn>
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
  data: () => ({
    showPassword: false
  })
};
</script>
