<template>
  <v-app>
  <v-card>
    <v-card-title>
      <h1 class="display-1">ログイン</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field label="ユーザ名" />
        <v-text-field type="password" label="パスワード" />
        <v-card-actions>
          <v-btn>ログイン</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    //
  }),
};
</script>
