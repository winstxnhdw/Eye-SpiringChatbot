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
      if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
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
    margin: 0;
  }
}
</style>
