<template>
  <div>
    <h1>ProfileView</h1>
    <CollectionList/>
    <collection-modal/>
    <ReviewList/>
  </div>
</template>

<script>
import CollectionList from '@/components/CollectionList'
import CollectionModal from '@/components/CollectionModal'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'ProfileView',
  components: {
    CollectionList,
    CollectionModal,
    ReviewList,
  }
}
</script>

<style>

</style>