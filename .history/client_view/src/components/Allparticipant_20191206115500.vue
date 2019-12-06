<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <v-col align="center" justify="center">全体の参加状況 人</v-col>
        </v-row>
        <v-row>
          <v-row align="center" justify="center">
            <v-col align="center" justify="center">
              <v-data-table
                style="max-width: 800px;"
                :headers="headers"
                :items="desserts"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
                :single-expand="singleExpand"
                :expanded.sync="expanded"
                show-expand
              >
                <template v-slot:top>
                  <v-toolbar flat>
                    <v-toolbar-title>Expandable Table</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-switch v-model="singleExpand" label="Single expand" class="mt-2"></v-switch>
                  </v-toolbar>
                </template>
                <template v-slot:expanded-item="{ headers }">
                  <td :colspan="headers.length">Peek-a-boo!</td>
                </template>
              </v-data-table>
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
        { text: "1年", value: "first" },
        { text: "2年", value: "second" },
        { text: "3年", value: "third" },
        { text: "4年", value: "forth" },
        { text: "既卒", value: "other" }
      ],
      desserts: [
        {
          name: "情報スペシャリスト学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: "",
          other: ""
        },
        {
          name: "情報システム学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: "",
          other: ""
        },
        {
          name: "公務員学科",
          venue_name: "",
          paticipant_num: "",
          forth: "",
          third: "",
          second: "",
          first: "",
          other: ""
        }
      ]
    };
  }
};
</script>