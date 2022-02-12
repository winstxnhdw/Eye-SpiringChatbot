<template>
  <div id="app">
    <ChatBox />
  </div>
</template>

<script lang="ts">
import ChatBox from './components/ChatBox.vue'

export default {
  name: 'App',
  components: {
    ChatBox
  }
}
</script>

<style>
@import './assets/base.css';
</style>
