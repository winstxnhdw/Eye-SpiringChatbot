<template>
  <div class="chat-box">
    <div class="chat-box-list-container">
      <ul class="chat-box-list">
        <li class="message" v-for="(message, index) in messages" :key="index">
          <p>
            <span> {{ message.text }}</span>
          </p>
        </li>
      </ul>
    </div>
    <div class="chat-input">
      <input type="text" v-model="message" @keyup.enter="send_message" />
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'ChatBox',
  data: () => ({
    message: '',
    messages: []
  }),

  methods: {
    send_message() {
      this.messages.push({
        text: this.message,
        author: 'You'
      })
    }
  }
}
</script>

<style scoped lang="scss">
.chatbox,
.chat-box-list {
  display: flex;
  flex-direction: column;
  list-style-type: none;
}

.chat-box {
  top: 10%;
  width: 50vw;
  box-shadow: 0 0 1rem 0 rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  margin-left: auto;
  margin-right: auto;
}

.chat-input {
  display: flex;

  input {
    line-height: 2;
    width: 100%;
    border-left: none;
    border-bottom: none;
    border-right: none;
    border-bottom-left-radius: 4px;
    padding-left: 15px;
  }
}
</style>
