import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    reviews: [],
    genres: [],
    otts: [
      {
        id: 97,
        name: 'watcha',
      },
      {
        id: 356,
        name: 'waave',
      },
      {
        id: 337,
        name: 'disney',
      },
      {
        id: 8,
        name: 'netflix',
      },    
    ],
    username: null,
    token: null,
    API_URL:'http://127.0.0.1:8000'
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_GENRES(state, genres) {
      state.genres = genres
    },
    // 회원가입 && 로그인
    SAVE_USER(state, user) {
      state.username = user.username
      state.token = user.token
      router.push({ name: 'HomeView' })
    },
    LOGOUT(state) {
      state.username = null
      state.token = null
      router.push({ name: 'LandingView' })
    },
    GET_REVIEWS(state, reivews) {
      state.reviews = reivews
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v1/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch(() => {
          console.log('actions의 getMovies 실패!')
        })
    },
    getReviews(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v2/reviews/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
          context.commit('GET_REVIEWS', res.data)
        })
        .catch(() => {
          console.log('actions의 getReviews 실패!')
        })
    },
    getGenres(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v1/genres/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_GENRES', res.data)
        })
        .catch(() => {
          console.log('actions의 getGenres 실패!')
        })
    },
  },
  modules: {
  }
})
