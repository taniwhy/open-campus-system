<template>
  <v-app>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-btn
            class="white--text"
            flat
            to="/branch"
            x-large
            app
            color="cyan"
            dark
            width="220px"
            height="80px"
          >アンケートを開始</v-btn>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({
    drawer: null
  }),
  props: {
    drawer: null
  }
};
</script>
