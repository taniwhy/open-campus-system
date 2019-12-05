<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn x-large flat to="/" class="ma-2" outlined color="light-blue lighten-3" width=120px>戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="height: 100%;">
      <v-row align="center" style="height: 60%;">
        <v-col>
          <v-row>
            <v-col>
              <v-row align="center" justify="center" style="width: 100%;">
                <p style="font-size: 30px;color: #333333;">オープンキャンパスへの参加は初めてですか？</p></v-row>
            </v-col>
          </v-row>
          <v-row height="100px">
            <v-col>
              <v-row align="center" justify="end" style="width: 100%;">
                <div class="my-2">
                  <v-btn class="white--text" flat to="/register" x-large color="light-blue lighten-3" width=120px>はい</v-btn>
                </div>
              </v-row>
            </v-col>
            <v-col cols="1"></v-col>
            <v-col>
              <v-row align="center" justify="start" style="width: 100%;">
                <div class="my-2">
                  <v-btn class="white--text" flat to="/branch" x-large color="light-blue lighten-3" width=120px>いいえ</v-btn>
                </div>
              </v-row>
            </v-col>
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
