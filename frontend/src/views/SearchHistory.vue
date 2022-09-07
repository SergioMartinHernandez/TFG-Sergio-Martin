<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <vue-good-table
      refs="my-table"
      @on-selected-rows-change="selectionChanged"
      :columns="columns"
      :rows="rows"
      :select-options="{ 
        enabled: true,
        selectOnCheckboxOnly: true,
      }"
      :sort-options="{
        enabled: true,
      }"
      :search-options="{
        enabled: true,
        placeholder: 'Search in your search history table',
      }"
      :pagination-options="{
        enabled: true,
        mode: 'pages',
        perPage: 10,
        perPageDropdown: [5, 10, 25, 50]
      }">
        <div slot="selected-row-actions">
          <button type="button" class="btn btn-danger" @click="deleteSearchUser()">Delete selected searchs</button> 
        </div>
        <template slot="table-row" slot-scope="props">
          <span v-if="props.column.field == 'action'">
            <!-- Boton eliminar busquedas -->
            <button type="button" class="btn btn-primary" @click="RepeatSearch(props.row)">Repeat Search</button>
          </span>
        </template>
      </vue-good-table>
    </div>
  </section>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';
import { VueGoodTable } from 'vue-good-table';
import 'vue-good-table/dist/vue-good-table.css'
/**
 * @vue-data columns - Columnas de la tabla de historial de búsquedas
 * @vue-data rows - Filas de la tabla de historial de búsquedas
 * @vue-data selectedRows - Filas seleccionadas en la tabla
 * @vue-computed {User} user
 * @vue-event RepeatSearch - Repite una búsqueda realizada anteriormente
 * @vue-event selectionChanged - Evento de cambio de selección casillero tabla de historial de búsquedas
 * @vue-event deleteSearchUser - Borra una búsqueda realizada del historial de búsquedas
 */

export default {
  name: 'SearchHistory',
  components: { VueGoodTable },
  data() {
    return {
      columns: [
      {
        field: "id",
        label: "ID",
      },
      {
        field: "title",
        label: "Title",
      },
      {
        field: "type",
        label: "Type",
        sortable: true,
        firstSortType: 'desc'
      },
      {
        field: "created_at",
        label: "Created at",
      },
      {
        field: "start_date",
        label: "Start date",
      },
      {
        field: "end_date",
        label: "End date",
      },
      {
        field: "num_tweets",
        label: "Num tweets",
      },
      {
        field: "action",
        label: "Repeat Search",
      }
    ],
    rows: [],
    selectedRows: []
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
    ...mapActions(['deleteSearch']),
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
    selectionChanged (params) {
      this.selectedRows = params.selectedRows
    },
    async deleteSearchUser() {
      var data = this.selectedRows;
      console.log(data)
       for (let i = 0; i < data.length; i++) {
          console.log(data[i].id)
          await this.deleteSearch(data[i].id);
          await this.$store.dispatch('viewMe');
       }
      document.location.reload()
    },  
  },
  async mounted () {
      // Carga de datos tabla de historial de búsquedas
      for (let i = 0; i < this.user.searchs.length; i++) {
        this.rows.push(this.user.searchs[i])
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
