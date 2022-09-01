<template>
    <section class="section about-section gray-bg">
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
        <div class="container">
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
            <DatePicker v-model="time_range" value-type="format" range/>
            <NumberInputSpinner :min="10" :max="50" :integerOnly="true" v-model="search.num_tweets"/>
            <br/>
            <br/>
            <div v-if="user.searchs !== '[]'">
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
    </section>
</template>
  
  
<script>
import { mapActions, mapGetters } from 'vuex';
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import NumberInputSpinner from 'vue-number-input-spinner';

export default {
name: 'Home',
components: { DatePicker, NumberInputSpinner, },
data(){
    return {
        search: {
            title: '',
            type: '',
            start_date: '',
            end_date: '',
            num_tweets: 10,
        },
        time_range: null,
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
        this.search.start_date = this.time_range[0]
        this.search.end_date = this.time_range[1]
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
    },
},
}
</script>

<style scoped>
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5ff;
    height: 100vh;
}
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
</style>
