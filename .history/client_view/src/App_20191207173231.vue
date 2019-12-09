<template>
  <v-app>
    <router-view></router-view>
  </v-app>
</template>
<script>
/**
 * 全てのページのベース
 */
import { Component, Vue } from 'vue-property-decorator';
@Component
export default {
  components: {},
  data: () => ({
  })
};
</script>

<script lang='ts'>


<style lang="scss">
* :not(.v-icon) {
  font-family: "Hiragino Kaku Gothic Pro","メイリオ", sans-serif!important;
}
</style>
