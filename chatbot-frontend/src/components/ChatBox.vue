<template>
  <section class="chat-box">
    <div class="chat-box-list-container" ref="chatbox">
      <ul class="chat-box-list">
        <li class="message" :class="message.author" v-for="(message, index) in messages" :key="index">
          <p>
            <span>{{ message.text }}</span>
          </p>
        </li>
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

      this.messages.push({
        text: `${chatbot_reply}`,
        author: 'server'
      })

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
  overflow-x: hidden;
  overflow-y: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
  margin-bottom: 1px;

  -webkit-scrollbar {
    display: none;
  }
}

.chat-box-list {
  padding-left: 10px;
  padding-right: 10px;

  span {
    padding: 8px;
    padding-left: 10px;
    color: white;
    border-radius: 4px;
  }
  .server {
    span {
      background: #99cc00;
    }

    p {
      float: right;
      text-align: left;
      max-width: 45%;
    }
  }

  .client {
    span {
      background: #0070c8;
    }

    p {
      float: left;
      text-align: left;
    }
  }
}

.chat-box {
  margin: 10px;
  border: 1px solid #fff;
  width: 35vw;
  height: 50vh;
  border-radius: 4px;
  margin-left: auto;
  margin-right: auto;
  align-items: space-between;
  justify-content: space-between;
  background-color: #fff;
}

.chat-input {
  display: flex;

  input {
    line-height: 3;
    width: 100%;
    border: 1px solid #fff;
    border-left: none;
    border-bottom: none;
    border-right: none;
    border-bottom-left-radius: 4px;
    padding-left: 15px;
    outline: none;
  }
}
</style>
