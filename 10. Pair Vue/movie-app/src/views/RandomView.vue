<template>
  <div class="container">
    <h1>Random</h1>
    <button @click="getRandomMovie">Pick</button>
    <div class="card mb-3">
      <img class="card-img-top" :src="imgSrc" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title">{{ selectMovie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'RandomView',
  data: function() {
    return {
      
    }
  },
  computed: {
    ...mapState(['selectMovie']),
    imgSrc: function(){
      return 'http://image.tmdb.org/t/p/w200/' + this.selectMovie.poster_path
    } 
  },
  methods: {
    ...mapActions(['getRandomMovie']),
  }  
}
</script>

<style>
</style>