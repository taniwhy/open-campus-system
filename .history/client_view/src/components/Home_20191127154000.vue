<template>
  <v-app>
    <v-col cols="12">
        <v-row justify="center">
          <v-col
            cols="6"
            md="2"
          >
            <div class="my-2">
            <v-btn color="warning" dark>Normal Button</v-btn>
          </div>
          </v-col>

          <v-col
            cols="6"
            md="2"
          >
            <v-select
              v-model="justify"
              :items="justifyAvailable"
              label="Justify"
            ></v-select>
          </v-col>
        </v-row>
      </v-col>
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
