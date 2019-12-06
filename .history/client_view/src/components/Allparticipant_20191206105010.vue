<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col class="shrink">
          <v-data-table
    :headers="headers"
    :items="desserts"
    :sort-by="['calories', 'fat']"
    :sort-desc="[false, true]"
    multi-sort
    class="elevation-1"
  ></v-data-table>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>


<script>
export default {
  data: () => ({})
};
</script>
