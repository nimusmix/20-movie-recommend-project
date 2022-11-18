<template>
  <div>
    <h1 class="h1">@{{ user.username }}</h1>
    <CollectionList/>
    <collection-modal/>
    <ReviewList/>
  </div>
</template>

<script>
import axios from 'axios'

import CollectionList from '@/components/CollectionList'
import CollectionModal from '@/components/CollectionModal'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'ProfileView',
  components: {
    CollectionList,
    CollectionModal,
    ReviewList,
  },
  data() {
    return {
      user: null,
    }
  },
  computed: {
  },
  created() {
    axios({
      method: 'get',
      url: `${this.$store.state.API_URL}/api/v3/accounts/${this.$route.params.username}/`,
    })
      .then((res) => {
        this.user = res.data
      })
      .catch((err) => {
        console.loh(err)
      })
  }
}
</script>

<style>

</style>