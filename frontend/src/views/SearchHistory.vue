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
      <!-- <LineChart v-if="loaded" :chart-data="chartData" /> -->
      <!-- <DoughnutChart v-if="loaded" :chart-data="chartData" /> -->
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
import LineChart from '/src/components/LineChart.vue'
// import DoughnutChart from '/src/components/DoughnutChart.vue'

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

// Grafico de lineas con las interaciones de los ultimos tweets
  name: 'LineC',
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted () {
    this.loaded = false

    try {
      var value = new Array();
      var numberTweets = new Array()
      var counter = 1
      
      for(var tweet in this.tweetSearch) {
          value[tweet] = this.tweetSearch[tweet].retweet_count + this.tweetSearch[tweet].reply_count + this.tweetSearch[tweet].like_count  + this.tweetSearch[tweet].quote_count;
          numberTweets[counter-1] = counter
          counter++
      }

      this.chartData = {
        labels: numberTweets,
        datasets: [
          {
            label: "Total interactions RTs + Likes + Replys + Quotes Last 10 tweets",
            backgroundColor: "#f87979",
            data: value
          }
        ]
      };
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
  
// Grafico donuts de fechas en las que se han publicado los ultimos 10 tweets
//   name: 'Doughnut',
//   components: { DoughnutChart },
//   data: () => ({
//     loaded: false,
//     chartData: null
//   }),
//   async mounted () {
//     this.loaded = false

//     try {
//       var differentDates = new Set()
//       var dates = new Array()
//       for(var tweet in this.tweetSearch) {
//           dates.push(this.tweetSearch[tweet].created_at)
//           differentDates.add(this.tweetSearch[tweet].created_at)
//       }

//       dates.sort()
//       var counter = new Array(differentDates.size);
//       counter.fill(0)
//       var j = 0
//       var aux=dates[0];
//       for (let i = 0; i < dates.length; i++) {
//           if(aux == dates[i]){
              
//               counter[j]++;
//           } else {
//               j++;
//               aux=dates[i];
//               contador[j]++;
//           }
//       }
//       this.chartData = {
//         labels: differentDates,
//         datasets: [
//           {
//             label: "Last 10 Tweets Date",
//             backgroundColor: ['#41B883', '#7C8CF8', '#E46651', '#00D8FF', '#DD1B16', '#f87979', '#a8a032', '#8c8c84', '#bf117a', '#bf6011'],
//             data: counter
//           }
//         ]
//       };
//       this.loaded = true
//     } catch (e) {
//       console.error(e)
//     }
//   }
// }

// Grafico donuts de palabras mas repetidas en los tweets
  // name: 'Doughnut',
  // components: { DoughnutChart },
  // data: () => ({
  //   loaded: false,
  //   chartData: null
  // }),
  // async mounted () {
  //   this.loaded = false

  //   try {
  //     var tweetsText = new String()
  //     var wordsSplit = new String()
  //     var count
  //     var wordsCounter = new Map()

  //     for(var tweet in this.tweetSearch) {
  //         tweetsText = tweetsText + this.tweetSearch[tweet].text.toLocaleLowerCase()
  //     }

  //     wordsSplit = tweetsText.split(" ");    
  //     for(let i = 0; i < wordsSplit.length; i++) {    
  //           count = 1;    
  //           for(let j = i+1; j < wordsSplit.length; j++) {    
  //               if(wordsSplit[i] == wordsSplit[j]) {    
  //                   count++;      
  //                   wordsSplit[j] = "0";    
  //               }    
  //           } 
  //           if(count > 1 && wordsSplit[i] != "0")   
  //               wordsCounter.set(wordsSplit[i],count)  
  //     }   
  //     var wordsRepeated = new Map([...wordsCounter.entries()].sort((a, b) => a[1] - b[1]));  
  //     var counter = new Array()
  //     wordsRepeated.forEach(function (value, key, mapObj) 
  //     { 
  //         if(wordsRepeated.size > 10) {
  //           wordsRepeated.delete(key)
  //         } else {
  //           counter.push(value)
  //         }
  //     });

  //     this.chartData = {
  //       labels: wordsRepeated.keys(),
  //       datasets: [
  //         {
  //           label: "Most Repeated Words",
  //           backgroundColor: ['#41B883', '#7C8CF8', '#E46651', '#00D8FF', '#DD1B16', '#f87979', '#a8a032', '#8c8c84', '#bf117a', '#bf6011'],
  //           data: counter
  //         }
  //       ]
  //     };
  //     this.loaded = true
  //   } catch (e) {
  //     console.error(e)
  //   }
  // }
}
</script>

<style>
.container{
    margin-top: 3%;
    padding: 5em;
    background-color: aliceblue;
}
</style>
