<template>
  <section>
    <div class="container">
      <div class="row align-items-center">
        <div class="col">
          <!-- Imagen pantalla -->
          <img src="../assets/login.png" class="img-fluid" alt="Responsive image">
        </div>
        <div class="col-6">
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-welcome">Welcome</label>
            </div>
            <div class="row">
              <label id="label-login">Log in with your user and password</label>
            </div>
            <!-- Formulario de inicio de sesion -->
            <div class="form-group row">
              <!-- Nombre de usuario -->
              <div class="col m-3"><input type="text" name="username" placeholder="Username" v-model="form.username" class="form-control" /></div>
            </div>
            <div class="form-group row">
              <!-- Contraseña -->
              <div class="col m-3"><input type="password" name="password" placeholder="Password" v-model="form.password" class="form-control" /></div>
            </div>
            <div class="row"> 
              <div class="col-6"></div>
              <!-- Botones de confirmar inicio de sesio o cancelar -->
              <div id="button-submit" class="col"> <button type="submit" class="btn btn-primary">Log in</button> </div> 
              <div id="button-cancel" class="col"> <button type="button" class="btn btn-dark" @click="$router.push('/')">Cancel</button> </div>  
            </div> 
            <div class="row">
              <div class="col-4"></div>
              <div id="a-account" class="col"><a>You do not have an account? </a><span><a href="/signup">Sign up</a></span></div>
            </div> 
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password:'',
      }
    };
  },
  // Metodo de inicio de sesion con comprobacion de contraseña
  methods: {
    ...mapActions(['logIn']),
    async submit() {
        try {
            const User = new FormData();
            User.append('username', this.form.username);
            User.append('password', this.form.password);
            await this.logIn(User);
            this.$router.push('/');
        } catch (error) {
            window.alert("There was a problem logging in. Check email and password.");
            throw 'There was a problem logging in. Check email and password.';
        }  
    }
  }
}
</script>

<style scoped>
.container{
  margin-top: 3%;
  padding: 5em;
  background-color: aliceblue;
}

#label-welcome {
  margin-left: 16px;
  font-size: xx-large;
  font-weight: bold;
  font-family: unset;
}
#label-login {
  margin-left: 16px;
  font-size: large;
  font-family: unset;
}
 #button-submit {
  text-align: right;
}
#button-cancel {
  text-align: right;
  margin-right: 16px;
} 
#a-account {
  margin-top: 17px;
}

</style>