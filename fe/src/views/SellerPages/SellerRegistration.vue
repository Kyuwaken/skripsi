<template>
  <div>
    <v-btn icon class="back-btn" @click="$router.push('/signup')">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>
    <v-container>
      <v-card>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field v-model="email" :rules="emailRules" label="Email" required></v-text-field>
            <v-text-field v-model="username" :rules="usernameRules" label="Username" required></v-text-field>
            <v-text-field v-model="storeName" :rules="storenameRules" label="Store Name" required></v-text-field>
            <v-text-field v-model="phone" :rules="phoneRules" label="Phone Number" required></v-text-field>
            <v-text-field v-model="password" :rules="passwordRules" label="Password" type="password"
              required></v-text-field>
            <v-text-field v-model="confirmPassword" :rules="confirmPasswordRules" label="Confirm Password" type="password"
              required></v-text-field>
            <v-btn @click="submitForm" :disabled="!valid">Submit</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>
  
<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import crypto from '@/plugins/crypto'
import Swal from "sweetalert2";
import Header from "../../components/Header.vue";
export default {
  mixins: [crypto],
  components:{
    Header
  },
  data() {
    return {
      email: '',
      username: '',
      storeName: '',
      phone: '',
      country: '',
      password: '',
      confirmPassword: '',
      valid: false,
      emailRules: [
        (v) => !!v || 'Email is required',
        (v) => /.+@.+/.test(v) || 'Email must be valid',
      ],
      usernameRules: [(v) => !!v || 'Username is required'],
      storenameRules: [(v) => !!v || 'Store name is required'],
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => v.length >= 6 || 'Password must be at least 6 characters',
      ],
      confirmPasswordRules: [
        (v) => !!v || 'Confirm Password is required',
        (v) => v === this.password || 'Password does not match',
      ],
      countryRules: [(v) => !!v || 'Country is required'],
      phoneRules: [(v) => !!v || 'Phone Number is required'],
    };
  },
  methods: {
    ...mapActions("register", ["postUser"]),
    submitForm() {
      // Perform form validation before submission
      if (!this.$refs.form.validate()) {
        return;
      }
      // Submit the form to the server
      var encryptPass = this.encryptData(this.password)
      console.log(encryptPass)
      this.postUser({

        username: this.username,
        password: encryptPass,
        name: this.storeName,
        role: "2",
        phone: this.phone,
        email: this.email,

      })
        .then(() => {
          // Display success message using SweetAlert2
          //Swal.fire
          // Reset form fields
          this.email = '';
          this.username = '';
          this.storeName = '';
          this.password = '';
          this.confirmPassword = '';
          this.valid = false;

          this.$router.push({ path: "/" })
        })
    },
  },
};
</script>