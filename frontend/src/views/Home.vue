<template>
  <section>
    <!-- Modal para muestra de errores en la validacion  -->
    <div class="modal fade" id="modalHome" tabindex="-1" role="dialog" aria-labelledby="modalHome" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Error</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Select filter by Tweet or User first, please.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
    </div>
    <div v-if="isLoggedIn" id="logout">
      <div id="search-container" class="container">
        <h2>Datter, the analysis of Twitter in your hand</h2>
        <h5>Perform a search to get started</h5>
        <br/>
        <!-- Barra de busqueda de la pagina -->
        <div id="search-bar" class="input-group mb-3">
          <!-- Filtros de busqueda -->
          <select id="search-filter" v-model="search.type" class="select">
            <option selected>Tweet</option>
            <option>User</option>
          </select>
          <input id="search-input" type="text" v-model="search.title" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="basic-addon1" v-on:keyup.enter="SaveSearch()">
          <button id="search-button" type="button" class="btn btn-primary" @click="SaveSearch()">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
              <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
          </button>
        </div> 
        <br/>
        <br/>
        <h5><strong>Last five searches</strong></h5>
        <table class="table">
          <thead>
            <!-- Columnas tabla de últimas 5 búsquedas  -->
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Type</th>
            </tr>
          </thead>
          <tbody>
            <!-- Contenido tabla de últimas 5 búsquedas -->
            <tr v-for="search in user.searchs.slice(-5)" :key="search.id">
              <td>{{ search.title }}</td>
              <td>{{ search.type }}</td>
            </tr>
          </tbody>
        </table>
      </div> 
    </div>
    <div v-else>
      <section class="home_banner_area">
        <div class="banner_inner">
          <div class="container">
            <div class="row">
              <div class="col-lg-7">
                <div class="banner_content">
                  <img class="" src="../assets/logoWhite.png" alt="">
                  <h4 class="text">Tool For Twitter Data Analysis</h4>
                  <div class="d-flex align-items-center">
                    <button id="login-button" type="button" class="btn btn-secondary btn-lg btn-block" @click="$router.push('/login')">Log In</button>
                    <button id="signup-button" type="button" class="btn btn-lg btn-dark btn-block" @click="$router.push('/signup')">Sign Up</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-5">
                <div class="home_right_img">
                  <img id="image-home" class="" src="../assets/home-image.png" alt="">
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </section>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'Home',
  data(){
    return {
      search: {
        title: '',
        type: '',
      }
    };
  },
  created: function() {
    this.$store.dispatch('viewMe');
  },
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    ...mapGetters({user: 'stateUser' }),
  },
  // Metodo de creacion de una busqueda
  methods: {
    ...mapActions(['createSearch']),
    async SaveSearch() {
      // Creacion de busqueda de tweets
      if(this.search.type=="Tweet") {
        try {
          await this.createSearch(this.search);
          await this.$store.dispatch('viewTweetSearch');
          this.$router.push('/tweetanalysis');
        } catch (error) {
          throw 'Error in create search tweet. Please try again.';
        }
      }
      // Creacion de busqueda de usuarios
      else if(this.search.type=="User"){
        try {
          await this.createSearch(this.search);
          await this.$store.dispatch('viewUserSearch');
          await this.$store.dispatch('viewTweetSearch');
          this.$router.push('/useranalysis');
        } catch (error) {
          throw 'Error in create search user. Please try again.';
        }
      } else {
        $('#modalHome').modal()
      }
    }
  }
}
</script>

<style scoped>
#search-container {
  background-color: aliceblue;
  margin-top: 7%;
  padding: 5em;
}
#search-bar {
  font-family: Arial, Helvetica, sans-serif;
}
#search-button {
  font-size: large;
}
#search-filter {
  background: lavender;
}
#login-button {
  margin-top: 20px; 
  margin-right: 20px;
  color: #fff;
  background-color: #343a40;
  border-color: #343a40;
}
#signup-button {
  margin-top: 20px; 
  color: #fff;
  background-color: gray;
  border-color: gray;
}
#image-home {
  display: block;
  max-width: 100%;
  height: auto;
  margin-left: 20px;
} 
.home_banner_area {
    z-index: 1;
    background: url(../assets/home-banner.png) no-repeat top center;
    background-position: center;
    background-size: cover; }
    .home_banner_area .banner_inner {
      width: 100%; }
      .home_banner_area .banner_inner .home_right_img {
        padding-top: 197px; }
        @media (max-width: 1480px) {
          .home_banner_area .banner_inner .home_right_img img {
            max-width: 100%;
            height: auto; } }
        @media (max-width: 991px) {
          .home_banner_area .banner_inner .home_right_img {
            display: none; } }
      .home_banner_area .banner_inner .col-lg-7 {
        vertical-align: middle;
        align-self: center; }
      .home_banner_area .banner_inner .banner_content {
        text-align: left; }
        @media (max-width: 991px) {
          .home_banner_area .banner_inner .banner_content {
            margin-top: 150px; } }
        .home_banner_area .banner_inner .banner_content h3 {
          font-size: 40px;
          margin-bottom: 20px;
          position: relative; }
          .home_banner_area .banner_inner .banner_content h3:after {
            content: '';
            width: 410px;
            height: 2px;
            position: absolute;
            top: 50%;
            left: 23%;
            background: #000000; }
            @media (max-width: 575px) {
              .home_banner_area .banner_inner .banner_content h3:after {
                display: none; } }
        .home_banner_area .banner_inner .banner_content h1 {
          margin-top: 20px;
          font-size: 70px;
          line-height: 60px;
          margin-bottom: 25px; }
          @media (max-width: 1024px) {
            .home_banner_area .banner_inner .banner_content h1 {
              font-size: 60px; } }
          @media (max-width: 767px) {
            .home_banner_area .banner_inner .banner_content h1 {
              font-size: 50px; } }
        .home_banner_area .banner_inner .banner_content h5 {
          font-size: 24px;
          margin-bottom: 35px; }
        .home_banner_area .banner_inner .banner_content .primary_btn {
          margin-right: 20px; }
</style>
