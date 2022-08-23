<template>
  <section>
    <div class="container">
      <table class="table">
        <thead>
          <!-- Columnas tabla de historial de búsquedas  -->
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Type</th>
          </tr>
        </thead>
        <tbody>
          <!-- Contenido tabla de historial de búsquedas -->
          <tr v-for="(search, index) in user.searchs" :key="search.id">
            <th scope="row">{{ index }}</th>
            <td>{{ search.title }}</td>
            <td>{{ search.type }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'SearchHistory',
  created: function() {
    this.$store.dispatch('viewMe');
    this.$store.dispatch('viewTweetSearch');

  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
  },
}
</script>

<style>
.container{
    margin-top: 3%;
    padding: 5em;
    background-color: aliceblue;
}
</style>
