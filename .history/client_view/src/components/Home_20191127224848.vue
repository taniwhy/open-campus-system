<template>
  <v-app>
    <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-row
          :align="alignment"
          :justify="justify"
          class="grey lighten-5"
          style="height: 300px;"
        >
          <v-card
            v-for="n in 3"
            :key="n"
            class="ma-3 pa-6"
            outlined
            tile
          >
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
