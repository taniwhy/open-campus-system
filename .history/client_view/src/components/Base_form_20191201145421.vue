<template>
  <div>
    <router-view v-bind:user.sync="user"></router-view>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      data: {
        form: {
          family_name: "aa",
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
      },
      mounted: function() {
        axios
          .get("http://127.0.0.1:8000/api/subject/")
          .then(response => this.subject_push(response.data));
      },
      methods: {
        subject_push: function(response) {
          for (var key in response) {
            this.data.subject_list.push(response[key].subject_name);
          }
        },
      }
    };
  }
};
</script>