<template>
  <section>
    <div class="container">
        <div class="row align-items-center">
          <div class="col-md-auto">
            <!-- Foto de perfil -->
            <img :src="userSearch.profile_image_url" id="profile-picture" class="rounded-circle img-fluid" alt="">
          </div>
          <div class="col-md-auto">
          <!-- Nombre de usuario -->
          @{{ userSearch.username }}
          <!-- Verificado si tiene -->
            <svg v-if="userSearch.verified" xmlns="http://www.w3.org/2000/svg" id  width="16" height="16" fill="currentColor" class="bi bi-patch-check" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M10.354 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
              <path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>
            </svg>
            <br>
            <!-- Descripcion -->
            <strong>Description: </strong>{{ userSearch.description }}
          </div>
          <div class="col">
            <!-- Nombre -->
            <strong>Name: </strong>{{ userSearch.name }}
          </div>
          <div class="col">
            <!-- Fecha de creacion de la cuenta -->
            <strong>Created at: </strong>{{ userSearch.created_at }}
          </div>
          <div class="col">
            <!-- Ubicacion -->
            <strong>Location: </strong>{{ userSearch.location }}
          </div>
        </div>
        <hr class="solid">
        <div class="row">
            <div class="col" id="border-black">
              <!-- Numero de seguidores -->
              <h4>Followers count</h4><h2>{{ userSearch.followers_count }}</h2>
            </div>
            <div class="col" id="border-black">
              <!-- Numero de seguidos -->
              <h4>Following count</h4><h2>{{ userSearch.following_count }}</h2>
            </div>
            <div class="col" id="border-black">
              <!-- Numero de tweets -->
              <h4>Tweet count</h4><h2>{{ userSearch.tweet_count }}</h2>
            </div>
        </div>
        <div class="row">
            <div class="col">
              Grafica 1
              <!-- <Bar v-if="loaded" :chart-data="chartData" /> -->
            </div>
            <div class="col">
            Grafica 2
            </div>
        </div>
        <div class="row">
              <div class="row">
                  <div v-for="tweet in tweetSearch" :key="tweet.id" class="card bg-light">
                    <div class="card-body">
                      <h6><strong>Username: </strong>{{ tweet.author }}</h6>
                      <!-- TEXTO TWEET -->
                      <p>{{ tweet.text }}</p>
                      <div class="row">  
                        <div id="stats-tweet" class="col-2">                    
                          <!-- Icono Respuestas -->
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-reply" viewBox="0 0 16 16">
                            <path d="M6.598 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822.984.624 1.99 1.76 2.595 3.876-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306 7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L7.3 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L2.614 8.254a.503.503 0 0 0-.042-.028.147.147 0 0 1 0-.252.499.499 0 0 0 .042-.028l3.984-2.933zM7.8 10.386c.068 0 .143.003.223.006.434.02 1.034.086 1.7.271 1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"/>
                          </svg>
                          <!-- Numero Respuestas -->
                          {{ tweet.reply_count }}
                        </div>
                        <div id="stats-tweet" class="col-3">
                          <!-- Icono Retweets -->
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-repeat" viewBox="0 0 16 16">
                            <path d="M11 5.466V4H5a4 4 0 0 0-3.584 5.777.5.5 0 1 1-.896.446A5 5 0 0 1 5 3h6V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192Zm3.81.086a.5.5 0 0 1 .67.225A5 5 0 0 1 11 13H5v1.466a.25.25 0 0 1-.41.192l-2.36-1.966a.25.25 0 0 1 0-.384l2.36-1.966a.25.25 0 0 1 .41.192V12h6a4 4 0 0 0 3.585-5.777.5.5 0 0 1 .225-.67Z"/>
                          </svg>
                          <!-- Numero Retweets -->
                          {{ tweet.retweet_count }}
                        </div>
                        <div id="stats-tweet" class="col-3">
                          <!-- Icono Me gustas -->
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                          </svg>
                          <!-- Numero Me gustas -->
                          {{ tweet.like_count }}
                        </div>
                        <div id="stats-tweet" class="col-4">
                          <!-- Numero Fecha de publicacion -->
                          {{ tweet.created_at }}
                        </div>
                      </div>
                    </div>
                    <div class="card-footer">
                      <div class="row">
                        <div class="col-lg-6" id="buttons-card">
                          <!-- Enlace al tweet -->
                          <a class="btn btn-primary" id="buttons-card" :href="tweet.url" role="button">Link</a>
                        </div>
                        <div class="col-lg-6">
                          <input class="btn btn-primary" type="submit" value="Guardar tweet">
                        </div>
                      </div>
                    </div>  
                  </div>
              </div>
          </div>
    </div>
  </section>
</template>


<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { mapGetters, mapActions } from 'vuex';

//ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
export default {
  name: 'UserAnalysis',
  created: function() {
    this.$store.dispatch('viewUserSearch');
    this.$store.dispatch('viewTweetSearch');
  },
  computed: {
    ...mapGetters({userSearch: 'stateUserSearch' }),
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
    
  },
  methods: {
  },

  // name: 'BarChart',
  // components: { Bar },
  // data: () => ({
  //   loaded: false,
  //   chartData: null
  // }),
  // async mounted () {
  //   this.loaded = false

  //   try {
  //     const { userlist } = await fetch('/api/userlist')
  //     this.chartdata = userlist

  //     this.loaded = true
  //   } catch (e) {
  //     console.error(e)
  //   }
  // }
}
</script>

<style>
#profile-picture {
    height: 75px;
}
.container{
    margin-top: 3%;
    padding: 5em;
    background-color: aliceblue;
}
/* Separador entre la informacion del usuario y los datos de seguidores */
hr.solid {
  border-top: 3px solid #bbb;
}
#no-padding-right {
  padding-right: 3px;
}
#no-padding-left {
  padding-left: 3px;
  padding-top: 4px;
}
#border-black {
  border: 1px solid grey;
  margin: 0px 4px 0px 4px;
  text-align: center;
}
#stats-tweet {
  padding-right: 10px;
  text-align: center;
}
#buttons-card {
  text-align: center;
}
</style>