<template>
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
            <div class="img" id="image-signup" style="background-image"></div>
						<div class="signup-wrap p-4 p-md-5">
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
/**
 * @vue-data {Form} user - Formulario de registro de un usuario
 * @vue-event submit - Envío del formulario de registro al backend
 * @vue-event validateEmail - Comprobación de correcto formato de correo eléctronico
 */
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
        if (!this.validateEmail(this.user.email)) {
          $("#modalSignUp .modal-body").text('Email entered in an invalid format, please try again');
          $('#modalSignUp').modal()
        } else {
          await this.signUp(this.user);
          this.$router.push('/search');
        }       
      } catch (error) {
        console.log(error)
        $('#modalSignUp').modal()
        throw 'Username already exists. Please try again.';
      }
    },
    validateEmail(email) 
    {
        var re = /\S+@\S+\.\S+/;
        var valid = re.test(email);
        return valid
    }
  }
};
</script>

<style scoped>
#image-signup {
  background: url(../assets/signup.png) no-repeat top center;
}
 section {
    display: block; 
    background-color: #f5f5ff;}
  
  h3 {
    margin-top: 0;
    margin-bottom: 0.5rem; }
  
  p {
    margin-top: 0;
    margin-bottom: 1rem; }
  
  a {
    color: #007bff;
    text-decoration: none;
    background-color: transparent; }
    a:hover {
      color: #0056b3;
      text-decoration: underline; }
  
  label {
    display: inline-block;
    margin-bottom: 0.5rem; }
  
  button {
    border-radius: 0; }
  
  button:focus {
    outline: 1px dotted;
    outline: 5px auto -webkit-focus-ring-color; }
  
  input,
  button {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit; }
  
  button,
  input {
    overflow: visible; }
  
  button {
    text-transform: none; }
  
  button:not(:disabled),
  [type="button"]:not(:disabled),
  [type="reset"]:not(:disabled),
  [type="submit"]:not(:disabled) {
    cursor: pointer; }
  
  button::-moz-focus-inner,
  [type="button"]::-moz-focus-inner,
  [type="submit"]::-moz-focus-inner {
    padding: 0;
    border-style: none; }
  
  ::-webkit-file-upload-button {
    font: inherit;
  }
  
  h3 {
    margin-bottom: 0.5rem;
    font-weight: 500;
    line-height: 1.2; }
  
  h3 {
    font-size: 1.75rem; }
  
  .container {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto; }
    @media (min-width: 576px) {
      .container {
        max-width: 540px; } }
    @media (min-width: 768px) {
      .container {
        max-width: 720px; } }
    @media (min-width: 992px) {
      .container {
        max-width: 960px; } }
    @media (min-width: 1200px) {
      .container {
        max-width: 1140px; } }
  
  .row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px; }
  
  .col-md-12, .col-lg-10 {
    position: relative;
    width: 100%;
    padding-right: 15px;
    padding-left: 15px; }
  
  @media (min-width: 768px) {
    .col-md-12 {
      -webkit-box-flex: 0;
      -ms-flex: 0 0 100%;
      flex: 0 0 100%;
      max-width: 100%; } }
  
  @media (min-width: 992px) {
    .col-lg-10 {
      -webkit-box-flex: 0;
      -ms-flex: 0 0 83.33333%;
      flex: 0 0 83.33333%;
      max-width: 83.33333%; } }
  
  .form-control {
    display: block;
    width: 100%;
    height: calc(1.5em + 0.75rem + 2px);
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    -webkit-transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
    @media (prefers-reduced-motion: reduce) {
      .form-control {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
    .form-control::-ms-expand {
      background-color: transparent;
      border: 0; }
    .form-control:focus {
      color: #495057;
      background-color: #fff;
      border-color: #80bdff;
      outline: 0;
      -webkit-box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
      box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); }
    .form-control::-webkit-input-placeholder {
      color: #6c757d;
      opacity: 1; }
    .form-control:-ms-input-placeholder {
      color: #6c757d;
      opacity: 1; }
    .form-control::-ms-input-placeholder {
      color: #6c757d;
      opacity: 1; }
    .form-control:disabled {
      background-color: #e9ecef;
      opacity: 1; }
  
  .form-group {
    margin-bottom: 1rem; }
  
  .was-validated .custom-control-input:valid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-valid:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #28a745; }
  
  .was-validated .custom-control-input:invalid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-invalid:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #dc3545; }
  
  .btn {
    display: inline-block;
    font-weight: 400;
    color: #212529;
    text-align: center;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: transparent;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.25rem;
    -webkit-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out;
    -o-transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, -webkit-box-shadow 0.15s ease-in-out; }
    @media (prefers-reduced-motion: reduce) {
      .btn {
        -webkit-transition: none;
        -o-transition: none;
        transition: none; } }
    .btn:hover {
      color: #212529;
      text-decoration: none; }
    .btn:focus {
      outline: 0;
      -webkit-box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
      box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); }
    .btn:disabled {
      opacity: 0.65; }
  
  .rounded {
    border-radius: 0.25rem !important; }
  
  .d-flex {
    display: -webkit-box !important;
    display: -ms-flexbox !important;
    display: flex !important; }
  
  @media (min-width: 768px) {
    .d-md-flex {
      display: -webkit-box !important;
      display: -ms-flexbox !important;
      display: flex !important; } }
  
  .justify-content-center {
    -webkit-box-pack: center !important;
    -ms-flex-pack: center !important;
    justify-content: center !important; }
  
  @supports ((position: -webkit-sticky) or (position: sticky)) { }
  
  .w-100 {
    width: 100% !important; }
  
  .mb-3 {
    margin-bottom: 1rem !important; }
  
  .mb-4 {
    margin-bottom: 1.5rem !important; }
  
  .px-3 {
    padding-right: 1rem !important; }
  
  .px-3 {
    padding-left: 1rem !important; }
  
  .p-4 {
    padding: 1.5rem !important; }
  
  @media (min-width: 768px) {
    .p-md-5 {
      padding: 3rem !important; } }
  
  .text-center {
    text-align: center !important; }
  
  @media print {
    *,
    *::before,
    *::after {
      text-shadow: none !important;
      -webkit-box-shadow: none !important;
      box-shadow: none !important; }
    a:not(.btn) {
      text-decoration: underline; }
    p,
    h3 {
      orphans: 3;
      widows: 3; }
    h3 {
      page-break-after: avoid; }
    @page {
      size: a3; }
    body {
      min-width: 992px !important; }
    .container {
      min-width: 992px !important; } }
  
  body {
    font-family: "Lato", Arial, sans-serif;
    font-size: 16px;
    line-height: 1.8;
    font-weight: normal;
    background: #f8f9fd;
     }
  
  a {
    -webkit-transition: .3s all ease;
    -o-transition: .3s all ease;
    transition: .3s all ease;
    }
    a:hover, a:focus {
      text-decoration: none !important;
      outline: none !important;
      -webkit-box-shadow: none;
      box-shadow: none; }
  
  h3 {
    line-height: 1.5;
    font-weight: 400;
    font-family: "Lato", Arial, sans-serif;
    color: #000; }
  
  .ftco-section {
    padding: 5em 0; }
  
  .img {
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center; }
  
  .wrap {
    width: 100%;
    overflow: hidden;
    background: #fff;
    border-radius: 5px;
    -webkit-box-shadow: 0px 10px 34px -15px rgba(0, 0, 0, 0.24);
    -moz-box-shadow: 0px 10px 34px -15px rgba(0, 0, 0, 0.24);
    box-shadow: 0px 10px 34px -15px rgba(0, 0, 0, 0.24); }
  
  .img, .signup-wrap {
    width: 50%;
    background-color: lavender; }
    @media (max-width: 991.98px) {
      .img, .signup-wrap {
        width: 100%; } }
  
  @media (max-width: 767.98px) {
    .wrap .img {
      height: 250px; } }
  
  .signup-wrap {
    position: relative;
    background: #fff h3;
       }
  
  .form-group {
    position: relative; }
    .form-group .label {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #000;
      font-weight: 700; }
  
  .form-control {
    height: 48px;
    background: #fff;
    color: #000;
    font-size: 16px;
    border-radius: 5px;
    -webkit-box-shadow: none;
    box-shadow: none;
    border: 1px solid rgba(0, 0, 0, 0.1); }
    .form-control::-webkit-input-placeholder {
      /* Chrome/Opera/Safari */
      color: rgba(0, 0, 0, 0.2) !important; }
    .form-control::-moz-placeholder {
      /* Firefox 19+ */
      color: rgba(0, 0, 0, 0.2) !important; }
    .form-control:-ms-input-placeholder {
      /* IE 10+ */
      color: rgba(0, 0, 0, 0.2) !important; }
    .form-control:-moz-placeholder {
      /* Firefox 18- */
      color: rgba(0, 0, 0, 0.2) !important; }
    .form-control:focus, .form-control:active {
      outline: none !important;
      -webkit-box-shadow: none;
      box-shadow: none;
      border: 1px solid #e3b04b; }
  
  .btn {
    cursor: pointer;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
    font-size: 15px;
    padding: 10px 20px; }
    .btn:hover, .btn:active, .btn:focus {
      outline: none; }
    .btn.btn-primary {
      background: #007bff !important;
      border: 1px solid #007bff !important;
      color: #fff !important; }
      .btn.btn-primary:hover {
        border: 1px solid #007bff;
        background: transparent;
        color: #007bff; }
  
</style>