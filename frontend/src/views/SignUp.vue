<template>
  <!-- <section>
    <div class="container">
      Modal para muestra de errores en la validacion
      <div class="modal fade" id="modalSignUp" tabindex="-1" role="dialog" aria-labelledby="modalSignUp" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Error</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Username already exists. Please try again.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row align-items-center">
        <div class="col">
          Imagen pantalla
          <img src="../assets/signup.png" class="img-fluid" alt="Responsive image">
        </div>
        <div class="col-8">
          Formulario de registro
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-signup">Sign up and start working</label>
            </div>
            <div class="form-group row">
              <div class="col m-3">
               Nombre 
              <input type="text" name="first_name" placeholder="First Name" v-model="user.first_name" class="form-control" />
              </div>
              <div class="col m-3">
               Apellidos
              <input type="text" name="last_name" placeholder="Last Name" v-model="user.last_name" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              Nombre de usuario
              <input type="text" name="username" placeholder="Username" v-model="user.username" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
               Correo electronico 
              <input type="email" name="email" placeholder="Email" v-model="user.email" class="form-control" />
              </div>
              <div class="col m-3">
               Contraseña 
              <input type="password" name="password" placeholder="Password" v-model="user.password" class="form-control" />
              </div>
            </div>
            <div class="row"> 
              <div class="col-6"></div>
               Botones de confirmar registro o cancelar registro 
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
  </section> -->
    <section class="ftco-section">
		<div class="container">
      <!-- Modal para muestra de errores en la validacion  -->
      <div class="modal fade" id="modalSignUp" tabindex="-1" role="dialog" aria-labelledby="modalSignUp" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Error</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Username already exists. Please try again.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
			<div class="row justify-content-center">
				<div class="col-md-12 col-lg-10">
					<div class="wrap d-md-flex">
            <!-- Imagen pantalla  -->
            <div src="../assets/signup.png" class="img" style="background-image"> </div>
						<div class="login-wrap p-4 p-md-5">
			      	<div class="d-flex">
			      		<div class="w-100">
			      			<h3 class="mb-4">Sign Up</h3>
			      		</div>	
			      	</div>
					  <form @submit.prevent="submit">
            <!-- Formulario de inicio de sesion  -->
                <div class="form-group mb-3">
                  <!-- Nombre  -->
			      			<label class="label" for="first_name">First Name</label>
			      			<input type="text" class="form-control" v-model="user.first_name" placeholder="First Name" required>
			      		</div>
                <div class="form-group mb-3">
                  <!-- Apellidos  -->
			      			<label class="label" for="last_name">Last Name</label>
			      			<input type="text" class="form-control" v-model="user.last_name" placeholder="Last Name" required>
			      		</div>
			      		<div class="form-group mb-3">
                  <!-- Nombre de usuario  -->
			      			<label class="label" for="username">Username</label>
			      			<input type="text" class="form-control" v-model="user.username" placeholder="Username" required>
			      		</div>
                <div class="form-group mb-3">
                  <!-- Correo electronico  -->
			      			<label class="label" for="email">Email</label>
			      			<input type="text" class="form-control" v-model="user.email" placeholder="Email" required>
			      		</div>
		            <div class="form-group mb-3">
                  <!-- Contraseña -->
		            	<label class="label" for="password">Password</label>
		              <input type="password" class="form-control" v-model="user.password" placeholder="Password" required>
		            </div>
                <!-- Boton de confirmar inicio de sesion -->
		            <div class="form-group">
		            	<button type="submit" class="form-control btn btn-primary rounded submit px-3">Sign Up</button>
		            </div>
		          </form>
		          <p class="text-center">Do you already have an account? <a href="/login">Log In</a></p>
		        </div>
		      </div>
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
        $('#modalSignUp').modal()
        //window.alert("Username already exists. Please try again.");
        throw 'Username already exists. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
/* .container{
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
} */
  @import '../assets/styles/style.css';
</style>