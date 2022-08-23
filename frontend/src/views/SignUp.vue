<template>
  <section>
    <div class="container">
      <div class="row align-items-center">
        <div class="col">
          <!-- Imagen pantalla -->
          <img src="../assets/signup.png" class="img-fluid" alt="Responsive image">
        </div>
        <div class="col-8">
          <!-- Formulario de registro -->
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-signup">Sign up and start working</label>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <!-- Nombre -->
              <input type="text" name="first_name" placeholder="First Name" v-model="user.first_name" class="form-control" />
              </div>
              <div class="col m-3">
              <!-- Apellidos -->
              <input type="text" name="last_name" placeholder="Last Name" v-model="user.last_name" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <!-- Nombre de usuario -->
              <input type="text" name="username" placeholder="Username" v-model="user.username" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <!-- Correo electronico -->
              <input type="email" name="email" placeholder="Email" v-model="user.email" class="form-control" />
              </div>
              <div class="col m-3">
              <!-- Contraseña -->
              <input type="password" name="password" placeholder="Password" v-model="user.password" class="form-control" />
              </div>
            </div>
            <div class="row"> 
              <div class="col-6"></div>
              <!-- Botones de confirmar registro o cancelar registro -->
              <div id="button-submit" class="col"> <button type="submit" class="btn btn-primary">Sign up</button> </div> 
              <div id="button-cancel" class="col"> <button type="button" class="btn btn-dark" @click="$router.push('/')">Cancel</button> </div>  
            </div> 
            <div class="row">
              <div class="col-6"></div>
              <div id="a-account" class="col-6"><a>Do you already have an account? </a><span><a href="/login">Log In</a></span></div>
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
  name: 'signUp',
  data() {
    return {
      user: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password: ''
      }
    };
  },
  // Metodo de creacion de cuenta de usuario y llamada al registro en la base de datos
  methods: {
    ...mapActions(['signUp']),
    async submit() {
      try {
        await this.signUp(this.user);
        this.$router.push('/');
      } catch (error) {
        window.alert("Username already exists. Please try again.");
        throw 'Username already exists. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
.container{
  margin-top: 3%;
  padding: 5em;
  background-color: aliceblue;
}
#label-signup {
  margin-left: 16px;
  font-size: x-large;
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