<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <table class="table">
        <thead>
          <!-- Columnas tabla de historial de búsquedas  -->
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Type</th>
            <th scope="col">Search Day</th>
            <th scope="col">Star Date</th>
            <th scope="col">End Date</th>
            <th scope="col">Num Tweets</th>
            <th scope="col">Repeat Search</th>
          </tr>
        </thead>
        <tbody>
          <!-- Contenido tabla de historial de búsquedas -->
          <tr v-for="(search, index) in user.searchs" :key="search.id">
            <th scope="row">{{ index }}</th>
            <td>{{ search.title }}</td>
            <td>{{ search.type }}</td>
            <td>{{ search.created_at }}</td>
            <td>{{ search.start_date }}</td>
            <td>{{ search.end_date }}</td>
            <td>{{ search.num_tweets }}</td>
            <td><button type="button" class="btn btn-primary" @click="RepeatSearch(search)">Repeat Search</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'SearchHistory',
  created: function() {
    this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['createSearch']),
    async RepeatSearch(search) {
      // Creacion de busqueda de tweets
      if(search.type=="Tweet") {
          try {
              await this.createSearch(search);
              await this.$store.dispatch('viewTweetSearch');
              this.$router.push('/tweetanalysis');
          } catch (error) {
              throw 'Error in create search tweet. Please try again.';
          }
      }
      // Creacion de busqueda de usuarios
      else if(search.type=="User"){
          try {
              await this.createSearch(search);
              await this.$store.dispatch('viewUserSearch');
              await this.$store.dispatch('viewTweetSearch');
              this.$router.push('/useranalysis');
          } catch (error) {
              throw 'Error in create search user. Please try again.';
          }
      }
    }
  }
}
</script>

<style scoped>
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5ff;
    height: 100%;
}
</style>
