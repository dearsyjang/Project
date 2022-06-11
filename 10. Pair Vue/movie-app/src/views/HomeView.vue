<template>
  <div class="HomeView">
    <div class="grid-container">
    <movie-card v-for="movie in movieList" :key="movie.id" :movie="movie">
    </movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '../components/MovieCard.vue'
import {mapState, mapActions} from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MovieCard
  },
  computed: {
    ...mapState(['movieList']),
    ...mapActions(['getMovieList'])
  },
  created() {
    this.getMovieList
  }
}
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  justify-content: space-between;
  
}
</style>
