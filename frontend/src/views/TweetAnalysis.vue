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
              Tweet deleted successfully.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
      <h4>Analysis of term: {{ Object.values(this.user.searchs).pop().title }}</h4>
      <br/>
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
              <wordcloud v-if="loaded" :data="defaultWords" nameKey="name" valueKey="value" :color="myColors" :showTooltip="true" :wordClick="wordClickHandler"></wordcloud>
            </div>
          </div>
        </div>
      </div>
      <!-- <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Username</th>
            <th scope="col">Text</th>
            <th scope="col">Reply count</th>
            <th scope="col">Retweets count</th>
            <th scope="col">Like count</th>
            <th scope="col">Created at</th>
            <th scope="col">Save Tweet</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="(tweet, index) in tweetSearch" :key="tweet.id">
            <th scope="row">{{ index +1 }}</th>
            <td>{{ tweet.author }}</td>
            <td>{{ tweet.text }}</td>
            <td>{{ tweet.reply_count }}</td>
            <td>{{ tweet.retweet_count }}</td>
            <td>{{ tweet.like_count }}</td>
            <td>{{ tweet.created_at }}</td>
            <td><input class="form-check-input" type="checkbox" value="" id="defaultCheck1"></td>
          </tr>
        </tbody>
      </table> -->
      <vue-table-dynamic :params="params" ref="table" @select="onSelect" @selection-change="onSelectionChange"></vue-table-dynamic>
      <div class="row">
        <div class="col">
            <div id="cards" v-for="(tweet, index) in tweetSearch" :key="tweet.id" class="card bg-light">
              <div class="card-body">
                <h5 class="text-right"><strong>{{ index+1 }}</strong></h5>
                <h6><strong>Username: </strong>{{ tweet.author }}</h6>
                <!-- Texto del tweet -->
                <p>{{ tweet.text }}</p>
                <div class="row">  
                  <div id="stats-tweet" class="col-2">                    
                    <!-- Icono Respuestas -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-reply" viewBox="0 0 16 16">
                      <path d="M6.598 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822.984.624 1.99 1.76 2.595 3.876-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306 7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L7.3 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L2.614 8.254a.503.503 0 0 0-.042-.028.147.147 0 0 1 0-.252.499.499 0 0 0 .042-.028l3.984-2.933zM7.8 10.386c.068 0 .143.003.223.006.434.02 1.034.086 1.7.271 1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"/>
                    </svg>
                    <!-- Numero Respuestas -->
                    {{ tweet.reply_count }}
                  </div>
                  <div id="stats-tweet" class="col-3">
                    <!-- Icono Retweets -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-repeat" viewBox="0 0 16 16">
                      <path d="M11 5.466V4H5a4 4 0 0 0-3.584 5.777.5.5 0 1 1-.896.446A5 5 0 0 1 5 3h6V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192Zm3.81.086a.5.5 0 0 1 .67.225A5 5 0 0 1 11 13H5v1.466a.25.25 0 0 1-.41.192l-2.36-1.966a.25.25 0 0 1 0-.384l2.36-1.966a.25.25 0 0 1 .41.192V12h6a4 4 0 0 0 3.585-5.777.5.5 0 0 1 .225-.67Z"/>
                    </svg>
                    <!-- Numero Retweets -->
                    {{ tweet.retweet_count }}
                  </div>
                  <div id="stats-tweet" class="col-3">
                    <!-- Icono Me gustas -->
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                      <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                    </svg>
                    <!-- Numero Me gustas -->
                    {{ tweet.like_count }}
                  </div>
                  <div id="stats-tweet" class="col-4">
                    <!-- Numero Fecha de publicacion -->
                    {{ tweet.created_at }}
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-6" id="buttons-card">
                    <!-- Enlace al tweet -->
                    <a class="btn btn-primary" id="buttons-card" :href="tweet.url" role="button">Link</a>
                  </div>
                  <div class="col-lg-6">
                    <button id="saveTweetButton" class="btn btn-primary" type="button" @click="saveTweet(tweet.id)">Guardar tweet</button>
                  </div>
                </div>
              </div>  
            </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
import wordcloud from 'vue-wordcloud'
import VueApexCharts from 'vue-apexcharts'
import VueTableDynamic from 'vue-table-dynamic'


export default {
  name: 'TweetAnalysis',
  created: function() {
    this.$store.dispatch('viewMe');
    return this.$store.dispatch('viewTweetSearch');
  },
  computed: {
    ...mapGetters({tweetSearch: 'stateTweetSearch' }),
    ...mapGetters({user: 'stateUser' }),
  },
  // Metodo para guardar tweet en el perfil
  methods: {
    ...mapActions(['saveTweet']),
    getLastSearch() {
      var search = Object.values(this.user.searchs).pop()
      return search.title
    },
    saveTweetUser(idTweet) {
      try {
        this.saveTweet(idTweet);
        $('#modalTweetSave').modal()
      } catch (error) {
        console.error(error);
      }
    },
  },
  

  // Graficos
  name: 'graphs',
  components: {
    wordcloud, apexcharts: VueApexCharts, VueTableDynamic 
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    },
    onSelect (isChecked, index, data) {
      console.log('onSelect: ', isChecked, index, data)
      console.log('Checked Data:', this.$refs.table.getCheckedRowDatas(true))
    },
    onSelectionChange (checkedDatas, checkedIndexs, checkedNum) {
      console.log('onSelectionChange: ', checkedDatas, checkedIndexs, checkedNum)
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
        sort: [0,1],
        stripe: true,
        pagination: true,
        pageSize: 10,
        pageSizes: [5, 10, 20, 50],
        showCheck: true,
        columnWidth: [{column: 0, width: 80},{column: 1, width: 130}, {column: 2, width: 2000},{column: 3, width: 110}, {column: 4, width: 110},{column: 5, width: 110},{column: 6, width: 120},{column: 7, width: 300}],
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
            counter.push(value)
          }
          tweetObject = {name: key, value: value}
          counter.push(tweetObject)
      });
      this.defaultWords = counter
      this.loaded = true;

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
#buttons-card {
  text-align: center;
}
#graphs {
  margin: 20px;
}
#cards {
  margin: 20px;
}
#card-charts {
  margin: 20px;
}
</style>