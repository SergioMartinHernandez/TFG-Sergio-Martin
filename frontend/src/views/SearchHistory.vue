<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <vue-table-dynamic :params="params" ref="table" @select="onSelect" @selection-change="onSelectionChange"></vue-table-dynamic>
      <!-- <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Type</th>
            <th scope="col">Search Day</th>
            <th scope="col">Start Date</th>
            <th scope="col">End Date</th>
            <th scope="col">Num Tweets</th>
            <th scope="col">Repeat Search</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(search, index) in user.searchs" :key="search.id">
            <th scope="row">{{ index }}</th>
            <td>{{ search.title }}</td>
            <td>{{ search.type }}</td>
            <td>{{ search.created_at }}</td>
            <td>{{ search.start_date }}</td>
            <td>{{ search.end_date }}</td>
            <td>{{ search.num_tweets }}</td>
            <td><button type="button" class="btn btn-primary" @click="RepeatSearch(search)">Repeat Search</button></td>
          </tr>
        </tbody>
      </table> -->
    </div>
  </section>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';
import VueTableDynamic from 'vue-table-dynamic'

export default {
  name: 'SearchHistory',
  components: { VueTableDynamic },
  data() {
    return {
      params: {
        data: [
          ['Index', 'Title', 'Type', 'Search Day', 'Start Date', 'End Date', 'Num Tweets'],
        ],
        header: 'row',
        border: true,
        enableSearch: true,
        sort: [0,1],
        stripe: true,
        pagination: true,
        pageSize: 10,
        pageSizes: [5, 10, 20, 50],
        showCheck: true,
        columnWidth: [{column: 0, width: 80},{column: 1, width: 200}, {column: 2, width: 80},{column: 3, width: 170}, {column: 4, width: 110},{column: 5, width: 110},{column: 6, width: 100}],
        rowHeight: 70,
      },
    };
  },
  created: function() {
    this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['createSearch']),
    async RepeatSearch(search) {
      // Creacion de busqueda de tweets
      if(search.type=="Tweet") {
          try {
              await this.createSearch(search);
              await this.$store.dispatch('viewTweetSearch');
              this.$router.push('/tweetanalysis');
          } catch (error) {
              throw 'Error in create search tweet. Please try again.';
          }
      }
      // Creacion de busqueda de usuarios
      else if(search.type=="User"){
          try {
              await this.createSearch(search);
              await this.$store.dispatch('viewUserSearch');
              await this.$store.dispatch('viewTweetSearch');
              this.$router.push('/useranalysis');
          } catch (error) {
              throw 'Error in create search user. Please try again.';
          }
      }
    },
    onSelect (isChecked, index, data) {
      //console.log('onSelect: ', isChecked, index, data)
      //console.log('Checked Data:', this.$refs.table.getCheckedRowDatas(true))
    },
    onSelectionChange (checkedDatas, checkedIndexs, checkedNum) {
      //console.log('onSelectionChange: ', checkedDatas, checkedIndexs, checkedNum)
    },
    // downloadCSV() {
    //   // var html = document.querySelector("vue-table-dynamic");
	  //   // htmlToCSV(html, "students.csv");
    // },

  },
  async mounted () {
      // Carga de datos tabla de historial de búsquedas
      for (let i = 0; i < this.user.searchs.length; i++) {
        this.params.data.push([i+1, 
        this.user.searchs[i].title,  
        this.user.searchs[i].type,
        this.user.searchs[i].created_at, 
        this.user.searchs[i].start_date, 
        this.user.searchs[i].end_date,
        this.user.searchs[i].num_tweets],
        )
      }
  }, 
}
</script>

<style scoped>
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5ff;
    height: 100%;
}
</style>
