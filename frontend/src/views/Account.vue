<template>
  <section>
    <div class="container">
      <div class="row align-items-center">
        <div class="col">
            <img class="rounded-circle img-fluid" src="https://naldzgraphics.net/wp-content/uploads/2017/02/22-graphic-UI-illustration.jpg" alt="Responsive image">
            <label class="form-label" for="newProfileImage">Change profile image</label>
            <input type="file" class="form-control" id="newProfileImage" />
        </div>
        <div class="col-8">
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-signup">Profile Settigns</label>
            </div>
            
            <div class="form-group row">
              <div class="col m-3">
              <label for="first_name" class="form-label">First Name:</label>
              <input type="text" name="first_name" placeholder="First Name" :value="user.first_name" readonly class="form-control" />
              </div>
              <div class="col m-3">
              <label for="last_name" class="form-label">Last Name:</label>
              <input type="text" name="last_name" placeholder="Last Name" :value="user.last_name" readonly class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              
              <div class="col m-3">
              <label for="username" class="form-label">Username:</label>
              <input type="text" name="username" placeholder="Username" :value="user.username" readonly class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <label for="email" class="form-label">Email:</label>
              <input type="email" name="email" placeholder="Email" :value="user.email" readonly class="form-control" />
              </div>
            </div>
            <div class="row">
                <label id="label-changepassword">Change password</label>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <label for="password" class="form-label">Old password:</label>
              <input type="password" name="password" placeholder="Password" v-model="user.password" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <label for="newpassword" class="form-label">New password:</label>
              <input type="password" name="newpassword" placeholder="New password" class="form-control" />
              </div>
              <div class="col m-3">
              <label for="newpassword2" class="form-label">Confirm new password:</label>
              <input type="password" name="newpassword2" placeholder="Confirm new password" class="form-control" />
              </div>
            </div>
            <div class="row"> 
              <div class="col-6">
                 <button class="btn btn-danger" data-toggle="modal" data-target="#deleteAccountModal">Delete account</button> 
                 <div class="modal fade" id="deleteAccountModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="ModalLabel">Delete account</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        Are you sure to delete the account?
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="deleteAccount()">Confirm</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div id="button-submit" class="col"> <button type="submit" class="btn btn-primary">Confirm changes</button> </div> 
              <div id="button-cancel" class="col"> <button type="button" class="btn btn-dark" @click="$router.push('/')">Cancel</button> </div>  
            </div> 
          </form>   
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Account',
  created: function() {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },
}
</script>

<style>
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
  #label-changepassword {
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