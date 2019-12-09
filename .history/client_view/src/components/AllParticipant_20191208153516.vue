<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <v-col align="center" justify="center">全体の参加状況{{entry_number_of_people}}人</v-col>
        </v-row>
        <v-row>
          <v-row align="center" justify="center">
            <v-col align="center" justify="center">
              <v-data-table style="max-width: 800px;" :headers="headers" :items="values"></v-data-table>
            </v-col>
          </v-row>
        </v-row>
      </v-col>
    </v-container>
  </v-content>
</template>


<script>
import moment from "moment";
import axios from "axios";
import settings from "..//local_settings.json";

export default {
  data() {
    return {
      today: moment().format("l"),
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
        { text: "既卒", value: "other" }
      ],
      value: []
    };
  },
  created() {
    axios
      .get(
        "http://127.0.0.1:8000/api/participant_history/",
        {
          params: {"join_day": this.today}
        },
        {
          auth: { username: settings["name"], password: settings["pass"] }
        }
      )
      .then(response => this.get_data(response))
      .catch(error => this.failed_registered(error));
  }
};
</script>