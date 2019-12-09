<!-- フォームのベース -->
<template>
  <div>
    <router-view v-bind:data.sync="data"></router-view>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      /**
       * フォームで使用する共通データ
       * @type {Object}
       */
      data: {
        /**
         * APIリクエスト時に付与するパラメタ
         * @type {Object}
         */
        form: {
          family_name: null,
          first_name: null,
          family_name_reading: null,
          first_name_reading: null,
          birth_year: null,
          birth_month: null,
          birth_day: null,
          gender: null,
          phone_number: null,
          postal_code: null,
          street_address: null,
          address: null,
          job: null,
          school_name: "",
          school_year: "",
          graduate_year: "",
          graduate_check: false,
          graduate_qualification: false
        },
        participantHistoryForm: {
          articipant: null,
          join_day: null,
          join_subject: null,
        },
        /**
         * 性別の初期値
         * @type {Boolean}
         */
        picked: null,
        /**
         * 職業の初期値
         * @type {Boolean}
         */
        picked_job: null,
        /**
         * 既卒判定の初期値
         * @type {Boolean}
         */
        picked_guraduate_check: null,
        /**
         * 高認判定の初期値
         * @type {Boolean}
         */
        picked_graduate_qualification: null,
        /**
         * 参加希望学科
         * @type {String}
         */
        join_subject: null,
        /**
         * 学生/既卒フォーム表示判定
         * @type {Boolean}
         */
        student_check: true,
        /**
         * 誕生年のセレクトデータ
         * @type {String}}
         */
        years_list: [],
        /**
         * 誕生月のセレクトデータ
         * @type {String}}
         */
        months_list: [],
        /**
         * 誕生日のセレクトデータ
         * @type {String}}
         */
        days_list: [],
        /**
         * 学年のセレクトデータ
         * @type {String}}
         */
        school_year_list: ["1学年", "2学年", "3学年", "4学年"],
        /**
         * 卒業年のセレクトデータ
         * @type {String}}
         */
        graduate_year_list: ["2020年", "2021年", "2022年", "2023年"],
        /**
         * 参加希望学科のセレクトデータ
         * @type {String}}
         */
        subject_list: []
      }
    };
  },
  created() {
    this.create_birth();
    axios
      .get("http://127.0.0.1:8000/api/subject/")
      .then(response => this.subject_push(response.data));
  },
  methods: {
    create_birth: function() {
      for (var y = 2019; y >= 1900; y--) {
        this.data.years_list.push(y);
      }
      for (var m = 1; m < 13; m++) {
        this.data.months_list.push(m);
      }
      for (var d = 1; d < 32; d++) {
        this.data.days_list.push(d);
      }
    },
    subject_push: function(response) {
      for (var key in response) {
        this.data.subject_list.push(response[key].subject_name);
      }
    }
  }
};
</script>