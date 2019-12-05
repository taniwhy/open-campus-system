<template>
  <v-app>
    <v-container fluid>
      <v-row>
        <v-col>
          <v-row align="center" justify="end" style="width: 100%;">
            <v-btn flat to="/Branch" class="ma-2" outlined color="primary">戻る</v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-card ref="form">
          <v-card-text>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">参加表入力</v-list-item-title>
              <v-list-item-subtitle>※項目はすべて入力してください</v-list-item-subtitle>
            </v-list-item-content>
            <v-row>
              <v-col>
                お名前
                <v-text-field
                  ref="name"
                  v-model="name"
                  :rules="[() => !!name || 'This field is required']"
                  :error-messages="errorMessages"
                  placeholder="姓"
                  required
                  width="100px"
                ></v-text-field>
              </v-col>
              <v-col>
                <br />
                <v-text-field
                  ref="name"
                  v-model="name"
                  :rules="[() => !!name || 'This field is required']"
                  :error-messages="errorMessages"
                  placeholder="名"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                フリガナ
                <v-text-field
                  ref="name"
                  v-model="name"
                  :rules="[() => !!name || 'This field is required']"
                  :error-messages="errorMessages"
                  placeholder="セイ"
                  required
                ></v-text-field>
              </v-col>
              <v-col>
                <br />
                <v-text-field
                  ref="name"
                  v-model="name"
                  :rules="[() => !!name || 'This field is required']"
                  :error-messages="errorMessages"
                  placeholder="メイ"
                  required
                ></v-text-field>
              </v-col>
            </v-row>住所
            <v-text-field
              ref="address"
              v-model="address"
              :rules="[
              () => !!address || 'This field is required',
              () => !!address && address.length <= 25 || 'Address must be less than 25 characters',
              addressCheck
            ]"
              placeholder="入力してください"
              counter
              required
            ></v-text-field>番地/建物名
            <v-text-field
              :rules="[() => !!zip || 'This field is required']"
              required
              placeholder="入力してください"
            ></v-text-field>郵便番号
            <v-text-field
              ref="zip"
              v-model="zip"
              :rules="[() => !!zip || 'This field is required']"
              required
              placeholder="入力してください"
            ></v-text-field>職業
            <v-radio-group v-model="row" row>
              <v-radio label="学生" value="radio-1"></v-radio>
              <v-radio label="その他" value="radio-2"></v-radio>
            </v-radio-group>学年
            <v-select :items="gakunen_items" filled label="選択してください"></v-select>卒業予定年
            <v-select :items="yotei_items" filled label="選択してください"></v-select>参加希望学科
            <v-select :items="gakka_items" filled label="選択してください"></v-select>
            <v-card-actions>
              <v-btn x-large color="primary" width="120px">登録</v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
export default {
  name: "Register",
  data: () => ({
    gakunen_items: ["1学年", "2学年", "3学年", "4学年"],
    yotei_items: ["2020年", "2021年", "2022年", "2023年"],
    gakka_items: [
      "医療福祉事務学科",
      "診療情報管理士学科",
      "ホテルブライダル学科",
      "経営アシスト学科",
      "公務員・公務員速修学科",
      "保育学科",
      "情報スペシャリスト学科",
      "情報システム学科",
      "ゲームクリエイター・ゲームプログラマー学科",
      "データマーケター学科",
      "ネット動画クリエイター学科",
      "CGデザイン学科"
    ]
  })
};
</script>

