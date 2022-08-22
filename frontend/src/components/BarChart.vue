<!-- <template>
  <div class="container">
    <Bar v-if="loaded" :chart-data="chartData" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { mapGetters, mapActions } from 'vuex';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  created: function() {
    this.$store.dispatch('viewUserSearch');
    this.$store.dispatch('viewTweetSearch');

  },
  computed: {
    ...mapGetters({userSearch: 'stateUserSearch' }),
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
  },
  data: () => ({
    loaded: false,
    chartData: null
  }),
  async mounted () {
    this.loaded = false
    function chart(id, fecha, age, eye) {
      this.id = id;
      this.fecha = fecha;
    }

    try {
      // const value = [];
      // for(var tweet in this.tweetSearch) {
      //     value[tweet] = this.tweetSearch[tweet].created_at;
      // }

      // //console.log(value)
      // this.chartData = Object.assign({}, value);
      // console.log(this.chartData)

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script> -->


<template>
  <Bar :chart-data="chartData" :chart-options="chartOptions" />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    chartData: {
        type: Object,
        required: true
      },
    chartOptions: {
      type: Object,
      default: () => {}
    }
  }
}
</script>