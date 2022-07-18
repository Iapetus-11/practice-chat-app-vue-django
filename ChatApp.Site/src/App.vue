<script setup>
import Message from './components/Message.vue';
import { useCookies } from "vue3-cookies";

window.cookies = useCookies().cookies;
</script>

<script>
export default {
  created() {
    // fetch messages
    this.updateMessages();

    setInterval(this.updateMessages, 750);
  },
  data() {
    return {
      messages: [],
      messageBox: "",
      userName: this.getUserName(),
    }
  },
  methods: {
    updateMessages: function() {
      fetch(`${import.meta.env.VITE_BASE_URL}/chat/messages`)
      .then(res => {
        res.json()
        .then(data => {
          this.messages = data.reverse();
        })
        .catch(e => console.error(e));
      })
      .catch(e => console.error(e));
    },
    sendMessage: function() {
      const content = this.messageBox;
      this.messageBox = "";

      if (!this.userName) return;
      if (!content) return;

      fetch(`${import.meta.env.VITE_BASE_URL}/chat/new-message`, {method: "POST", headers: {"content-type": "application/json"}, body: JSON.stringify({msg_user_name: this.userName, msg_content: content})})
      .catch(e => console.error(e));
    },
    setUserName: function(userName) {
      window.cookies.set("userName", userName);
      this.userName = userName;
    },
    getUserName: function() {
      return window.cookies.get("userName") || "anon";
    },
    saveUserName: function() {
      this.setUserName(this.userName.slice(0, 20));
    }
  }
};
</script>

<template>
  <main class="w-full h-full fixed overflow-y-auto">
    <div class="flex flex-col w-full h-full px-36 py-8 justify-center space-y-2">
      <header class="flex flex-row pb-5 justify-between">
        <div class="flex flex-grow flex-shrink w-1">
          <input class="px-3 -my-1 py-2 border-2 rounded" v-model="userName" v-on:keyup.enter="saveUserName" v-on:focusout="saveUserName" placeholder="Change Username" />
        </div>
      </header>

      <!-- messages container -->
      <div class="flex flex-col-reverse w-full h-full overflow-y-scroll" ref="messages">
        <Message v-for="message in messages" :key="message.id" :user_name="message.user_name" :content="message.content" />
      </div>

      <!-- message box / bar thingy at the bottom -->
      <div class="flex flex-row w-full mt-auto pb-5 h-16 px-2 pt-5 space-x-2">
        <input class="w-full px-3 -my-1 py-5 border-2 rounded" v-model="messageBox" v-on:keyup.enter="sendMessage" placeholder="Type in here! Press enter to send messages!" />
      </div>
    </div>
  </main>
</template>
