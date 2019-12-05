<template>
  <v-app>
    <v-btn
      class="white--text"
      x-large
      color="light-blue lighten-3"
      width="120px"
      v-on:click="register"
    >確認</v-btn>
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
      console.log(props.data)
    }
  }
};
</script>

