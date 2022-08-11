<template>
  <section>
    <div class="container">
      <!-- <div v-if="isLoggedIn" id="logout"> -->

        <!-- <p id="titulo">Proyecto de TFG de Sergio Martín Hernández</p>
        <div id="search-bar" class="input-group mb-3">
          <select id="search-filter" class="selectpicker">
            <option>Tweet</option>
            <option>User</option>
          </select>
          <input id="search-input" type="text" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="basic-addon1">
          <button id="search-button" type="button" class="btn btn-primary" @click="SaveSearch()">
            <i class="fas fa-search"></i>
          </button>
        </div> 


      </div> 
      <div v-else>--->
        <div class="row align-items-center">
          <div class="col-6">
            <img src="https://w7.pngwing.com/pngs/574/920/png-transparent-icon-twitter-emblem-logo-famous.png" class="img-fluid">
          </div>
          <div class="col">
            <div class="row">
              <!-- <div class="col"><button type="button" class="btn btn-outline-dark btn-lg btn-block" @click="$router.push('/login')">Log in</button></div> -->
              <button id="login-button" type="button" class="btn btn-outline-dark btn-lg btn-block" @click="$router.push('/login')">Log in</button>
            </div>
            <div class="row">
              <!-- <div class="col"><button type="button" class="btn btn-lg btn-dark btn-block" @click="$router.push('/signup')">Sign up</button></div> -->
              <button id="signup-button" type="button" class="btn btn-lg btn-dark btn-block" @click="$router.push('/signup')">Sign up</button>
            </div>
          </div>
        </div>
      <!-- </div> -->
    </div>
  </section>
</template>


<script>

export default {
  name: 'Home',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    SaveSearch: function() {
      //const searchInput = document.getElementById("search-input");
      //const inputValue = searchInput.value;
      const searchvalue = document.getElementById("search-filter").value;
      if(searchvalue=="Tweet") {
        //document.getElementById("view").innerHTML =  searchvalue;
        // HACER LLAMADA A LA FUNCION BUSCAR TWEET
      }
      else {
        //document.getElementById("view").innerHTML =  searchvalue;
        // HACER LLAMADA A LA FUNCION BUSCAR USER
      }

      //this.$router.push('/analysis')
    }
  }
}

// const searchButton = document.getElementById('search-button');
// const searchInput = document.getElementById('search-input');
// searchButton.addEventListener('click', () => {
//   const inputValue = searchInput.value;
//   console.log(inputValue);
// });
</script>

<style scoped>

.container {
  background-color: aliceblue;
  margin-top: 7%;
  padding: 5em;
}

#titulo {
  text-align: center;
  font-size: x-large;
  font-family: revert;
  font-weight: bold;
  padding-bottom: 20px;
}
#search-bar {
  font-family: Arial, Helvetica, sans-serif;
}

#search-button {
  font-size: large;
}

#search-filter {
  background: lavender;
}

#login-button {
  margin: 20px;
}

#signup-button {
  margin: 20px;
}
</style>
