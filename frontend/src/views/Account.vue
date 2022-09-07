<template>
  <section class="section about-section gray-bg">
    <div class="container">
      <div class="row align-items-center">
        <div class="col">
          <!-- Foto de perfil del usuario y metodo para poder cambiarla -->
          <img class="rounded-circle img-fluid" :src="user.image" alt="Responsive image">
          <label class="form-label" for="newProfileImage">Change profile image</label>
          <input type="text" name="profileImage" v-model="formUserUpdate.image" placeholder="URL new profile image" class="form-control" />
        </div>
        <div class="col-8">
          <form @submit.prevent="submit">
            <div class="row">
              <label id="label-signup">Profile Settings</label>
            </div>
            <!-- Datos de la cuenta del usuario -->
            <div class="form-group row">
              <div class="col m-3">
              <!-- Nombre del usuario -->
              <label for="first_name" class="form-label">First Name:</label>
              <input type="text" name="first_name" placeholder="First Name" :value="user.first_name" readonly class="form-control" />
              </div>
              <div class="col m-3">
              <!-- Apellidos del usuario -->
              <label for="last_name" class="form-label">Last Name:</label>
              <input type="text" name="last_name" placeholder="Last Name" :value="user.last_name" readonly class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <!-- Nombre de usuario -->
              <label for="username" class="form-label">Username:</label>
              <input type="text" name="username" placeholder="Username" :value="user.username" readonly class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <!-- Correo electronico -->
              <label for="email" class="form-label">Email:</label>
              <input type="email" name="email" placeholder="Email" :value="user.email" readonly class="form-control" />
              </div>
            </div>
            <!-- Metodo para cambiar la contraseña del usuario -->
            <div class="row">
                <label id="label-changepassword">Change password</label>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <label for="password" class="form-label">Old password:</label>
              <input type="password" name="password" placeholder="Password" v-model="formUserUpdate.oldpassword" class="form-control" />
              </div>
            </div>
            <div class="form-group row">
              <div class="col m-3">
              <label for="newpassword" class="form-label">New password:</label>
              <input id="newpassword" type="password" name="newpassword" v-model="formUserUpdate.password" placeholder="New password" class="form-control" />
              </div>
              <div class="col m-3">
              <label for="newpassword2" class="form-label">Confirm new password:</label>
              <input id="newpassword2" type="password" name="newpassword2" placeholder="Confirm new password" class="form-control" />
              </div>
            </div>
            <div class="row"> 
              <!-- Boton de borrar cuenta del usuario con modal para la confirmacion -->
              <div class="col-6">
                <button class="btn btn-danger" @click="showDeleteAccount()">Delete account</button> 
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
                        <button type="button" class="btn btn-danger" data-dismiss="modal" @click="deleteAccount()">Confirm</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Boton para confirmar los cambios en el perfil del usuario -->
              <div id="button-submit" class="col"> <button type="button" class="btn btn-primary" @click="updateAccount()">Confirm changes</button> </div> 
              <!-- Boton para cancelar los cambios y volver a la pagina principal -->
              <div id="button-cancel" class="col"> <button type="button" class="btn btn-dark" @click="$router.push('/search')">Cancel</button> </div>  
            </div> 
          </form>   
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
/**
 * @vue-data {Form} formUserUpdate - Formulario de actualización de usuario
 * @vue-computed {User} user
 * @vue-event showDeleteAccount - Muestra el modal de confirmación de eliminación de usuario
 * @vue-event deleteAccount - Borra un usuario del sistema
 * @vue-event updateAccount - Actualiza los datos de un usuario del sistema
 */
export default {
  name: 'Account',
  data() {
    return {
      formUserUpdate: {
        image: '',
        oldpassword: '',
        password: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['deleteUser', 'updateUser']),
    async showDeleteAccount() {
      $('#deleteAccountModal').modal()
    },
    // Metodo para borrar cuenta del usuario
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    },
    // Metodo para realizar los cambios en la cuenta del usuario
    async updateAccount() {
        const newpassword = document.getElementById("newpassword").value;
        const newpassword2 = document.getElementById("newpassword2").value;
        if(newpassword == newpassword2) {
             try {
              let updatedUser = {
                image: this.formUserUpdate.image,
                password: this.formUserUpdate.password,
                oldpassword: this.formUserUpdate.oldpassword,
              };
              console.log(updatedUser)
              await this.updateUser(updatedUser);
              this.$router.push('/search');
            } catch (error) {
              console.log(error);
            }
        }
    }
  },
}
</script>

<style scoped>
  .section {
      padding: 100px 0;
      position: relative;
  }
  .gray-bg {
      background-color: #f5f5ff;
      height: 100%;
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