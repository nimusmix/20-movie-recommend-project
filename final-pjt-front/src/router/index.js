import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingView from '@/views/LandingView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingView',
    component: LandingView
  },

  {
    path: '/login',
    name: 'LoginView',
    component: () => import('@/views/LoginView')
  },

  {
    path: '/signup',
    name: 'SignupView',
    component: () => import('@/views/SignupView')
  },

  {
    path: '/accounts/:username',
    name: 'ProfileView',
    component: () => import('@/views/ProfileView')
  },

  {
    path: '/home',
    name: 'HomeView',
    component: () => import('@/views/HomeView')
  },

  {
    path: '/feed',
    name: 'FeedView',
    component: () => import('@/views/FeedView')
  },

  {
    path: '/recommend',
    name: 'RecommendView',
    component: () => import('@/views/RecommendView')
  },

  {
    path: '/category',
    name: 'CategoryView',
    component: () => import('@/views/CategoryView')
  },

  {
    path: '/movies/:pk',
    name: 'DetailView',
    component: () => import('@/views/DetailView'),
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router