<template>
  <Doughnut :chart-data="chartData" :chart-options="chartOptions"/>
</template>

<script>
import { Doughnut } from 'vue-chartjs/legacy'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from '../../node_modules/chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement)

export default {
  name: 'DoughnutChart',
  components: { Doughnut },
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