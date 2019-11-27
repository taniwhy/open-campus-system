<template>
  <v-app>
      <v-toolbar dense>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1 class="display-1">管理者ログイン</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" />
        <v-text-field v-bind:type="showPassword ?
          'text' : 'password'" prepend-icon="mdi-lock" append-icon="mdi-eye-off" label="パスワード"
          @click:append="showPassword = !showPassword"/>
        <v-card-actions>
          <v-btn class="info">ログイン</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</v-app>
</template>

<script>

export default {
  name: 'Login',
  data: () => ({
    showPassword : false
  }),
};
</script>
