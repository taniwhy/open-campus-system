<template>
  <v-app>名前: {{ data.from.family_name }}</v-app>
</template>

<script>
export default {
  props: {
    data: Object
  }
};
</script>

