<template>
  <v-app>

  </v-app>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      props: {
        data: Object
      },
      student_check: true,
      school_year_list: ["1学年", "2学年", "3学年", "4学年"],
      graduate_year_list: ["2020年", "2021年", "2022年", "2023年"],
      subject_list: []
    };
  },
  methods: {
    register: function() {
    }
  }
};
</script>

