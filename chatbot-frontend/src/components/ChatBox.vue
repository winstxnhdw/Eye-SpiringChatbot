<template>
  <section class="chat-box">
    <div class="chat-box-list-container" ref="chatbox">
      <ul class="chat-box-list">
        <div :class="message.author" v-for="(message, index) in messages" :key="index">
          <div class="message-inner" :class="message.author">
            <div class="username">{{ message.author == 'client' ? this.client_name : this.server_name }}</div>
            <div class="content">{{ message.text }}</div>
          </div>
        </div>
      </ul>
    </div>
    <div class="chat-input">
      <input type="text" placeholder="Enter your message" v-model="message" @keyup.enter="send_message" />
    </div>
  </section>
</template>

<script lang="ts">
import get_chatbot_response from '@/axios'
import { onMounted } from 'vue'

export default {
  name: 'ChatBox',
  data: () => ({
    message: '',
    messages: [],

    client_name: 'You',
    server_name: 'Rosie'
  }),

  setup() {
    onMounted(() => {
      console.log('Starting')
    })
  },

  methods: {
    async send_message() {
      this.messages.push({
        text: `${this.message}`,
        author: 'client'
      })

      const chatbot_reply = await get_chatbot_response({
        text: this.message
      })

      if (chatbot_reply !== '') {
        this.messages.push({
          text: `${chatbot_reply}`,
          author: 'server'
        })
      }

      this.message = ''
      this.$nextTick(() => {
        this.$refs.chatbox.scrollTop = this.$refs.chatbox.scrollHeight
      })
    }
  }
}
</script>

<style scoped lang="scss">
.chat-box,
.chat-box-list {
  display: flex;
  flex-direction: column;
  list-style-type: none;
}

.chat-box-list-container {
  height: 100%;
  margin-bottom: 1px;
  overflow-x: hidden;
  overflow-y: scroll;
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-scrollbar {
    display: none;
  }
}

.chat-box-list {
  padding-left: 10px;
  padding-right: 10px;
  display: flex;
  padding: 20px;

  .client {
    padding: 10px;

    .message-inner {
      .username {
        color: #000;
        font-size: 12px;
        margin-bottom: 5px;
        padding-left: 15px;
        padding-right: 10px;
      }

      .content {
        display: inline-block;
        padding: 10px 20px;
        box-shadow: inset 0 0 0 500px rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        font-size: 14px;
        line-height: 1.2em;
        text-align: left;
        max-width: 70%;
        word-wrap: break-word;
      }
    }
  }

  .server {
    padding: 10px;
    float: right;

    .message-inner {
      max-width: 70%;

      .username {
        text-align: right;
        color: #000;
        font-size: 12px;
        margin-bottom: 5px;
        padding-right: 25px;
      }
      .content {
        display: inline-block;
        padding: 10px 20px;
        box-shadow: inset 0 0 0 500px rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        font-size: 14px;
        line-height: 1.2em;
        text-align: left;
      }
    }
  }
}

.chat-box {
  width: 45vw;
  height: 60vh;
  box-shadow: inset 0 0 0 500px rgba(255, 255, 255, 0.6);
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.chat-input {
  display: flex;

  input {
    line-height: 4;
    width: 100%;
    border: none;
    border-left: none;
    border-bottom: none;
    border-right: none;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    padding-left: 15px;
    outline: none;
    background: rgba(255, 255, 255, 0.3);
  }
}
</style>
