<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <h1>TalkUS - Teste</h1>
    <p>Se você está vendo isso, o Vue está funcionando!</p>
    <RouterView />
  </div>
</template>

<style>
/* Reset básico */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #f0f2f5;
}

#app {
  min-height: 100vh;
  padding: 20px;
}

h1 {
  color: #333;
  margin-bottom: 10px;
}

p {
  color: #666;
  margin-bottom: 20px;
}
</style>
