<template>
  <section>
    <div class="container">
        <div class="row">
            <div class="col">
            Followers count
            </div>
            <div class="col">
            Following count
            </div>
            <div class="col">
            Tweet count
            </div>
        </div>
        <div class="row">
            <div class="col">
              <bar-chart></bar-chart>
            </div>
            <div class="col">
            Grafica 2
            </div>
        </div>
    </div>
  </section>
</template>


<script>
import BarChart from '@/views/graphs/BarChart.vue'
export default {
  components: {
    BarChart
  }
}
</script>