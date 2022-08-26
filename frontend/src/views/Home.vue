<template>
  <section>
    <div class="container">
      <div v-if="isLoggedIn" id="logout">
        <p id="title">Proyecto de TFG de Sergio Martín Hernández</p>
        <!-- Barra de busqueda de la pagina -->
        <div id="search-bar" class="input-group mb-3">
          <!-- Filtros de busqueda -->
          <select id="search-filter" v-model="search.type" class="select">
            <option selected>Tweet</option>
            <option>User</option>
          </select>
          <input id="search-input" type="text" v-model="search.title" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="basic-addon1">
          <button id="search-button" type="button" class="btn btn-primary" @click="SaveSearch()">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
              <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
          </button>
        </div> 
      </div> 
      <div v-else>
        <div class="row align-items-center">
          <div class="col-6">
            <img id="image-home" src="../assets/home.png" class="img-fluid">
          </div>
          <div class="col">
            <div class="row">
              <!-- Boton de inicio de sesion -->
              <button id="login-button" type="button" class="btn btn-outline-primary btn-lg btn-block" @click="$router.push('/login')">Log in</button>
            </div>
            <div class="row">
              <!-- Boton de registro de usuario -->
              <button id="signup-button" type="button" class="btn btn-lg btn-dark btn-block" @click="$router.push('/signup')">Sign up</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
import { mapActions } from 'vuex';
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
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  // Metodo de creacion de una busqueda
  methods: {
    ...mapActions(['createSearch']),
    async SaveSearch() {
      // Creacion de busqueda de tweets
      if(this.search.type=="Tweet") {
        try {
          await this.createSearch(this.search);
          this.$router.push('/tweetanalysis');
        } catch (error) {
          throw 'Error in create search tweet. Please try again.';
        }
      }
      // Creacion de busqueda de usuarios
      else if(this.search.type=="User"){
        try {
          await this.createSearch(this.search);
          this.$router.push('/useranalysis');
        } catch (error) {
          throw 'Error in create search user. Please try again.';
        }
      } else {
        window.alert("Select filter by Tweet or User first, please");
      }
    }
  }
}
</script>

<style scoped>
.container {
  background-color: aliceblue;
  margin-top: 7%;
  padding: 5em;
}
#title {
  text-align: center;
  font-size: x-large;
  font-family: revert;
  font-weight: bold;
  padding-bottom: 20px;
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
  margin: 20px;
}
#signup-button {
  margin: 20px;
}
#image-home {
  display: block;
  max-width: 100%;
  height: auto;
}
</style>
