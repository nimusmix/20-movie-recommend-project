<template>
  <div>
    <h1 class="h1">프로필</h1>
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