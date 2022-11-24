import Vue from 'vue'
import VueRouter from 'vue-router'

import store from '@/store/index.js'
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
  scrollBehavior(to, from, savedPosition) { 
    // 디테일뷰에서 카테고리로 이동
    if(from.name === 'DetailView'){
      if(to.name === 'CategoryView'){
        return { x: 0, y: savedPosition.y } 
      }
    }
    // 카테고리에서 디테일로 이동
    if (from.name === 'CategoryView'){
      if(to.name != 'DetailView'){
        const data = {
          selectedOtts:[],
          selectedGenres:[],
        }
        store.commit('SAVE_CATEGORY', data)
      }
    }

    return { x: 0, y: 0 } 
  },
  routes
})

router.beforeEach((to, from, next) => {
  const isLogin = store.getters.isLogin
  const allowAllPages = ['LandingView', 'LoginView', 'SignupView']
  const isAuthRequired = !allowAllPages.includes(to.name)

  if (!isLogin && isAuthRequired) {
    next({ name: 'LoginView' })
  } else {
    next()
  }
})

export default router