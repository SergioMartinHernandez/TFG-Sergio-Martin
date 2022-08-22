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
      <BarChart v-if="loaded" :chart-data="chartData" />
      <!-- <PieChart v-if="loaded" :chart-data="chartData" /> -->
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
import BarChart from '/src/components/BarChart.vue'
// import PieChart from '/src/components/PieChart.vue'

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

  name: 'Bar',
  components: { BarChart },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted () {
    this.loaded = false

    try {
      const value = [];
      
      for(var tweet in this.tweetSearch) {
          value[tweet] = this.tweetSearch[tweet].retweet_count + this.tweetSearch[tweet].reply_count + this.tweetSearch[tweet].like_count  + this.tweetSearch[tweet].quote_count;
      }
      //console.log(value)

      this.chartData = {
        labels: [1,2,3,4,5,6,7,8,9,10],
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
  

  // name: 'Pie',
  // components: { PieChart },
  // data: () => ({
  //   loaded: false,
  //   chartData: null
  // }),
  // async mounted () {
  //   this.loaded = false

  //   try {
  //     var value = [];
  //     for(var tweet in this.tweetSearch) {
  //         value[tweet] = this.tweetSearch[tweet].created_at;
  //     }
  //     console.log(typeof value)

  //     for(var s in this.value){
  //       console.log(Collections.frequency(value,s));
  //     }


  //     this.chartData = {
  //       labels: value,
  //       datasets: [
  //         {
  //           label: "Data One",
  //           backgroundColor: "#f87979",
  //           data: [1, 3,3, 4, 5, 6]
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
