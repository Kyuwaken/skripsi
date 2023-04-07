<template>
    <div>
      <v-container>
        <v-card>
          <v-card-title>Register as Customer</v-card-title>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Email"
                required
              ></v-text-field>
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                label="Username"
                required
              ></v-text-field>
              <v-text-field
                  v-model="nik"
                  :rules="nikRules"
                  label="Nomor Induk Kependudukan (NIK)"
                  required
              ></v-text-field>
              <v-text-field
                  v-model="phone"
                  :rules="phoneRules"
                  label="Phone Number"
                  required
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                label="Password"
                type="password"
                required
              ></v-text-field>
              <v-text-field
                v-model="confirmPassword"
                :rules="confirmPasswordRules"
                label="Confirm Password"
                type="password"
                required
              ></v-text-field>
              <v-btn @click="submitForm" :disabled="!valid">Submit</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-container>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        username: '',
        password: '',
        confirmPassword: '',
        nik:'',
        valid: false,
        emailRules: [
          (v) => !!v || 'Email is required',
          (v) => /.+@.+/.test(v) || 'Email must be valid',
        ],
        usernameRules: [
            (v) => !!v || 'Username is required',
            (v) => v.length >= 6 || 'Username must be at least 6 characters'
        ],
        nikRules: [
            (v) => !!v || 'NIK is required',
            (v) => v.length == 16 || 'NIK must be 16 characters',
        ],
        passwordRules: [
          (v) => !!v || 'Password is required',
          (v) => v.length >= 6 || 'Password must be at least 6 characters',
        ],
        confirmPasswordRules: [
          (v) => !!v || 'Confirm Password is required',
          (v) => v === this.password || 'Password does not match',
        ],
      };
    },
    methods: {
      submitForm() {
        // Perform form validation before submission
        if (!this.$refs.form.validate()) {
          return;
        }
  
        // Perform additional validation if necessary
  
        // Submit the form to the server
        this.$axios
          .post('/api/customer/register', {
            email: this.email,
            username: this.username,
            password: this.password,
            nik: this.nik,
            role: "Customer"
          })
          .then(() => {
            // Display success message using SweetAlert2
            Swal.fire({
              title: 'Success',
              text: 'Registration successful!',
              icon: 'success',
            });
  
            // Reset form fields
            this.email = '';
            this.username = '';
            this.password = '';
            this.confirmPassword = '';
            this.valid = false;
          })
          .catch(() => {
            // Display error message using SweetAlert2
            Swal.fire({
              title: 'Error',
              text: 'Registration failed. Please try again later.',
              icon: 'error',
            });
          });
      },
    },
  };
  </script>