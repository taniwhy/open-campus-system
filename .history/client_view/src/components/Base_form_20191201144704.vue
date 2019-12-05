<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
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
  }
};
</script>