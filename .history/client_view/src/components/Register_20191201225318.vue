<template>
  <v-app>
    <!-- 戻るボタン配置用コンテナ -->
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn
              x-large
              flat
              to="/Branch"
              class="ma-2"
              outlined
              color="light-blue lighten-3"
              width="120px"
            >戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <!-- カード配置用コンテナ -->
    <v-container align="center" justify="center" style="width: 100%;">
      <v-row align="center" justify="center" style="width: 100%;">
        <v-col align="center" justify="center" style="width: 100%;">
          <!-- フォーム用カード -->
          <v-card ref="form" width="520px">
            <v-card-text>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
                <v-list-item-subtitle>※項目はすべて入力してください</v-list-item-subtitle>
              </v-list-item-content>

              <!-- カード配置用コンテナ -->
              <v-container style="width: 90%;" fluid>
                <!-- 名前用コンテナ -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">お名前</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="data.form.family_name"
                      ref="name"
                      :rules="[
              () => !!data.form.family_name || '※入力されていません',
              () => !!data.form.family_name && data.form.family_name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="姓"
                      required
                      width="100px"
                      height="15px"
                      style="vertical-align: top;"
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="data.form.first_name"
                      :rules="[
              () => !!data.form.first_name || '※入力されていません',
              () => !!data.form.first_name && data.form.first_name.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="名"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- フリガナフォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">フリガナ</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="data.form.family_name_reading"
                      :rules="[
              () => !!data.form.family_name_reading || '※入力されていません',
              () => !!data.form.family_name_reading && data.form.family_name_reading.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="セイ"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="data.form.first_name_reading"
                      :rules="[
              () => !!data.form.first_name_reading || '※入力されていません',
              () => !!data.form.first_name_reading && data.form.first_name_reading.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="メイ"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 生年月日フォーム -->
                <v-row style="height: 15px;">
                  <p style="text-align: left;">生年月日</p>
                </v-row>

                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-select v-model="data.form.birh_year" :items="data.years_list" label="年" dense solo></v-select>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-select v-model="data.form.birh_month" :items="data.months_list" label="月" dense solo></v-select>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-select v-model="data.form.birh_day" :items="data.days_list" label="日" dense solo></v-select>
                  </v-col>
                </v-row>

                <!-- 性別フォーム -->
                <v-row style="height: 10px;">
                  <p style="text-align: left;">性別</p>
                </v-row>
                <v-radio-group row>
                  <v-radio label="男" @change="dataform.gender=false"></v-radio>
                  <v-radio label="女" @change="data.form.gender=true"></v-radio>
                </v-radio-group>

                <!-- 電話番号フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">電話番号</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="data.form.phone_number"
                      :rules="[
              () => !!data.form.phone_number || '※入力されていません',
              () => data.form.phone_number.match(/^\d+$/) || '半角数字のみを入力してください',
              () => data.form.phone_number.length == 11 || '※11桁で入力してください',
              ]"
                      required
                      height="15px"
                      placeholder="入力してください"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <!-- 郵便番号フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">郵便番号</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="data.form.postal_code"
                      :rules="[
              () => !!data.form.postal_code || '※入力されていません',
              () => data.form.postal_code.match(/^\d+$/) || '半角数字のみを入力してください',
              () => data.form.postal_code.length == 7 || '※7桁で入力してください',
              ]"
                      required
                      height="15px"
                      placeholder="入力してください"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 住所フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">住所</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      v-model="data.form.street_address"
                      :rules="[
              () => !!data.form.street_address || '※入力されていません',
              () => !!data.form.street_address && data.form.street_address.length <= 32 || '※32文字以内で入力してください',
            ]"
                      placeholder="入力してください"
                      counter
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 番地/建物名フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">番地/建物名</p>
                </v-row>
                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="zip"
                      v-model="data.form.address"
                      :rules="[
              () => !!data.form.address || '※入力されていません',
              () => !!data.form.address && data.form.address.length <= 32 || '※32文字以内で入力してください',
            ]"
                      required
                      height="15px"
                      placeholder="入力してください"
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 職業フォーム -->
                <v-row style="height: 10px;">
                  <p style="text-align: left;">職業</p>
                </v-row>
                <v-radio-group row>
                  <v-radio
                    label="学生"
                    value="yes1"
                    @change="data.student_check = true, form.job=false"
                  ></v-radio>
                  <v-radio
                    label="その他"
                    value="no1"
                    @change="data.student_check = false, form.job=true"
                  ></v-radio>
                </v-radio-group>

                <!-- 職業が学生なら表示 -->
                <div v-if="data.student_check">
                  <v-row style="height: 10px;">
                    <p style="text-align: left;">学校名</p>
                  </v-row>
                  <v-text-field
                    v-model="data.form.school_name"
                    :rules="[
              () => !!data.form.school_name || '※入力されていません',
              () => !!data.form.school_name && data.form.school_name.length <= 32 || '※32文字以内で入力してください',
            ]"
                    placeholder="入力してください"
                    counter
                    height="15px"
                    required
                  ></v-text-field>
                  <v-row style="height: 25px;">
                    <p style="text-align: left;">学年</p>
                  </v-row>
                  <v-select
                    :items="data.school_year_list"
                    v-model="data.form.school_year"
                    filled
                    label="選択してください"
                  ></v-select>
                  <v-row style="height: 25px;">
                    <p style="text-align: left;">卒業予定年</p>
                  </v-row>
                  <v-select
                    :items="data.graduate_year_list"
                    v-model="data.form.school_graduate_year"
                    filled
                    label="選択してください"
                  ></v-select>
                </div>

                <!-- 職業がその他なら表示 -->
                <div v-if="!data.student_check">
                  <v-row style="height: 2px;">
                    <p style="text-align: left;">高校卒業済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" @change="data.form.graduate_check=true"></v-radio>
                    <v-radio label="いいえ" @change="data.form.graduate_check=false"></v-radio>
                  </v-radio-group>
                  <v-row style="height: 0px;">
                    <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" @change="data.form.graduate_qualification=true"></v-radio>
                    <v-radio label="いいえ" @change="data.form.graduate_qualification=false"></v-radio>
                  </v-radio-group>
                </div>

                <!-- 参加希望学科フォーム -->
                <v-row style="height: 25px;">
                  <p style="text-align: left;">参加希望学科</p>
                </v-row>
                <v-select :items="data.subject_list" v-model="data.join_subject" label="選択してください"></v-select>

                <!-- 登録ボタン -->
                <v-card-actions>
                  <v-col align="center" justify="start">
                    <v-btn
                      class="white--text"
                      x-large
                      color="light-blue lighten-3"
                      width="120px"
                      v-on:click="$router.push('/confirmation')"
                    >確認</v-btn>
                  </v-col>
                </v-card-actions>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    {{data}}
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  props: {
    data: Object
  },
  mounted: function() {
    this.create_birth()
    axios
      .get("http://127.0.0.1:8000/api/subject/")
      .then(response => this.subject_push(response.data));
  },
  methods: {
    create_birth: function() {
      for (var y = 2019; y > 1900; y--) {
        this.data.years_list.push(y);
      }
      for (var m = 1; m < 13; m++) {
        this.data.months_list.push(m);
      }
      for (var d = 1; d < 32; d++) {
        this.data.days_list.push(d);
      }
    },
    subject_push: function(response) {
      for (var key in response) {
        this.data.subject_list.push(response[key].subject_name);
      }
    }
  }
};
</script>

