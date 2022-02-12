<template>
  <div id="app">
    <ChatBox />
  </div>
</template>

<script lang="ts">
import ChatBox from '@/components/ChatBox.vue'

export default {
  name: 'App',
  components: {
    ChatBox
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
