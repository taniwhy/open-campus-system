<template>
  <v-app>
    <header id="header">
    <h1>This is the header.</h1>
    <nav id="header-nav">
      <ul>
        <router-link tag="li" id="home-nav" to="/" exact><a>ホーム</a></router-link>
        <router-link tag="li" id="game-nav" to="/game"><a>ゲーム</a></router-link>
        <router-link tag="li" id="info-nav" to="/info"><a>情報</a></router-link>
        <router-link tag="li" id="gift-nav" to="/gift"><a>お土産</a></router-link>
      </ul>
    </nav>
  </header>
    <v-content>
      <Home/>
    </v-content>
  </v-app>
</template>

<script>
import Home from './components/Home';

export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>
