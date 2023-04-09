<template>
    <v-container>
      <v-card class="mx-auto mt-8" max-width="400">
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field v-model="username" :rules="usernameRules" label="Username"></v-text-field>
            <v-text-field v-model="password" :rules="passwordRules" label="Password" type="password"></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions class="d-flex justify-center">
          <v-btn color="primary" :disabled="!valid" @click="submit">Login</v-btn>
        </v-card-actions>
      </v-card>
      <div class="text-center mt-4">
        <span>Don't have an account? </span>
        <v-btn text @click="signup">Sign up here</v-btn>
      </div>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
  export default {
    computed:{
      ...mapState("login",["loginData"])
    },
    data() {
      return {
        username: '',
        password: '',
        valid: false,
        usernameRules: [
          v => !!v || 'Username is required',
          v => v && v.length >= 3 || 'Username must be at least 3 characters'
        ],
        passwordRules: [
          v => !!v || 'Password is required',
          v => v && v.length >= 8 || 'Password must be at least 8 characters'
        ]
      }
    },
    methods: {
      ...mapActions("login", ["postLogin"]),
      async submit() {
        console.log(this.valid)
        if (this.valid) {
          this.postLogin({username:this.username,password:this.password})
          // try {
            //   const response = await axios.post('login/', {
              //     username: this.username,
              //     password: this.password
              //   });
              //   console.log(response)
              //   // Handle login success here
              //   // Swal.fire({
                //   //   title: 'Success!',
                //   //   text: 'Logged in successfully',
                //   //   icon: 'success',
                //   //   timer: 2000,
                //   //   showConfirmButton: false
                //   // });
                // } catch (error) {
          //   console.log("failed")
          //   // Handle login error here
          //   // Swal.fire({
          //   //   title: 'Error!',
          //   //   text: 'Invalid username or password',
          //   //   icon: 'error',
          //   //   timer: 2000,
          //   //   showConfirmButton: false
          //   // });
          // }
        }
      },
      signup() {
        // Redirect to sign up page
        alert('Redirect to sign up page');
      }
    },
    watch: {
      username: function(val) {
        this.valid = this.$refs.form.validate();
      },
      password: function(val) {
        this.valid = this.$refs.form.validate();
      }
    }
  }
  </script>
  