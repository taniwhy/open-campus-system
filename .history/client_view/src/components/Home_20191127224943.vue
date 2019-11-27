<template>
  <v-app>
    <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-row
          :align="center"
          :justify="center"
          class="grey lighten-5"
          style="height: 300px;"
        >
          <v-card>
            Column
          </v-card>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Home",
  data: () => ({
  })
};
</script>
