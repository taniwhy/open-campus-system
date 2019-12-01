<template>
  <v-app>名前: {{ data.form.family_name }}</v-app>
</template>

<script>
export default {
  props: {
    data: Object
  }
};
</script>

