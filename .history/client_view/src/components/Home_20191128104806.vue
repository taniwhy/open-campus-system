<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/login" class="ma-2" outlined color="light-blue lighten-3">管理者ログイン</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container style="height: 100%;">
      <v-row style="height: 100%;">
        <v-col>
          <v-row align="center" justify="center" style="height: 60%;">
            <div class="my-2">
              <v-btn class="white--text" flat to="/branch" x-large color="light-blue lighten-3" width=220px height=80px>アンケート開始</v-btn>
            </div>
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
