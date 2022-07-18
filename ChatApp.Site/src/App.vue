<script setup>
import Message from './components/Message.vue';
import { useCookies } from "vue3-cookies";

window.cookies = useCookies().cookies;
</script>

<script>
export default {
  created() {
    // fetch csrf token and set csrftoken cookie
    this.updateCsrfToken();

    // fetch messages
    this.updateMessages();

    setInterval(this.updateMessages, 500);
  },
  data() {
    return {
      messages: [],
      messageBox: "",
      userName: window.cookies.get("userName"),
    }
  },
  methods: {
    updateCsrfToken: function() {
      fetch(`${import.meta.env.VITE_BASE_URL}/chat/csrf-token`)
      .then(res => {
        res.json()
        .then(data => {
          window.cookies.set("csrftoken", data.token);
        })
        .catch(e => console.error(e));
      })
      .catch(e => console.error(e));
    },
    getCsrfToken: function() {
      return window.cookies.get("csrftoken");
    },
    updateMessages: function() {
      fetch(`${import.meta.env.VITE_BASE_URL}/chat/messages`)
      .then(res => {
        res.json()
        .then(data => {
          this.messages = data;
        })
        .catch(e => console.error(e));
      })
      .catch(e => console.error(e));
    },
    sendMessage: function() {
      const content = this.messageBox;
      this.messageBox = "";

      if (!this.userName) return;

      window.cookies.set("userName", this.userName);

      if (!content) return;

      fetch(`${import.meta.env.VITE_BASE_URL}/chat/new-message`, {method: "POST", headers: {'X-CSRFToken': this.getCsrfToken(), "content-type": "application/json"}, body: JSON.stringify({msg_user_name: this.userName, msg_content: content})})
      .catch(e => console.error(e));
    }
  }
};
</script>

<template>
  <main class="w-full h-full fixed overflow-y-auto">
    <div class="flex flex-col w-full h-full px-36 py-8 justify-center space-y-2">
      <div class="flex flex-col w-full h-full space-y-3 overflow-y-scroll" ref="messages">
        <Message v-for="message in messages" :key="message.id" :user_name="message.user_name" :content="message.content" />
      </div>
      <div class="flex flex-row w-full mt-auto pb-5 h-16 border-2 px-2 pt-5 space-x-2 rounded">
        <input class="w-full px-3 -my-1 w-1/6" v-model="userName" placeholder="Type your name!" />
        <input class="w-full px-3 -my-1" v-model="messageBox" v-on:keyup.enter="sendMessage" placeholder="Type in here! Press enter to send messages!" />
      </div>
    </div>
  </main>
</template>

<style>
  
</style>
