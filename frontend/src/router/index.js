import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

console.log('Criando router...')

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    }
  ]
})

console.log('Router criado!')

export default router