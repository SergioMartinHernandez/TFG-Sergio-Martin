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
export default {
  components: {
    NavBar,
  },
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #f5f5ff;
  min-height: 100vh;
}

body, main {
  height: 100vh;
}
</style>