import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingView from '@/views/LandingView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import ProfileView from '@/views/ProfileView'
import HomeView from '@/views/HomeView'
import FeedView from '@/views/FeedView'
import RecommendView from '@/views/RecommendView'
import CategoryView from '@/views/CategoryView'
import DetailView from '@/views/DetailView'

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
    component: LoginView,
  },

  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView,
  },

  {
    path: '/accounts/:username',
    name: 'ProfileView',
    component: ProfileView
  },

  {
    path: '/home',
    name: 'HomeView',
    component: HomeView
  },

  {
    path: '/feed',
    name: 'FeedView',
    component: FeedView
  },

  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },

  {
    path: '/category',
    name: 'CategoryView',
    component: CategoryView
  },

  {
    path: '/movies/:pk',
    name: 'DetailView',
    component: DetailView,
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router