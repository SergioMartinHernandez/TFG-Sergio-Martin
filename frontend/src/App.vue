<template>
  <div id="app">
    <NavBar/>
    <div class="main-Container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from '/src/components/NavBar.vue'
import BarChart from '/src/components/BarChart.vue'
export default {
  components: {
    NavBar,
    BarChart 
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #0d6efd;
  height: 100%;
}

body, main {
    height: 100vh;
}
</style>