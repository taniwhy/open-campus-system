<template>
  <router-view v-bind:form.sync="form"></router-view>
</template>

<script>
import axios from "axios";

export default {
  name: "Base_form",
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
      subject_list: []
    };
  },
  mounted: function() {
    axios
      .get("http://127.0.0.1:8000/api/subject/")
      .then(response => this.subject_push(response.data));
  },
  methods: {
    subject_push: function(response) {
      for (var key in response) {
        this.subject_list.push(response[key].subject_name);
      }
    }
  }
};
</script>