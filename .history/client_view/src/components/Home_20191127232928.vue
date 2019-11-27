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
    <v-container style="height: 100%;">
      <v-row style="height: 100%;">
        <v-col>
          <v-row align="center" justify="center" style="height: 60%;">
            <div class="ma-2">
              <v-btn x-large color="cyan" >アンケート開始</v-btn>
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
