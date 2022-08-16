<template>
  <section>
    <div class="container">
      <div class="row align-items-center">
        <div class="col">
          <!-- IMAGEN -->
          <img src="https://naldzgraphics.net/wp-content/uploads/2017/02/22-graphic-UI-illustration.jpg" class="img-fluid" alt="Responsive image">
        </div>
        <div class="col-6">
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-welcome">Welcome</label>
            </div>
            <div class="row">
              <label id="label-login">Log in with your user and password</label>
            </div>
            <div class="form-group row">
              <!-- <label for="username" class="form-label">Username:</label> -->
              <div class="col m-3"><input type="text" name="username" placeholder="Username" v-model="form.username" class="form-control" /></div>
            </div>
            <div class="form-group row">
              <!-- <label for="password" class="form-label">Password:</label> -->
              <div class="col m-3"><input type="password" name="password" placeholder="Password" v-model="form.password" class="form-control" /></div>
            </div>
            <div class="row"> 
              <div class="col-6"></div>
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