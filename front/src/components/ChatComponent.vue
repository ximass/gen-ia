<template>
  <div class="chat-container">
    <h2>Chat</h2>
    <div class="messages">
      <div v-for="message in messages" :key="message.id" class="message">
        {{ message.text }}
      </div>
    </div>
    <input v-model="inputMessage" @keyup.enter="sendMessage" placeholder="Digite algo..." />
  </div>
</template>

<script>
window.Pusher = require('pusher-js');

import Pusher from 'pusher-js';

export default {
  data() {
    return {
      inputMessage: '',
      messages: [],
    };
  },
  created() {
    var pusher = new Pusher('fed30f50518acf03eb5a', {
      cluster: 'sa1'
    });

    var channel = pusher.subscribe('chat');
    
    channel.bind('MessageSent', (data) => {
      console.log('Mensagem recebida', data);

      this.messages.push({
        text: data.message
      });
    });
  },
  methods: {
    sendMessage() {
      fetch('http://127.0.0.1:8000/api/send-message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: this.inputMessage }),
      }).then(() => {
        console.log('Mensagem enviada');
      });

      this.inputMessage = '';
    },
  },
};
</script>

<style scoped>
.chat-container {
  max-width: 600px;
  margin: auto;
  border: 1px solid #ddd;
  padding: 20px;
}
.messages {
  height: 300px;
  overflow-y: scroll;
  border-bottom: 1px solid #ddd;
  margin-bottom: 10px;
}
.message {
  padding: 5px;
  border-bottom: 1px solid #f0f0f0;
}
</style>
