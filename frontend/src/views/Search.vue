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
                Make sure that all fields are filled in, please.
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
            <div class="row">
                <div class="col">
                    <!-- Selector de fechas de inicio y fin de muestra de tweets -->
                    <label><strong>Select the start date and end date you want to display tweets on</strong></label>
                    <DatePicker v-model="time_range" value-type="format" range/>
                </div>
                <div class="col">
                    <!-- Selector de cantidad de tweets mostrados -->
                    <label><strong>Select the number of tweets you want to display</strong></label>
                    <NumberInputSpinner :min="10" :max="50" :integerOnly="true" v-model="search.num_tweets"/>
                </div>
                
            </div>
            <br/>
            <br/>
            <!-- Tabla ultimas 5 búsquedas -->
            <div v-if="user.searchs !== '[]'">
                <h5><strong>Last five searches</strong></h5>
                <table class="table">
                <thead>
                    <!-- Columnas tabla de últimas 5 búsquedas  -->
                    <tr>
                        <th scope="col">Title</th>
                        <th scope="col">Type</th>
                        <th scope="col">Search Day</th>
                        <th scope="col">Start Date</th>
                        <th scope="col">End Date</th>
                        <th scope="col">Num Tweets</th>
                        <th scope="col">Repeat Search</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Contenido tabla de últimas 5 búsquedas -->
                    <tr v-for="search in user.searchs.slice(-5)" :key="search.id">
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
            <br/>
            <br/>
            <!-- Tabla de ultimos 5 tweets guardados -->
            <div class="table-responsive">
                <h5><strong>Last five tweet saved</strong></h5>
                <table class="table">
                    <thead>
                    <!-- Columnas tabla de últimos 5 tweets guardados -->
                    <tr>
                        <th scope="col">Author</th>
                        <th scope="col">Text</th>
                        <th scope="col">Replys</th>
                        <th scope="col">Retweets</th>
                        <th scope="col">Likes</th>
                        <th scope="col">Created at</th>
                    </tr>
                    </thead>
                    <tbody>
                    <!-- Contenido tabla de últimos 5 tweets guardados -->
                    <tr v-for="tweet in user.tweetsaved.slice(-5)" id='tweetssaved'>
                        <td>{{ tweet.author }}</td>
                        <td>{{ tweet.text }}</td>
                        <td>{{ tweet.reply_count }}</td>
                        <td>{{ tweet.retweet_count }}</td>
                        <td>{{ tweet.like_count }}</td>
                        <td>{{ tweet.created_at.slice(0,-6) }}</td>
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
components: { DatePicker, NumberInputSpinner},
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
methods: {
    ...mapActions(['createSearch']),
    // Metodo de creacion de una busqueda
    async SaveSearch() {
        var today = new Date(),
        month = '' + (today.getMonth() + 1),
        day = '' + today.getDate(),
        year = today.getFullYear();

        if (month.length < 2)   month = '0' + month;
        if (day.length < 2) day = '0' + day;

        var date = [year, month, day].join('-');
        // Comprobacion de campos rellenados
        if (this.time_range == null || this.search.type == '' || this.search.title == '')
            $('#modalHome').modal()
        else if(date < this.time_range[1] || date < this.time_range[0]) {
            $("#modalHome .modal-body").text('Make sure that the start date and end date are before the current day, please');
            $('#modalHome').modal()
        }
        else {
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
            }
        }
    },
    // Metodo para la repeticion de una de las 5 últimas búsquedas
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
    height: 100%;
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
