<template>
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
                      v-model="form.family_name"
                      ref="name"
                      :rules="[
              () => !!form.family_name || '※入力されていません',
              () => !!form.family_name && form.family_name.length <= 15 || '※15文字以内で入力してください',
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
                      v-model="form.first_name"
                      :rules="[
              () => !!form.first_name || '※入力されていません',
              () => !!form.first_name && form.first_name.length <= 15 || '※15文字以内で入力してください',
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
                      v-model="form.family_name_reading"
                      :rules="[
              () => !!form.family_name_reading || '※入力されていません',
              () => !!form.family_name_reading && form.family_name_reading.length <= 15 || '※15文字以内で入力してください',
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
                      v-model="form.first_name_reding"
                      :rules="[
              () => !!form.first_name_reding || '※入力されていません',
              () => !!form.first_name_reding && form.first_name_reding.length <= 15 || '※15文字以内で入力してください',
              ]"
                      :error-messages="errorMessages"
                      placeholder="メイ"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>

                <!-- 生年月日フォーム -->
                <v-row style="height: 0px;">
                  <p style="text-align: left;">生年月日</p>
                </v-row>

                <v-row style="height: 70px;">
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="form.birth_year"
                      :rules="[
              () => !!form.birth_year || '※入力されていません',
              () => 1900 <= form.birth_year && form.birth_year <= 2019 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="年"
                      required
                      height="15px"
                      width="100px"
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="form.birth_month"
                      :rules="[
              () => !!form.birth_year || '※入力されていません',
              () => 1 <= form.birth_month && form.birth_month <= 12 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="月"
                      height="15px"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col style="height: 70px;">
                    <v-text-field
                      ref="name"
                      v-model="form.birth_day"
                      :rules="[
              () => !!form.birth_day || '※入力されていません',
              () => 1 <= form.birth_day && form.birth_day <= 31 || '※入力が無効です',
              ]"
                      :error-messages="errorMessages"
                      placeholder="日"
                      required
                      height="15px"
                      width="100px"
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
                      v-model="form.postal_code"
                      :rules="[
              () => !!form.postal_code || '※入力されていません',
              () => form.postal_code.match(/^\d+$/) || '半角数字のみを入力してください',
              () => form.postal_code.length == 7 || '※7桁で入力してください',
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
                      v-model="form.street_address"
                      :rules="[
              () => !!form.street_address || '※入力されていません',
              () => !!form.street_address && form.street_address.length <= 32 || '※32文字以内で入力してください',
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
                      v-model="form.address"
                      :rules="[
              () => !!form.address || '※入力されていません',
              () => !!form.address && form.address.length <= 32 || '※32文字以内で入力してください',
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
                  <v-radio label="学生" value="yes1" @change="student_check = true, form.job=false"></v-radio>
                  <v-radio label="その他" value="no1" @change="student_check = false, form.job=true"></v-radio>
                </v-radio-group>

                <!-- 職業が学生なら表示 -->
                <div v-if="student_check">
                  <v-row style="height: 10px;">
                    <p style="text-align: left;">学校名</p>
                  </v-row>
                  <v-text-field
                    v-model="form.school_name"
                    :rules="[
              () => !!form.school_name || '※入力されていません',
              () => !!form.school_name && form.school_name.length <= 32 || '※32文字以内で入力してください',
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
                    :items="school_year_list"
                    v-model="form.school_year"
                    filled
                    label="選択してください"
                  ></v-select>
                  <v-row style="height: 25px;">
                    <p style="text-align: left;">卒業予定年</p>
                  </v-row>
                  <v-select :items="graduate_year_list" filled label="選択してください"></v-select>
                </div>

                <!-- 職業がその他なら表示 -->
                <div v-if="!student_check">
                  <v-row style="height: 2px;">
                    <p style="text-align: left;">高校卒業済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="yes2"></v-radio>
                    <v-radio label="いいえ" value="no2"></v-radio>
                  </v-radio-group>
                  <v-row style="height: 0px;">
                    <p style="text-align: left;">高等学校卒業程度認定試験取得済み</p>
                  </v-row>
                  <v-radio-group v-model="row" row>
                    <v-radio label="はい" value="radio-1"></v-radio>
                    <v-radio label="いいえ" value="radio-2"></v-radio>
                  </v-radio-group>
                </div>

                <!-- 参加希望学科フォーム -->
                <v-row style="height: 25px;">
                  <p style="text-align: left;">参加希望学科</p>
                </v-row>
                <v-select :items="subject_list" filled label="選択してください"></v-select>

                <!-- 登録ボタン -->
                <v-card-actions>
                  <v-col align="center" justify="start">
                    <v-btn
                      to="/Confirmation"
                      class="white--text"
                      x-large
                      color="light-blue lighten-3"
                      width="120px"
                      v-on:click="register"
                    >確認</v-btn>
                  </v-col>
                </v-card-actions>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      props: {
        form: Object
      },
      student_check: true,
      school_year_list: ["1学年", "2学年", "3学年", "4学年"],
      graduate_year_list: ["2020年", "2021年", "2022年", "2023年"],
      subject_list: []
    };
  },
  methods: {
    register: function() {
    }
  }
};
</script>

