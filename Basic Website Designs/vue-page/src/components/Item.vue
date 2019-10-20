<template>
  <div class="db ma2 w-30 bg-light-green br2 grow-hover">
    <h3>{{ index }}. {{ item }}</h3>
  </div>
</template>

<script>
export default {
  name: "Item",
  props: {
    index: Number,
    item: String
  }
};
</script>

<style>
</style>