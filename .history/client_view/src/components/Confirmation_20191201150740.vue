<template>
  {{data}}
  <v-btn
    x-large
    flat
    class="ma-2"
    outlined
    color="light-blue lighten-3"
    width="120px"
    v-on:click="$router.back()"
  >戻る</v-btn>
</template>

<script>
export default {
  props: {
    data: Object
  }
};
</script>