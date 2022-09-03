<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <!-- Modal para muestra de correcto guardado de tweet -->
      <div class="modal fade" id="modalTweetSave" tabindex="-1" role="dialog" aria-labelledby="modalTweetSave" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Info</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Tweets saved successfully.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
      <h4>Analysis of user: @{{ userSearch.username }}</h4>
      <br/>
      <div class="row">
        <div class="col-md-auto">
          <!-- Foto de perfil -->
          <img :src="userSearch.profile_image_url" id="profile-picture" class="rounded-circle img-fluid" alt="">
        </div>
        <div class="col align-self-center">
          <!-- Nombre de usuario -->
          @{{ userSearch.username }}
          <!-- Verificado si tiene -->
          <svg v-if="userSearch.verified" xmlns="http://www.w3.org/2000/svg" id  width="16" height="16" fill="currentColor" class="bi bi-patch-check" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M10.354 6.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
            <path d="m10.273 2.513-.921-.944.715-.698.622.637.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01.622-.636a2.89 2.89 0 0 1 4.134 0l-.715.698a1.89 1.89 0 0 0-2.704 0l-.92.944-1.32-.016a1.89 1.89 0 0 0-1.911 1.912l.016 1.318-.944.921a1.89 1.89 0 0 0 0 2.704l.944.92-.016 1.32a1.89 1.89 0 0 0 1.912 1.911l1.318-.016.921.944a1.89 1.89 0 0 0 2.704 0l.92-.944 1.32.016a1.89 1.89 0 0 0 1.911-1.912l-.016-1.318.944-.921a1.89 1.89 0 0 0 0-2.704l-.944-.92.016-1.32a1.89 1.89 0 0 0-1.912-1.911l-1.318.016z"/>
          </svg>
        </div>
      </div> 
      <div class="row"> 
        <div id="description" class="col-md-auto">
          <!-- Descripcion -->
          <strong>Description: </strong>{{ userSearch.description }}
        </div>
      </div>
      <div class="row">
        <div class="col-4">
          <!-- Nombre -->
          <strong>Name: </strong>{{ userSearch.name }}
        </div>
        <div class="col-4">
          <!-- Fecha de creacion de la cuenta -->
          <strong>Created at: </strong>{{ userSearch.created_at }}
        </div>
        <div class="col-4">
          <!-- Ubicacion -->
          <strong>Location: </strong>{{ userSearch.location }}
        </div>
      </div>
      <hr class="solid">
      <div class="row">
          <div class="col" id="border-black">
            <!-- Numero de seguidores -->
            <h4>Followers count</h4><h2>{{ userSearch.followers_count }}</h2>
          </div>
          <div class="col" id="border-black">
            <!-- Numero de seguidos -->
            <h4>Following count</h4><h2>{{ userSearch.following_count }}</h2>
          </div>
          <div class="col" id="border-black">
            <!-- Numero de tweets -->
            <h4>Tweet count</h4><h2>{{ userSearch.tweet_count }}</h2>
          </div>
      </div>
      <div class="row">
        <div id="charts-col" class="col">
          <div id="card-charts" class="card">
            <div class="card-header">
              Time graph of tweets
            </div>
            <div class="card-body">
              <!-- Grafica de tiempo -->    
              <apexcharts v-if="loaded2" height="350" width="500" type="line" :options="chartOptions" :series="series"></apexcharts>
            </div>
          </div>
        </div>
        <div id="charts-col" class="col">
          <div id="card-charts" class="card">
            <div class="card-header">
              Most Repeated Words
            </div>
            <div class="card-body">
              <!-- Grafica nube -->    
              <wordcloud v-if="loaded" :data="defaultWords" :fontSize="[50,100]" nameKey="name" valueKey="value" :color="myColors" :showTooltip="true" :wordClick="wordClickHandler"></wordcloud>
            </div>
          </div>
        </div>
      </div>
      <!-- Boton guardar tweets -->
      <button type="button" class="btn btn-primary" @click="saveTweets()">Save selected tweets</button>
      <!-- <button type="button" class="btn btn-secondary" @click="downloadCSV()">Download csv</button> -->
      <!-- Tabla con los tweets -->
      <vue-table-dynamic :params="params" ref="table" @select="onSelect" @selection-change="onSelectionChange"></vue-table-dynamic>
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
import wordcloud from 'vue-wordcloud'
import VueApexCharts from 'vue-apexcharts'
import VueTableDynamic from 'vue-table-dynamic'

