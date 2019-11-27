<template>
  <v-app>
      <v-toolbar>
      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn text>Link 1</v-btn>
        <v-btn text>Link 2</v-btn>
        <v-btn text>Link 3</v-btn>
      </v-toolbar-items>

      <template v-if="$vuetify.breakpoint.smAndUp">
        <v-btn icon>
          <v-icon>mdi-export-variant</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-delete-circle</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </template>
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
