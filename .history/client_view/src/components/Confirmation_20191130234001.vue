<template>
  <v-app>
    <!-- カード配置用コンテナ -->
    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <!-- フォーム用カード -->
          <v-card ref="form" width="520px"></v-card>
        </v-col>
      </v-row>
    </v-container>
    <!-- 戻るボタン配置用コンテナ -->
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn
              x-large
              flat
              to="/Register"
              class="ma-2"
              outlined
              color="light-blue lighten-3"
              width="120px"
            >戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import Vue from "vue";
// 『イベントバス』のためのインスタンス
var bus = new Vue();

export default {
  name: "Register",
  data() {
    return {
      form: {
        family_name: null,
        first_name: null,
        family_name_reading: null,
        first_name_reding: null,
        birth_year: null,
        birth_month: null,
        birth_day: null,
        postal_code: null,
        street_address: null,
        address: null,
        job: null,
        school_year: null
      },

      student_check: true,
      school_year_list: ["1学年", "2学年", "3学年", "4学年"],
      graduate_year_list: ["2020年", "2021年", "2022年", "2023年"],
      subject_list: []
    };
  },
  mounted: function() {
    bus.$on("bus-event", this.changeMethod);
  },
  methods: {
    changeMethod: function(message) {
      console.log(message);
      this.message = message;
    }
  }
};
</script>

