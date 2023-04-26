<template>
  <div>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="$router.push('/signup')"></v-app-bar-nav-icon>
      <v-toolbar-title>Register as Customer</v-toolbar-title>
    </v-app-bar>
    <v-container>
      <v-card>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field v-model="email" :rules="emailRules" label="Email" required></v-text-field>
            <v-text-field v-model="username" :rules="usernameRules" label="Username" required></v-text-field>
            <v-text-field v-model="customerName" :rules="customernameRules" label="Customer Name" required></v-text-field>
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
  components: {
    Header,
  },
  data() {
    return {
      email: '',
      username: '',
      customerName: '',
      phone: '',
      password: '',
      confirmPassword: '',
      valid: false,
      emailRules: [
        (v) => !!v || 'Email is required',
        (v) => /.+@.+/.test(v) || 'Email must be valid',
      ],
      usernameRules: [(v) => !!v || 'Username is required'],
      customernameRules: [(v) => !!v || 'Customer name is required'],
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => v.length >= 6 || 'Password must be at least 6 characters',
      ],
      confirmPasswordRules: [
        (v) => !!v || 'Confirm Password is required',
        (v) => v === this.password || 'Password does not match',
      ],
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
      this.postUser({

        username: this.username,
        password: encryptPass,
        name: this.customerName,
        role: "3",
        phone: this.phone,
        email: this.email,

      })
        .then(() => {
          // Display success message using SweetAlert2
          //Swal.fire
          // Reset form fields
          this.email = '';
          this.username = '';
          this.customerName = '';
          this.password = '';
          this.confirmPassword = '';
          this.valid = false;

          this.$router.push({ path: "/" })
        })
    },
  },
};
</script>