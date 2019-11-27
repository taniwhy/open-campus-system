<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/Branch" class="ma-2" outlined color="primary">戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <v-card class="mx-auto" max-width="500" outlined>
      <v-list-item three-line>
        <v-list-item-content>
          <v-list-item-title class="headline mb-1">参加票入力</v-list-item-title>
          <v-list-item-subtitle>※全ての項目に対して、入力・選択を行ってください。</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          <v-form v-model="valid">
            <v-container>
              お名前
              <v-row>
                <v-col>
                  <v-text-field label="姓" outlined dense></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field label="名" outlined dense></v-text-field>
                </v-col>
              </v-row>フリガナ
              <v-row>
                <v-col>
                  <v-text-field label="セイ" outlined dense></v-text-field>
                </v-col>
                <v-col>
                  <v-text-field label="メイ" outlined dense fonr-size=1></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "Register",
  data: () => ({})
};
</script>
