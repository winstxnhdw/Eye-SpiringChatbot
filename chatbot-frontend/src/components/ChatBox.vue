<template>
  <div class="chat-box">
    <div class="chat-box-list-container">
      <ul class="chat-box-list">
        <li class="message" v-for="(message, index) in messages" :key="index">
          <p>
            <span>{{ message.text }}</span>
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
import { get_chatbot_response } from '@/axios'

export default {
  name: 'ChatBox',
  data: () => ({
    message: '',
    messages: [],

    client_name: 'You',
    server_name: 'Rosie'
  }),

  methods: {
    async send_message() {
      this.messages.push({
        text: `${this.client_name}: ${this.message}`,
        author: 'client'
      })

      const chatbot_reply = await get_chatbot_response({
        text: this.message
      })

      this.messages.push({
        text: `${this.server_name}: ${chatbot_reply}`,
        author: 'server'
      })

      this.message = ''
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
  border: 1px solid #fff;
  width: 50vw;
  height: 50vh;
  box-shadow: 0 0 1rem 0 rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  margin-left: auto;
  margin-right: auto;
  align-items: space-between;
  justify-content: space-between;
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
.chat-box-list {
  padding-left: 10px;
  padding-right: 10px;

  span {
    padding: 8px;
    color: white;
    border-radius: 4px;
  }
}

.chat-box-list-container {
  overflow: scroll;
}
</style>
