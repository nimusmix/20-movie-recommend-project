import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: sessionStorage,
    })
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
    loginUser: null,
    similarUsers: [],
    API_URL:'http://127.0.0.1:8000',
    width: 0,
    height: 0,
    selectedOtts: [],
    selectedGenres: [],
    // recommend
    recommendSimilar: [],
    recommendLatent: [],
    recommendPreference: {},
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    recent2Reviews(state) {
      return state.reviews.slice(0, 2)
    }
  },
  mutations: {
    GET_GENRES(state, genres) {
      state.genres = genres
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    GET_LOGIN_USER(state, user) {
      state.loginUser = user
    },
    GET_SIMILAR(state, similarUsers) {
      state.similarUsers = similarUsers
    },
    // 회원가입 && 로그인
    SAVE_USER(state, user) {
      state.username = user.username
      state.token = user.token
    },
    LOGOUT(state) {
      state.username = null
      state.token = null
      router.push({ name: 'LandingView' })
    },
    GET_WINDOWS(state){
      state.width = window.innerWidth;
      state.height = window.innerHeight;
    },
    GET_RECOMMEND(state, data) {
      if (data.name === 'similar') {
        state.recommendSimilar = data.data
      } else if (data.name === 'latent') {
        state.recommendLatent = data.data
      } else {
        state.recommendPreference[data.name] = data.data
      }
    },
    SET_RECOMMEND_PREFERENCE(state) {
      state.recommendPreference = {}
    },
    SAVE_CATEGORY(state, data){
      state.selectedOtts = data.selectedOtts
      state.selectedGenres = data.selectedGenres
    }
  },
  actions: {
    getGenres(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v1/genres/`,
      })
        .then((res) => {
          console.log('1 actions의 getGenres 성공!')
          context.commit('GET_GENRES', res.data)
        })
        .catch(() => {
          console.log('actions의 getGenres 실패!')
        })
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          console.log('2 actions의 getMovies 성공!')
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
      })
        .then((res) => {
          console.log('3 actions의 getReviews 성공!')
          context.commit('GET_REVIEWS', res.data)
        })
        .catch(() => {
          console.log('actions의 getReviews 실패!')
        })
    },
    getLoginUser(context) {
      const username = context.state.username
      if (username) {
        axios({
          method: 'get',
          url: `${context.state.API_URL}/api/v3/accounts/${username}/`,
        })
          .then((res) => {
            context.commit('GET_LOGIN_USER', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    getSimilar(context) {
      axios({
          method: 'get',
          url: `${context.state.API_URL}/api/v2/get-similar`,
          headers: {
              Authorization: `Token ${context.state.token}`
          },
      })
        .then((res) => {
          const similarUsers = res.data.map((user) => {
            return user.id
          })
          context.commit('GET_SIMILAR', similarUsers)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    putPreference(context, genre) {
      axios({
        method: 'put',
        url: `${context.state.API_URL}/api/v3/accounts/edit-perferences-score/${genre}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then(() => {
          console.log('actions의 putPreference 성공!')
          // context.dispatch('getRecommend')
        })
        .catch(() => {
          console.log('actions의 putPreference 실패!')
        })
    },
    getRecommend(context, recommendObject) {
      context.commit('SET_RECOMMEND_PREFERENCE')
      const {name, url} = recommendObject

      axios({
        method: 'get',
        url: `${context.state.API_URL}/${url}/`,
        headers: {
            Authorization: `Token ${context.state.token}`
        },
      })
        .then((res) => {
          if (name === 'preference') {
            for (const data of res.data) {
              const temp = {
                name: data.label,
                data: data.movies
              }
              context.commit('GET_RECOMMEND', temp)
            }
          } else {
            const temp = {
              name: name,
              data: res.data
            }
            context.commit('GET_RECOMMEND', temp)
          }
        })
        .catch((err) => {
          console.log(`getRecommend ${name} 실패!`)
          console.log(err)
        })
    },
    // 윈도우 크기 설정
    getWindowSize(context){
      context.commit('GET_WINDOWS')
    },
  },
})
