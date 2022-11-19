<template>
  <div>
    <div class="d-flex">
    <h1>CollectionList</h1>
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
      <CollectionListItem
        v-for="movie in cuttedCollection"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import CollectionListItem from '@/components/CollectionListItem'
import CollectionModal from '@/components/CollectionModal'

export default {
  name: 'CollectionList',
  components: {
    CollectionListItem,
    CollectionModal,
  },
  props: {
    collectionId: Array,
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
    collection() {
      const myCollection = this.movies.filter((movie) => {
        if (this.collectionId?.includes(movie.id)) {
          return true
        }
      })
      return myCollection
    },
    cuttedCollection() {
      return this.collection.slice(0, 4)
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