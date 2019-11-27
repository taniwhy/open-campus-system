<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn class="ma-2" outlined color="cyan">管理者ログイン</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container style="height: 200%;">
      <v-row style="height: 200%;">
        <v-col style="height: 200%;">
          <v-row align="center" justify="center">
            <v-btn class="ma-2" outlined color="cyan">管理者ログイン</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
