<template>
  <div id="MODAL">
    <div class="d-flex">
      <h3 class="h3">{{ this.$route.params.username }}님의 컬렉션</h3>
      <div class="more cusor-pointer" @click="openModal">더보기</div>
    </div>
    <div v-if="isModalViewed">
      <CollectionModal
        class="collection-modal"
        :collections="collection"
        :username="this.$route.params.username"
        @close-modal="closeModal"
      />
    </div>
    <div v-if="cuttedCollection?.length" class="row row-cols-1 row-cols-md-4 row-cols-xl-6 g-4">
      <MovieItem
        v-for="movie in cuttedCollection"
        :key="movie.id"
        :movie="movie"
      />
    </div>
    <div v-else>아직 담은 영화가 없습니다.</div>
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
      return this.collection?.slice(0, 5)
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
  .more {
    margin-left: 2rem;
    color: var(--primary-color);
  }


</style>