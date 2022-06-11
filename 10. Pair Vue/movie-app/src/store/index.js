import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

//homeview 
//영화 목록 Ajax 활용해서 불러오기
//movie/top_rated response
//poster_path, title, overview


//randomview
//맨 처음에는 pick 버튼만 보이게
//pick 버튼 클릭시 랜덤으로 영화 보여주기


//watchlistview
//watchlistform으로 보고 싶은 영화 제목 입력하면
//하단에 목록으로 저장됨
//README에는 명시되지 않았지만, watchlistitem을 v-for로 담기 위한 watchlist.vue가 추가적으로 필요할 듯?

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],

  state: {
    movieList: [],
    watchList: [],
    selectMovie: {},
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIST(state){
      const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      const API_KEY = '85b03cb96344fddee47b329076ffa046'
      const params = {
        api_key: API_KEY,
        language: 'ko-KR',
        page: 1
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(response => {
        // response로 오브젝트 받아오고, 그 안에 result 값이 원하는 영화들의 정보를 담고 있음
        state.movieList = response.data.results
      })
      .catch(function(error){
        console.log(error)
      })

    },
    GET_RANDOM_MOVIE(state){
      // movieList는 GET_MOVIE_LIST를 통해 받아온 영화들이 담긴 array -> 여기서 하나의 영화 오브젝트를 랜덤하게 받아오기
      const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      const API_KEY = '85b03cb96344fddee47b329076ffa046'
      const params = {
        api_key: API_KEY,
        language: 'ko-KR',
        page: 1
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(response => {
        // response로 오브젝트 받아오고, 그 안에 result 값이 원하는 영화들의 정보를 담고 있음
        state.selectMovie = _.sample(response.data.results)
        console.log(state.selectMovie)
      })
      .catch(function(error){
        console.log(error)
      })

    },
    CREATE_WATCH_MOVIE(state, newMovie){
      state.watchList.push(newMovie)
    },
  },
  actions: {
    getMovieList(context){
      context.commit('GET_MOVIE_LIST')
    },
    getRandomMovie(context){
      context.commit('GET_RANDOM_MOVIE')
    },
    createWatchMovie(context, newMovie){
      context.commit('CREATE_WATCH_MOVIE', newMovie)
    },
  },

})
