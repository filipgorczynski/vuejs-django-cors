<template>
  <div id="app">
    <h1>IMDb Top Rated Movies</h1>
    <ul>
      <li v-for="movie in movies">
        {{ movie.title }} <em>{{ movie.year }}</em>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data: function() {
    return {
      movies: []
    };
  },
  created() {
    axios
      .get(process.env.API_URL)
      .then(results => {
        this.movies = results.data;
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
