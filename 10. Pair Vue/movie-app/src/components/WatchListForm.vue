<template>
  <div class="WatchListForm">
    <input type="text" v-model.trim="movieTitle" @keyup.enter="createMovie">
    <button @click="createMovie">ADD</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return { 
      movieTitle : '',
      date: new Date().getTime(),
    }
  },
  methods: {
    createMovie() {
      const newMovie = {
        title: this.movieTitle
      }
      if (newMovie.title) {
        this.$store.dispatch('createWatchMovie', newMovie)
      }
      this.movieTitle = ''
    }
  }  
}
</script>

<style>

</style>