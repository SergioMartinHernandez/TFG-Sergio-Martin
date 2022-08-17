<template>
  <section>
    <div class="container">
      <div v-for="search in user.searchs" :key="search.id">
        {{ search.title }}
        {{ search.type }}
      </div>
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'SearchHistory',
  created: function() {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
  },

}
</script>

<style>
.container{
    margin-top: 3%;
    padding: 5em;
    background-color: aliceblue;
}
</style>
