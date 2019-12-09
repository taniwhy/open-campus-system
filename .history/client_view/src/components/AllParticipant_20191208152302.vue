<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <v-col align="center" justify="center">全体の参加状況{{}}人</v-col>
        </v-row>
        <v-row>
          <v-row align="center" justify="center">
            <v-col align="center" justify="center">
              <v-data-table
                style="max-width: 800px;"
                :headers="headers"
                :items="desserts"
              ></v-data-table>
            </v-col>
          </v-row>
        </v-row>
      </v-col>
    </v-container>
  </v-content>
</template>


<script>
export default {
  data() {
    return {
      entry_number_of_people: 0,
      headers: [
        {
          text: "学科名",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "会場名", value: "venue_name" },
        { text: "参加人数", value: "participant_num" },
        { text: "1年", value: "first" },
        { text: "2年", value: "second" },
        { text: "3年", value: "third" },
        { text: "4年", value: "forth" },
        { text: "既卒", value: "other" },
        { text: "", value: "data-table-expand" }
      ]
    };
  }
};
</script>