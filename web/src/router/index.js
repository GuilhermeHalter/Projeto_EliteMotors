import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OfertasView from '../views/OfertasView.vue'
import InfoView from '../views/InfoView.vue'
import CarrosView from '../views/CarrosView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/ofertas',
      name: 'ofertas',
      component: OfertasView
    },
    {
      path: '/infos',
      name: 'infos',
      component: InfoView
    },
    {
      path: '/lojas',
      name: 'lojas',
      component: CarrosView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
  ]
})

export default router