<template>
  <div>
    <div style="border:1px solid black">
      <!-- {{ review }} -->
      <!-- <div>{{ review.movie }}</div> -->
      <div>{{ review.movie_title }}</div>
      <!-- <div>{{ review.user }}</div> -->
      <div>{{ review.username }}</div>
      <div>{{ review.content }}</div>
      <div>{{ review.score }}</div>
      <div>{{ review.created_at }}</div>
      <div>{{ review.is_spoiler }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  props:{
    review: Object,
  },
  computed:{
    
  }
}
</script>

<style>

</style>