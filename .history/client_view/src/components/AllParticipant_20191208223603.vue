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
  methods: {
    async loadList() {
      this.loading = true;
      try {
        let sorts = [];
        if (this.options.sortBy !== null) {
          this.options.sortBy.forEach((value, index) => {
            sorts.push((this.options.sortDesc[index] ? "-" : "+") + value);
          });
        }
        const res = await Axios.post(
          "/api/list",
          Object.assign(this.model, {
            offset: (this.options.page - 1) * this.options.itemsPerPage,
            limit: this.options.itemsPerPage,
            sort: sorts.join(" ")
          })
        );
        if (res.data) {
          this.items = res.data.items;
          this.total = res.data.total;
        }
      } catch (error) {
        alert("情報を取得できませんでした。時間をおいてやり直してください。");
      }
      this.loading = false;
    }
  },
  created: function() {
    this.loadList();
  }
};
</script>