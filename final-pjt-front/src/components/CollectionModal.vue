<template>
  <div>
    <div class="overlay" @click="closeModal"></div>
    <div class="modal-card">
      <CollectionModalItem/>
    </div>
  </div>
</template>

<script>
import CollectionModalItem from '@/components/CollectionModalIttem'

export default {
  name: 'CollectionModal',
  components: {
    CollectionModalItem
  },
  props: {
    collection: Array,
  },
  methods: {
    closeModal() {
      this.$emit('close-modal')
    }
  }
}
</script>

<style>
  .overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    background-color: black;
  }

  .modal-card {
    position: relative;
    z-index: 1;
    min-width: 100%;
    min-height: 500px;
    margin: auto;
    padding: 20px;
    opacity: 1;
    background-color: white;
    border: 1px red solid;
  }
</style>