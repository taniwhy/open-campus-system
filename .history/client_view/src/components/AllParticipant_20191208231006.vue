<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-col>
        <v-row align="center" justify="center">
          <v-col align="center" justify="center">全体の参加状況{{total_people}}人</v-col>
        </v-row>
        <v-row>
          <v-row align="center" justify="center">
            <v-col align="center" justify="center">
              <v-data-table
                style="max-width: 800px;"
                :headers="headers"
                :items="values"
                :loading="loading"
                multi-sort
                locale="ja-jp"
                loading-text="読込中"
                no-data-text="データがありません。"
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
import moment from "moment";
import axios from "axios";
import settings from "..//local_settings.json";

export default {
  data() {
    return {
      today: moment().format("l"),
      total_people: 0,
      subjectList: [],
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
      value: [{}]
    };
  },
  methods: {
    subject_push: function(response) {
      for (var key in response) {
        this.subjectList.push(response[key].subject_name);
      }
      console.log(this.subjectList)
    },
    makeSubjectList() {
      try {
        axios
          .get("http://127.0.0.1:8000/api/subject/")
          .then(response => this.subject_push(response.data));
      } catch (error) {
        alert("情報を取得できませんでした。時間をおいてやり直してください。");
      }
    },
    async loadList() {
      this.loading = true;
      try {
        const res = await axios.get(
          "http://127.0.0.1:8000/api/participant_history/",
          {
            params: { join_day: this.today }
          },
          {
            auth: { username: settings["name"], password: settings["pass"] }
          }
        );
        console.log(res.data);
        console.log(this.subjectList);
        this.total_people = res.data.length;
      } catch (error) {
        alert("情報を取得できませんでした。時間をおいてやり直してください。");
      }
      this.loading = false;
    }
  },
  created: function() {
    this.makeSubjectList();
    this.loadList();
  }
};
</script>