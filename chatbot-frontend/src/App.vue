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
      if (window.matchMedia('only screen and (max-width: 760px)').matches) {
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
    margin-top: 30px;
  }
}
</style>
