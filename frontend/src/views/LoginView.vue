<script setup>
import { ref } from 'vue';

const email = ref('');
const password = ref('');
const errorMessage = ref('');

async function handleLogin() {
  errorMessage.value = '';
  console.log('🔄 Iniciando login...');
  
  if (!email.value || !password.value) {
    errorMessage.value = 'Por favor, preencha todos os campos.';
    return;
  }

  const formData = new FormData();
  formData.append('username', email.value);
  formData.append('password', password.value);

  console.log('📤 Enviando dados para:', 'http://127.0.0.1:8000/token');
  console.log('📧 Email:', email.value);

  try {
    const response = await fetch('http://127.0.0.1:8000/token', {
      method: 'POST',
      body: formData
    });
    
    console.log('📥 Resposta recebida:', response.status);
    
    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('user_token', data.access_token);
      console.log('✅ Login bem-sucedido!');
      alert('Login realizado com sucesso! Token salvo.');
    } else {
      const errorText = await response.text();
      console.error('❌ Erro na resposta:', response.status, errorText);
      errorMessage.value = 'E-mail ou senha incorretos.';
    }
  } catch (error) {
    console.error('❌ Erro de conexão:', error);
    errorMessage.value = 'Erro de conexão com o servidor.';
  }
}
</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h1>Chat Empresarial</h1>
      <p>Faça login para continuar</p>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="email">E-mail</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="input-group">
          <label for="password">Senha</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Entrar</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-container { display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; }
.login-box { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); width: 100%; max-width: 400px; text-align: center; }
h1 { margin-bottom: 24px; color: #333; }
.input-group { margin-bottom: 16px; text-align: left; }
label { display: block; margin-bottom: 8px; font-weight: bold; color: #555; }
input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
button { width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; margin-top: 8px; }
button:hover { background-color: #0056b3; }
.error-message { margin-top: 16px; color: red; font-weight: bold; }
</style>