<template>
  <div class="WatchListItem">
    <span>{{ movie.title }}</span>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    movie: Object,
  },
}
</script>

<style>
</style>