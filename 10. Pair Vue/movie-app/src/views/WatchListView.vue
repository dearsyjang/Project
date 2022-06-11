<template>
  <div class="WatchListView">
    <h1>My Movie List</h1>
    <watch-list-form></watch-list-form>
    <br>
    <br>
    <watch-list-item v-for="movie in watchList" :key="movie.date" :movie="movie"></watch-list-item>
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'
import WatchListForm from '@/components/WatchListForm.vue'
import { mapState } from 'vuex'


export default {
  name: 'WatchListView',
  components: {
    WatchListItem,
    WatchListForm,
  },
  computed:{
    ...mapState(['watchList'])
  }
}
</script>

<style>

</style>