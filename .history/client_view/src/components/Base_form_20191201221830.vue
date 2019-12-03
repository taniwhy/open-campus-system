<template>
  <div>
    <router-view v-bind:data.sync="data"></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {
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
          school_name: null,
          school_year: null,
          graduate_year: null,
          graduate_check: null,
          graduate_qualification: null

        },
        join_subject: null,
        student_check: true,
        years_list: [],
        school_year_list: ["1学年", "2学年", "3学年", "4学年"],
        graduate_year_list: ["2020年", "2021年", "2022年", "2023年"],
        subject_list: []
      },
    }
  },
   mounted() {

    },
};
</script>