export default {

  name: 'UserAnalysis',
  computed: {
    ...mapGetters({userSearch: 'stateUserSearch' }),
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
  },

// Graficos Y Tablas
name: 'GraphsAndTable',
  components: {
    wordcloud, apexcharts: VueApexCharts, VueTableDynamic 
  },
  methods: {
    ...mapActions(['saveTweet']),
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
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
    // Metodo para guardar tweet en el perfil
    saveTweets() {
      var data = this.$refs.table.getCheckedRowDatas(true)
      for (let i = 1; i < data.length; i++) {
        var url = data[i][7]
        for (let j = 0; j < this.tweetSearch.length; j++) {
          if(this.tweetSearch[j].url===url) {
            this.saveTweet(this.tweetSearch[j].id);
          }
        }
      }
      $('#modalTweetSave').modal()
    }
  },
  data() {
    return {
      loaded: false,
      loaded2: false,
      // Datos de grafico nube
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      defaultWords: [],
      // Datos de grafico de lineas
      chartOptions: {
        chart: {
          id: "basic-bar",
        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          title: {
            text: 'NumTweets'
        },
      },
      },
      series: [
        {
          data: [],
        },
      ],
      params: {
        data: [
          ['Index', 'Username', 'Text', 'Reply count', 'Retweet count', 'Likes count', 'Created at', 'URL'],
        ],
        header: 'row',
        border: true,
        enableSearch: true,
        sort: [0,1,3,4,5,6],
        stripe: true,
        pagination: true,
        pageSize: 10,
        pageSizes: [5, 10, 20, 50],
        showCheck: true,
        columnWidth: [{column: 0, width: 80},{column: 1, width: 130}, {column: 2, width: 1800},{column: 3, width: 110}, {column: 4, width: 110},{column: 5, width: 110},{column: 6, width: 120},{column: 7, width: 400}],
        rowHeight: 70,
      }
    }
  },
  async mounted () {
      this.loaded = false
      this.loaded2 = false

      // Se añaden los datos a la grafica de nube
      var tweetsText = new String()
      var wordsSplit = new String()
      var words = new String()
      var wordClean = new String()
      var count
      var tweetObject
      var wordsCounter = new Map()
      var stopWordsES = ['vuelva','realizar','vimos','semana','pasada','luego','dices','k','poner','hablamos','favor','sale','digo','miro','tarde','saludo','dejan','dado','quería','necesitaría','decir','día','hacerlo','hace','muchas','pedimos','ido','genial','preguntar','quedo','pasa','días','tardes','buenas','necesito','buenos','hola','gracias','quieres','quiero','de','la','que','el','en','y','a','los','del','se','las','por','un','para','con','no','una','su','al','lo','como','más','pero','sus','le','ya','o','este','sí','porque','esta','entre','cuando','muy','sin','sobre','también','me','hasta','hay','donde','quien','desde','todo','nos','durante','todos','uno','les','ni','contra','otros','ese','eso','ante','ellos','e','esto','mí','antes','algunos','qué','unos','yo','otro','otras','otra','él','tanto','esa','estos','mucho','quienes','nada','muchos','cual','poco','ella','estar','estas','algunas','algo','nosotros','mi','mis','tú','te','ti','tu','tus','ellas','nosotras','vosotros','vosotras','os','mío','mía','míos','mías','tuyo','tuya','tuyos','tuyas','suyo','suya','suyos','suyas','nuestro','nuestra','nuestros','nuestras','vuestro','vuestra','vuestros','vuestras','esos','esas','estoy','estás','está','estamos','estáis','están','esté','estés','estemos','estéis','estén','estaré','estarás','estará','estaremos','estaréis','estarán','estaría','estarías','estaríamos','estaríais','estarían','estaba','estabas','estábamos','estabais','estaban','estuve','estuviste','estuvo','estuvimos','estuvisteis','estuvieron','estuviera','estuvieras','estuviéramos','estuvierais','estuvieran','estuviese','estuvieses','estuviésemos','estuvieseis','estuviesen','estando','estado','estada','estados','estadas','estad','he','has','ha','hemos','habéis','han','haya','hayas','hayamos','hayáis','hayan','habré','habrás','habrá','habremos','habréis','habrán','habría','habrías','habríamos','habríais','habrían','había','habías','habíamos','habíais','habían','hube','hubiste','hubo','hubimos','hubisteis','hubieron','hubiera','hubieras','hubiéramos','hubierais','hubieran','hubiese','hubieses','hubiésemos','hubieseis','hubiesen','habiendo','habido','habida','habidos','habidas','soy','eres','es','somos','sois','son','sea','seas','seamos','seáis','sean','seré','serás','será','seremos','seréis','serán','sería','serías','seríamos','seríais','serían','era','eras','éramos','erais','eran','fui','fuiste','fue','fuimos','fuisteis','fueron','fuera','fueras','fuéramos','fuerais','fueran','fuese','fueses','fuésemos','fueseis','fuesen','siendo','sido','tengo','tienes','tiene','tenemos','tenéis','tienen','tenga','tengas','tengamos','tengáis','tengan','tendré','tendrás','tendrá','tendremos','tendréis','tendrán','tendría','tendrías','tendríamos','tendríais','tendrían','tenía','tenías','teníamos','teníais','tenían','tuve','tuviste','tuvo','tuvimos','tuvisteis','tuvieron','tuviera','tuvieras','tuviéramos','tuvierais','tuvieran','tuviese','tuvieses','tuviésemos','tuvieseis','tuviesen','teniendo','tenido','tenida','tenidos','tenidas','tened','ahí','ajena','ajeno','ajenas','ajenos','algúna','allá','ambos','aquello','aquellas','aquellos','así','atrás','aun','aunque','bajo','bastante','bien','cabe','cada','casi','cierto','cierta','ciertos','ciertas','conmigo','conseguimos','conseguir','consigo','consigue','consiguen','consigues','cualquier','cualquiera','cualquieras','cuan','cuanto','cuanta','cuantas','cuantos','de','dejar','demás','demasiadas','demasiados','dentro','dos','ello','emplean','emplear','empleas','encima','entonces','era','eras','eramos','eses','estes','gueno','hacer','hacemos','hacia','hago','incluso','intenta','intentas','intentamos','intentan','intento','ir','mismo','ningúno','nunca','parecer','podemos','podría','podrías','podríais','podríamos','podrían','primero','puedes','pueden','pues','querer','quiénes','quienesquiera','quienquiera','quizás','sabe','sabes','saben','sabéis','sabemos','saber','sino','solo','esta','tampoco','tan','tanta','tantas','tantos','tener','tiempo','toda','todas','tomar','trabaja','trabajas','tras','último','ultimo','última','ultima','unas','ustedes','variasos','verdadera','pocas','pocos','podéis','podemos','poder','podría','podrías','podríais','podríamos','podrían','primero','puede','puedo','pueda','pues','querer','quiénes','quienesquiera','quienquiera','quizás','mas','sabe','sabes','saben','sabéis','sabemos','saber','según','ser','si','siempre','sino','so','solamente','solo','sólo','sr','sra','sres','sta','tal','tales','tampoco','tan','tanta','tantas','tantos','tener','tiempo','toda','den','queria','todas','tomar','trabaja','trabajo','trabajáis','trabajamos','trabajan','trabajar','trabajas','tras','último','ultimo','unas','usa','usas','usáis','usamos','usan','usar','uso','usted','ustedes','va','van','vais','valor','vamos','varias','varias','varios','vaya','verdadera','voy','vez','más','ok'];
      var stopwordsEN = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']


      for(var tweet in this.tweetSearch) {
          tweetsText = tweetsText + this.tweetSearch[tweet].text.toLocaleLowerCase()
      }
      var res = []
      words = tweetsText.split(" "); 
      for(let i = 0; i < words.length; i++) {
        wordClean = words[i].split(".").join("")
        if(!stopwordsEN.includes(wordClean) && !stopWordsES.includes(wordClean)) {
          res.push(wordClean)
        }
      }   
      wordsSplit= res.slice(res.join(' '))
      for(let i = 0; i < wordsSplit.length; i++) {    
            count = 1;    
            for(let j = i+1; j < wordsSplit.length; j++) {    
                if(wordsSplit[i] == wordsSplit[j]) {    
                    count++;      
                    wordsSplit[j] = "0";    
                }    
            } 
            if(count > 1 && wordsSplit[i] != "0") 
              wordsCounter.set(wordsSplit[i],count)
      }  
      var wordsRepeated = new Map([...wordsCounter.entries()].sort((a, b) => a[1] - b[1]));  
      var counter = new Array()
      wordsRepeated.forEach(function (value, key, mapObj) 
      { 
          if(wordsRepeated.size > 10) {
            wordsRepeated.delete(key)
          } else {
            tweetObject = {name: key, value: value}
            counter.push(tweetObject)
          }
      });
      this.defaultWords = counter

      this.loaded = true
      
      // Datos de la grafica de lineas
      var differentDates = new Set()
      var dates = new Array()
      var dateFormat = new String
      for(var tweet in this.tweetSearch) {
          dateFormat = this.tweetSearch[tweet].created_at.slice(0,-9)
          dates.push(dateFormat)
          differentDates.add(dateFormat)
      }

      dates.sort()
      var counter = new Array(differentDates.size);
      counter.fill(0)
      var j = 0
      var aux=dates[0];
      for (let i = 0; i < dates.length; i++) {
          if(aux == dates[i]){ 
              counter[j]++;
          } else {
              j++;
              aux=dates[i];
              counter[j]++;
          }
      }
      this.chartOptions = {
        chart: {
          id: "basic-bar",
        },
        xaxis: {
          categories: dates,
          title: {
            text: 'Time of publication'
          }
        },
      },
      this.series = [
        {
          name: "num Tweets",
          data: counter,
        }
      ]
      this.loaded2 = true

      // Carga de datos tabla de tweets
      for (let i = 0; i < this.tweetSearch.length; i++) {
        this.params.data.push([i+1, this.tweetSearch[i].author, 
        this.tweetSearch[i].text, 
        this.tweetSearch[i].reply_count, 
        this.tweetSearch[i].retweet_count, 
        this.tweetSearch[i].like_count, 
        this.tweetSearch[i].created_at,
        this.tweetSearch[i].url])
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
#description {
  width: fit-content;
}
#buttons-card {
  text-align: center;
}
#card-charts {
  margin: 20px;
}
#cards {
  margin: 20px;
}
</style>