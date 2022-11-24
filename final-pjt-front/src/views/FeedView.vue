<template>
  <div class="router-view-padding">
    <h1 class="h1">피드</h1>
    <div class="d-flex">
      <div :class="['feed-menu', {'select-feed':selectFeed==='all'}]" @click="filtering('all')">모두</div>
      <div :class="['feed-menu', {'select-feed':selectFeed==='follow'}]" @click="filtering('follow')">팔로잉</div>
      <div :class="['feed-menu', {'select-feed':selectFeed==='similar'}]" @click="filtering('similar')">나와 비슷한 사람</div>
    </div>
    <article v-for="review in filteredReviews" :key="review.id">
      <FeedItem :review="review"/>
    </article>
  </div>
</template>

<script>
// import axios from 'axios'
import FeedItem from '@/components/FeedItem'

export default {
  name: 'FeedView',
  components: {
    FeedItem,
  },
  data() {
    return {
      filteredReviews: [],
      selectFeed:3,
    }
  },
  methods: {
    allFilter(review) {
      if (this.followings.includes(review.user) || this.similarUsers.includes(review.user) || review.user === this.loginUser.id) {
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
      this.selectFeed = name
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
    similarUsers() {
      return this.$store.state.similarUsers.filter((user) => {
        if (!this.followings.includes(user)) {
          return true
        }
      })
    },
    reviews() {
      return this.$store.state.reviews
    }
  },
  watch: {
    '$route' (to, from) {
      if (to !== from) {
        this.filtering('all')
      }
    }
  },
  created() {
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
  .select-feed{
    font-weight: 700;
    text-decoration: underline;
  }
</style>