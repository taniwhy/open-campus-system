<template>
  <v-app>
    <v-content>
      <v-containerfluid>
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
            >アンケート開始</v-btn>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
