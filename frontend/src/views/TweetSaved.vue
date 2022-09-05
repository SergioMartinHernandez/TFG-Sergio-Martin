<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <div class="row">
        <div class="col">
          <!-- Boton eliminar tweets -->
          <button type="button" class="btn btn-danger" @click="deleteTweetUser()">Delete selected tweets</button>
        </div>
        <div class="col">
          <!-- Boton exportar tweets a csv -->
          <vue-json-to-csv v-if="tweetSaved !== null" :json-data="tweetSaved" 
          :labels="{
            author: { title: 'Author' },
            text: { title: 'Text' },
            reply_count: { title: 'Reply count'},
            retweet_count: { title: 'Retweet count'},
            like_count: { title: 'Likes count'},
            created_at: { title: 'Created at'},
            url: { title: 'URL'},
          }"
          :csv-title="'TweetSavedData'" :separator="';'">
            <button type="button" class="btn btn-success" style="float: right;">Download csv tweets</button>
          </vue-json-to-csv>
        </div>
      </div>

      
      <!-- Tabla de tweets guardados -->
      <vue-table-dynamic :params="params" ref="table" @select="onSelect" @selection-change="onSelectionChange"></vue-table-dynamic>
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
import VueTableDynamic from 'vue-table-dynamic'
import VueJsonToCsv from 'vue-json-to-csv'

export default {
  name: 'TweetSaved',
  components: { VueTableDynamic, VueJsonToCsv },
  data() {
    return {
      params: {
        data: [
          ['Index', 'Username', 'Text', 'Reply count', 'Retweet count', 'Likes count', 'Created at', 'URL'],
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
        columnWidth: [{column: 0, width: 80},{column: 1, width: 130}, {column: 2, width: 1800},{column: 3, width: 110}, {column: 4, width: 110},{column: 5, width: 110},{column: 6, width: 120},{column: 7, width: 400}],
        rowHeight: 70,
      },
    };
  },
  created: function() {
    this.$store.dispatch('viewTweetSaved');
  },
  computed: {
    ...mapGetters({tweetSaved: 'stateTweetSaved' }),
  },
  // Metodo para eliminar tweet del perfil
  methods: {
    ...mapActions(['deleteTweet']),
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
    // Metodo para eliminar tweet del perfil
    async deleteTweetUser() {
      var data = this.$refs.table.getCheckedRowDatas(true)
      
      for (let i = 1; i < data.length; i++) {
        var url = data[i][7]
        for (let j = 0; j < this.tweetSaved.length; j++) {
          if(this.tweetSaved[j].url===url) {
            await this.deleteTweet(this.tweetSaved[j].id); 
          }
        }
      }
      await this.$store.dispatch('viewTweetSaved');
      document.location.reload()
    }
  },
  async mounted () {
      // Carga de datos tabla de tweets
      for (let i = 0; i < this.tweetSaved.length; i++) {
        this.params.data.push([i+1, this.tweetSaved[i].author, 
        this.tweetSaved[i].text, 
        this.tweetSaved[i].reply_count, 
        this.tweetSaved[i].retweet_count, 
        this.tweetSaved[i].like_count, 
        this.tweetSaved[i].created_at,
        this.tweetSaved[i].url],
        )
      }
  }, 
}
</script>

<style scoped>
#profile-picture {
    height: 75px;
}
.section {
    padding: 100px 0;
    position: relative;
}
.gray-bg {
    background-color: #f5f5ff;
    height: 100%;
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
#cards {
  margin: 20px;
}
</style>