<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <v-col align="center" justify="center">全体の参加状況 〇 人</v-col>
        </v-row>
        <v-row>
          <v-row align="center" justify="center">
            <v-col>
              <v-data-table
                align="center"
                justify="center"
                style="max-width: 800px;"
                :headers="headers"
                :items="desserts"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
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
      headers: [
        {
          text: "学科名",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "会場名", value: "venue_name" },
        { text: "参加人数", value: "participant_num" },
        { text: "4年", value: "forth" },
        { text: "3年", value: "third" },
        { text: "2年", value: "second" },
        { text: "1年", value: "first" }
      ],
      desserts: [
        {
          name: "情報スペシャリスト学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: ""
        },
        {
          name: "情報システム学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: ""
        },
        {
          name: "公務員学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: ""
        }
      ]
    };
  }
};
</script>