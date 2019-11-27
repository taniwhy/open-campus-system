<template>
  <v-app>
    <v-row align="center">
      <v-col class="text-center" cols="12" sm="4">
        <div class="my-2">
          <v-btn text small>Normal</v-btn>
        </div>
        <div class="my-2">
          <v-btn text small color="primary">Primary</v-btn>
        </div>
        <div class="my-2">
          <v-btn text small color="error">Error</v-btn>
        </div>
        <div class="my-2">
          <v-btn text small disabled>Disabled</v-btn>
        </div>
      </v-col>

      <v-col class="text-center" cols="12" sm="4">
        <div class="my-2">
          <v-btn text>Normal</v-btn>
        </div>
        <div class="my-2">
          <v-btn text color="primary">Primary</v-btn>
        </div>
        <div class="my-2">
          <v-btn text color="error">Error</v-btn>
        </div>
        <div class="my-2">
          <v-btn text disabled>Disabled</v-btn>
        </div>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({
    showPassword: false
  })
};
</script>
