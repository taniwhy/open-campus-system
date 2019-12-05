<template>
  <v-app>
    <v-content>
      <v-row align="center" justify="center">
        <v-col  align="center" justify="center">
          <div class="my-2">
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
          </div>
        </v-col>
      </v-row>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({})
};
</script>
