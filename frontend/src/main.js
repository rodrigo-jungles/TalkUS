import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

console.log('Iniciando aplicação Vue com router...')

try {
  const app = createApp(App)
  app.use(router)
  app.mount('#app')
  console.log('✅ Aplicação Vue montada com sucesso!')
} catch (error) {
  console.error('❌ Erro ao montar aplicação:', error)
  // Fallback simples em caso de erro
  document.getElementById('app').innerHTML = `
    <div style="padding: 50px; text-align: center;">
      <h1 style="color: red;">Erro no Frontend</h1>
      <p>Erro: ${error.message}</p>
    </div>
  `
}
