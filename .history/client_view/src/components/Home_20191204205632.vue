<template>
  <v-app>
    <v-content>
      <v-row>
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
