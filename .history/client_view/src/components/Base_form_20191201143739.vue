<template>
  <div>
    <div>
      入力
      <span v-if="$route.meta.isConfirm">> 確認</span>
    </div>
    <router-view></router-view>
  </div>
</template>