<template>
  <header>
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <a class="navbar-brand" href="/">
          <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
          TFG
        </a>
        <!-- Para que salga el menu al hacer la pantalla mas pequeña -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarWeb" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarWeb">
          <!-- <ul v-if="isLoggedIn" class="navbar-nav"> -->
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <a class="nav-link" href="/">Home</a>
              </li>
              <ul class="navbar-nav mr-auto" id="options-navbar">
                <li class="nav-item active">
                  <a class="nav-link" href="/account">Account</a>
                </li>
                <li class="nav-item active">
                  <a class="nav-link" href="/searchhistory">Search History</a>
                </li>
                <li class="nav-item active">
                  <a class="nav-link" href="/tweetsaved">Tweets Saved</a>
                </li>
                <li class="nav-item active">
                  <a class="nav-link" @click="logout">Log Out</a>
                </li>
                <li class="nav-item active">
                <a class="nav-link" href="/useranalysis">User Analysis</a>
                </li>
                <li class="nav-item active">
                <a class="nav-link" href="/tweetanalysis">Tweet Analysis</a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Settings
                  </a>
                  <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="/account">Account</a>
                    <a class="dropdown-item" href="/myTweets">Tweets Saved</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" @click="logout">Log Out</a>
                  </div>
                </li>
              </ul>   
            </ul>
          <!-- </ul> -->
          <!-- DESCOMENTAR CUANDO SE SOLUCIONE EL PROBLEMA DE LA CREACION DE USUARIOS -->
          <!-- <ul v-else class="navbar-nav">
              <button class="btn btn-sm btn-outline-dark float-right" type="button" @click="$router.push('/login')">Log in</button>
              <button class="btn btn-dark float-right" type="button" @click="$router.push('/signup')">Sign up</button>
          </ul> -->
        </div>
    </nav>
    
  </header>
  
</template>

<script>

export default {
  name: 'NavBar',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#options-navbar {
  position: absolute;
  right: 10px;
}


.navbar-brand {
    padding-top: 0.3125rem;
    padding-bottom: 0.3125rem;
    margin-right: 1rem;
    margin-left: 1rem;
    font-size: 1.25rem;
    text-decoration: none;
    white-space: nowrap;
}
</style>