<template>
  <div class="router-view-padding">
    <h1 class="h1">피드</h1>
    <div class="d-flex">
      <div class="feed-menu" @click="filtering('all')">모두</div>
      <div class="feed-menu" @click="filtering('follow')">팔로잉</div>
      <div class="feed-menu" @click="filtering('similar')">나와 비슷한 사람</div>
    </div>
    <article v-for="review in filteredReviews" :key="review.id">
      <FeedItem :review="review"/>
    </article>
  </div>
</template>

<script>
import axios from 'axios'
import FeedItem from '@/components/FeedItem'

export default {
  name: 'FeedView',
  components: {
    FeedItem,
  },
  data() {
    return {
      filteredReviews: [],
      similarUsers: [],
    }
  },
  methods: {
    allFilter(review) {
      if (this.followings.includes(review.user) || this.similarUsers.includes(review.user)) {
        return true
      }
    },
    followFilter(review) {
      if (this.followings.includes(review.user)) {
        return true
      }
    },
    similarFilter(review) {
      if (this.similarUsers.includes(review.user)) {
        return true
      }
    },
    filtering(name) {
      switch(name) {
        case 'all': {
          this.filteredReviews = this.reviews.filter(this.allFilter)
          break
        }
        case 'follow': {
          this.filteredReviews = this.reviews.filter(this.followFilter)
          break
        }
        case 'similar': {
          this.filteredReviews = this.reviews.filter(this.similarFilter)
          break
        }
      }
    },
    getSimilar() {
      axios({
          method: 'get',
          url: `${this.$store.state.API_URL}/api/v2/get-similar`,
          headers: {
              Authorization: `Token ${this.$store.state.token}`
          },
      })
        .then((res) => {
          let tmpSimilarUsers = []
          for (const user of res.data) {
            tmpSimilarUsers.push(user.id)
          }
          this.similarUsers = tmpSimilarUsers
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  computed: {
    loginUser() {
      return this.$store.state.loginUser
    },
    followings() {
      let tmp_followings = []
      for (const following of this.loginUser?.followings) {
        tmp_followings.push(following.id)
      }
      return tmp_followings
    },
    reviews() {
      return this.$store.state.reviews
    }
  },
  created() {
    this.getSimilar()
    this.filtering('all')
  },
}
</script>

<style>
  .feed-menu {
    margin-right: 2.8rem;
    margin-bottom: 1.6rem;
    font-size: 1.2rem;
    font-weight: 400;
    cursor: pointer;
  }
</style>