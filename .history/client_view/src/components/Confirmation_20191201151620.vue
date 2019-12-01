<template>
  <v-app>
    <!-- 戻るボタン配置用コンテナ -->
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn
              x-large
              flat
              to="/Branch"
              class="ma-2"
              outlined
              color="light-blue lighten-3"
              width="120px"
            >戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>

  </v-app>
</template>

<script>
export default {
  props: {
    data: Object
  }
};
</script>