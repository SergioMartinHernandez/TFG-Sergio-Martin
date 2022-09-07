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
                <input id="search-input" type="text" v-model="search.title" class="form-control" placeholder="Search" aria-label="Search" v-on:keyup.enter="CreateSearch()">
                <button id="search-button" type="button" class="btn btn-primary" @click="CreateSearch()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                    </svg>
                </button>
            </div>
            <div class="row">
                <div class="col">
                    <!-- Selector de fechas de inicio y fin de muestra de tweets -->
                    <label><strong>Select the start date and end date you want to display tweets on</strong></label>
                    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8">
                        <div class="mb-4">
                        <v-date-picker v-model="range" mode="Date" :masks="masks" :min-date="min_date" :max-date="max_date" is-range>
                            <template v-slot="{ inputValue, inputEvents, isDragging }">
                            <div id="date-picker" class="flex flex-col sm:flex-row justify-start items-center">
                                <input id="container-date1"
                                    class="flex-grow pl-8 pr-2 py-1 bg-gray-100 border rounded w-full"
                                    :class="isDragging ? 'text-gray-600' : 'text-gray-900'"
                                    :value="inputValue.start"
                                    v-on="inputEvents.start"
                                />
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                    <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                                </svg>
                                
                                <input id="container-date2"
                                    class="flex-grow pl-8 pr-2 py-1 bg-gray-100 border rounded w-full"
                                    :class="isDragging ? 'text-gray-600' : 'text-gray-900'"
                                    :value="inputValue.end"
                                    v-on="inputEvents.end"
                                />
                            </div>
                            </template>
                        </v-date-picker>
                        </div>
                    </form>
                </div>
                <div class="col">
                    <!-- Selector de cantidad de tweets mostrados -->
                    <label><strong>Select the number of tweets you want to display</strong></label>
                    <vue-slider id="slider" ref="slider" :min="min_value" :max="max_value" :height="height" v-model="search.num_tweets"></vue-slider>
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
                        <td>{{ search.start_date.slice(0, -14) }}</td>
                        <td>{{ search.end_date.slice(0, -14) }}</td>
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
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import VCalendar from "v-calendar";
/**
 * @vue-data {Form} search - Formulario de creación de una búsqueda
 * @vue-data {Number} [min_value=10] - Mínimo de tweets que se pueden recuperar
 * @vue-data {Number} [max_value=50] - Máximo de tweets que se pueden recuperar
 * @vue-data {Number} [height=12] - Grosor slider seleccion de tweets
 * @vue-data {Date} range - Fechas de selección de tweets
 * @vue-data {String} masks - Formato de selección de fechas
 * @vue-data {Date} min_date - Fecha mínima que se puede seleccionar
 * @vue-data {Date} max_date - Fecha máxima que se puede seleccionar
 * @vue-computed {Boolean} isLoggedIn
 * @vue-event CreateSearch - Crea una nueva búsqueda
 * @vue-event RepeatSearch - Repite una búsqueda realizada anteriormente
 */

export default {
name: 'Home',
components: { VCalendar, VueSlider},
data(){
    return {
        search: {
            title: '',
            type: '',
            start_date: '',
            end_date: '',
            num_tweets: 10,
        },
        min_value:10,
        max_value:50,
        height: 12,
        range: {
            start: new Date().toISOString().slice(0, 10),
            end: new Date().toISOString().slice(0, 10),
        },
        masks: {
            input: 'YYYY-MM-DD',
        },
        min_date: new Date(Date.now() - 6 * 24 * 60 * 60 * 1000),
        max_date: new Date().toISOString().slice(0, 10),
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
    async CreateSearch() {
        // Comprobacion de campos introducidos
        if (this.search.type == '' || this.search.title == '')
            $('#modalHome').modal()
        else {
            this.search.start_date = this.range.start
            this.search.end_date = this.range.end
            // Creacion de busqueda de tweets
            if(this.search.type=="Tweet") {
                try {
                    await this.createSearch(this.search);
                    await this.$store.dispatch('viewMe');
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
                    await this.$store.dispatch('viewMe');
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
#date-picker {
    background-color: #f5f5ff;
}
#container-date1 {
    margin-right: 10px;
}
#container-date2 {
    margin-top: 10px;
    margin-left: 10px;
}
#slider {
    margin-top: 20px;
}
</style>
