 <!--
 参加者一覧表示用コンポーネント

 Adminページで確認できる

 親ページ: Admin
 兄弟ページ:
  -->
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
                :items-per-page="20"
                hide-default-footer
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

export default {
  data() {
    return {
      /**
       * 参加者履歴テーブルから本日の参加者を
       * 持ってくるためのキー
       * @type {string}
       */
      today: moment().format("l"),
      /**
       * 本日の参加者数表示用
       * @type {number}
       */
      total_people: 0,
      /**
       * 学科一覧リスト
       * @type {String}
       */
      subjectList: [],
      /**
       * 参加者一覧テーブルのヘッダ
       * @type {Object}
       */
      headers: [
        {
          text: "学科名",
          align: "left",
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
      /**
       * 参加者一覧テーブルのバリュー
       * @type {Object}
       */
      values: []
    };
  },
  methods: {
    /**
     * 学科一覧リストに格納処理
     */
    subject_push(response) {
      for (var key in response) {
        this.subjectList.push(response[key].subject_name);
      }
      this.loadList();
    },
    /**
     * GETで学科一覧を持ってくる
     */
    makeSubjectList() {
      this.loading = true;
      try {
        axios
          .get("http://127.0.0.1:8000/api/subject/")
          .then(response => this.subject_push(response.data));
      } catch (error) {
        alert("情報を取得できませんでした。時間をおいてやり直してください。");
      }
    },
    /**
     * 参加者一覧テーブルの作成処理
     */
    async loadList() {
      const token = this.$store.getters.idToken;
      console.log(this.today);
      try {
        //参加者履歴テーブルから本日の参加者を持ってくる;
        const res = await axios.get(
          "http://127.0.0.1:8000/api/participant_history/",
          {
            headers: {
              Authorization: "JWT " + token.token
            },
            params: {
              join_day: this.today
            }
          },
        );
        //本日の参加者数に代入
        this.total_people = res.data.length;
        if (this.total_people == 0) {
          this.loading = false;
        } else {
          //学科一覧から一つずつ取り出す
          for (var subjectKey in this.subjectList) {
            //学科一覧テーブルのバリューに挿入用オブジェクト宣言
            var valueBuf = {
              name: null,
              venue_name: "未定",
              participant_num: 0,
              first: 0,
              second: 0,
              third: 0,
              forth: 0,
              other: 0
            };
            //順番に学科名を収納
            var key = this.subjectList[subjectKey];
            valueBuf.name = key;
            //順番に参加者履歴から取り出し
            for (var resKey in res.data) {
              //もし学科名と参加学科が一致したら
              if (res.data[resKey].join_subject == key) {
                valueBuf.participant_num += 1;
                if (res.data[resKey].school_year == "1学年") {
                  valueBuf.first += 1;
                } else if (res.data[resKey].school_year == "2学年") {
                  valueBuf.second += 1;
                } else if (res.data[resKey].school_year == "3学年") {
                  valueBuf.third += 1;
                } else if (res.data[resKey].school_year == "4学年") {
                  valueBuf.forth += 1;
                } else {
                  valueBuf.other += 1;
                }
              }
            }
            //参加者数が1以上のみ表示させる
            if (valueBuf.participant_num != 0) {
              this.values.push(valueBuf);
            }
          }
        }
      } catch (error) {
        alert("情報を取得できませんでした。時間をおいてやり直してください。");
      }
      this.loading = false;
    }
  },
  created: function() {
    this.makeSubjectList();
  }
};
</script>