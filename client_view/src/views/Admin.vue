 <!--
 Adminのベース

 ログイン完了した管理者は自動的にここに遷移される

 遷移元: Home
 遷移先:
  -->
<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-account-badge-horizontal-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>全体参加状況</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>交通費支給確認</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-account-edit</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>アンケート管理</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-printer</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>データ出力</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click.stop="dialog = true">
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>ログアウト</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Open campus system Admin</v-toolbar-title>
    </v-app-bar>

    <router-view></router-view>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
    <v-col>
      <v-row align="center" justify="center">
        <v-dialog v-model="dialog" max-width="290">
          <v-card>
            <v-col>
              <v-row align="center" justify="center">
                <v-card-title class="headline">ログアウトしますか？</v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    class="white--text"
                    style="font-weight: 700;"
                    large
                    color="cyan"
                    width="120px"
                    @click="logout"
                  >ログアウト</v-btn>
                  <v-btn
                    text
                    class="white--text"
                    style="font-weight: 700;"
                    large
                    color="cyan"
                    width="120px"
                    @click="dialog = false"
                  >キャンセル</v-btn>
                </v-card-actions>
              </v-row>
            </v-col>
          </v-card>
        </v-dialog>
      </v-row>
    </v-col>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    /**
     * ドロワーの表示判定
     * @type {boolean}
     */
    drawer: null,
    /**
     * ダイアログの表示判定
     * @type {boolean}
     */
    dialog: false
  }),
  /**
   * 遷移時にログイン状態をチェックし
   * 未ログインであればログイン画面にリダイレクトする
   */
  mounted() {
    if (this.$store.getters.loggedIn == false) {
      this.$router.push({ path: "login" });
    }
  },
  //ログアウト処理
  methods: {
    logout() {
      this.$store.dispatch("logout");
    }
  }
};
</script>