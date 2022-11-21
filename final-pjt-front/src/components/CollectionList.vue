<template>
  <div>
    <div class="d-flex">
      <h3 class="h3">내 컬렉션</h3>
      <div @click="openModal">더보기</div>
    </div>
    <div v-if="isModalViewed">
      <CollectionModal
        class="collection-modal"
        :collection="collection"
        @close-modal="closeModal"
      />
    </div>
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <MovieItem
        v-for="movie in cuttedCollection"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'
import CollectionModal from '@/components/CollectionModal'

export default {
  name: 'CollectionList',
  components: {
    MovieItem,
    CollectionModal,
  },
  props: {
    collection: Array,
  },
  data() {
    return {
      isModalViewed: false,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    cuttedCollection() {
      return this.collection?.slice(0, 4)
    }
  },
  methods: {
    openModal() {
      this.isModalViewed = true
    },
    closeModal() {
      this.isModalViewed = false
    }
  }
}
</script>

<style>
  .collection-modal {
    position: absolute;
  }
</style>