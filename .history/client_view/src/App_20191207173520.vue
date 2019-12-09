<template>
  <v-app>
    <router-view></router-view>
  </v-app>
</template>
<script>
/**
 * 全てのページのベース
 */
export default {
  components: {},
  data: () => ({
  })
};
</script>

<style lang="scss">
* :not(.v-icon) {
  font-family: 'Kosugi';
}
</style>
