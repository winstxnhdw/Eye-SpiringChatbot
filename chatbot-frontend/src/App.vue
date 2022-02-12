<template>
  <div id="app">
    <MobileView v-if="!is_mobile" />
    <ChatBox />
  </div>
</template>

<script lang="ts">
import ChatBox from '@/components/ChatBox.vue'
import MobileView from '@/views/Mobile.vue'

export default {
  name: 'App',
  components: {
    ChatBox,
    MobileView
  },

  methods: {
    is_mobile() {
      if (
        navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i)
      ) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style>
@import './assets/base.css';

#app {
  margin-top: 150px;
}

@media (max-width: 1000px) {
  #app {
    margin: 30px;
  }
}
</style>
