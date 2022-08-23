<template>
  <section>
    <div class="container">
        <div class="row">
          <div id="charts-col" class="col-md-7">
            <div id="card-charts" class="card">
              <div class="card-header">
                Total interactions RTs + Likes + Replys + Quotes Last 10 tweets
              </div>
              <div class="card-body">
                <!-- Grafica de lineas -->
                <LineChart id="charts" v-if="loaded" :chart-data="chartData" />
              </div>
            </div>
          </div>
          <div id="charts-col" class="col-md-5">
             <div id="card-charts" class="card">
              <div class="card-header">
                Most Repeated Words
              </div>
              <div class="card-body">
                <!-- Grafica donuts -->    
                <DoughnutChart id="charts" v-if="loaded2" :chart-data="chartData2" />
              </div>
            </div>
          </div>
        </div>
        <div class="row">
              <div class="col">
                  <div id="cards" v-for="tweet in tweetSearch" :key="tweet.id" class="card bg-light">
                    <div class="card-body">
                      <h6><strong>Username: </strong>{{ tweet.author }}</h6>
                      <!-- Texto del tweet -->
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
                          <button id="saveTweetButton" class="btn btn-primary" type="button" @click="saveTweet(tweet.id)">Guardar tweet</button>
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
import LineChart from '/src/components/LineChart.vue'
import DoughnutChart from '/src/components/DoughnutChart.vue'
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'UserAnalysis',
  created: function() {
    return this.$store.dispatch('viewTweetSearch');
  },
  computed: {
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
    
  },
  // Metodo para guardar tweet en el perfil
  methods: {
    ...mapActions(['saveTweet']),
    saveTweetUser(idTweet) {
      try {
        this.saveTweet(idTweet);
        window.alert("Tweet saved successfully");
      } catch (error) {
        console.error(error);
      }
    },
  },

// Graficos
// Grafico de lineas con las interaciones de los ultimos tweets
// Grafico donuts de palabras mas repetidas en los tweets
  name: 'Charts',
  components: { LineChart, DoughnutChart },
  data: () => ({
    // Datos grafica de lineas
    loaded: false,
    chartData: null,
    // Datos grafica donuts
    loaded2: false,
    chartData2: null
  }),
  async mounted () {
    this.loaded = false
    this.loaded2 = false

    try {
      // Se añaden los datos a la grafica de lineas
      const value = [];
      
      for(var tweet in this.tweetSearch) {
          value[tweet] = this.tweetSearch[tweet].retweet_count + this.tweetSearch[tweet].reply_count + this.tweetSearch[tweet].like_count  + this.tweetSearch[tweet].quote_count;
      }

      this.chartData = {
        labels: [1,2,3,4,5,6,7,8,9,10],
        datasets: [
          {
            label: "Total interactions",
            backgroundColor: "#f87979",
            data: value
          }
        ]
      };
      this.loaded = true

      // Se añaden los datos a la grafica donuts
      var tweetsText = new String()
      var wordsSplit = new String()
      var count
      var wordsCounter = new Map()

      for(var tweet in this.tweetSearch) {
          tweetsText = tweetsText + this.tweetSearch[tweet].text.toLocaleLowerCase()
      }

      wordsSplit = tweetsText.split(" ");    
      for(let i = 0; i < wordsSplit.length; i++) {    
            count = 1;    
            for(let j = i+1; j < wordsSplit.length; j++) {    
                if(wordsSplit[i] == wordsSplit[j]) {    
                    count++;      
                    wordsSplit[j] = "0";    
                }    
            } 
            if(count > 1 && wordsSplit[i] != "0")   
                wordsCounter.set(wordsSplit[i],count)  
      }   
      var wordsRepeated = new Map([...wordsCounter.entries()].sort((a, b) => a[1] - b[1]));  
      var counter = new Array()
      wordsRepeated.forEach(function (value, key, mapObj) 
      { 
          if(wordsRepeated.size > 10) {
            wordsRepeated.delete(key)
          } else {
            counter.push(value)
          }
      });

      this.chartData2 = {
        labels: wordsRepeated.keys(),
        datasets: [
          {
            label: "Most Repeated Words",
            backgroundColor: ['#41B883', '#7C8CF8', '#E46651', '#00D8FF', '#DD1B16', '#f87979', '#a8a032', '#8c8c84', '#bf117a', '#bf6011'],
            data: counter
          }
        ]
      };
      this.loaded2 = true
    } catch (e) {
      console.error(e)
    }
  },
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
#graphs {
  margin: 20px;
}
#cards {
  margin: 20px;
}
#card-charts {
  margin: 20px;
}
</style>