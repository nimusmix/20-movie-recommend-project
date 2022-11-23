import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingView from '@/views/LandingView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import UserEditView from '@/views/UserEditView'
import FeedView from '@/views/FeedView'
import NotFound404 from '@/views/NotFound404'

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
    component: LoginView
  },

  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/edit/:signUpFlag',
    name: 'UserEditView',
    component: UserEditView,
  },

  {
    path: '/feed',
    name: 'FeedView',
    component: FeedView
  },

  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: () => import('@/views/ProfileView')
  },

  {
    path: '/home',
    name: 'HomeView',
    component: () => import('@/views/HomeView')
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
    props: true
  },

  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },

  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router