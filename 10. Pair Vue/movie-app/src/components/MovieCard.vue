<template>
  <div class="MovieCard">
    <div class="card" style="width: 18rem;">
      <img class="card-img-top" :src="imgSrc" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title"> {{movie.title}} </h5>
        <p class="card-text"> {{movie.overview}} </p>
      </div>
    </div>
  </div>
</template>



<script>
// movie/top_rated response
// poster_path, title, overview

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  }, 
  data(){
    return{
      imgSrc: 'http://image.tmdb.org/t/p/w200/' + this.movie.poster_path
    }
  }
}
</script>

<style>
.MovieCard div img{
  width: 100%;
}
</style>