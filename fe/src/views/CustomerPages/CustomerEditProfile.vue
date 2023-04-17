<template>
    <v-card>
      <v-card-title>
        <v-btn icon @click="$router.push('/customerprofile')">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <span class="headline">Edit Profile</span>
      </v-card-title>
  
      <v-card-text>
        <v-form ref="form">
          <v-text-field
            v-model="profile.name"
            label="Name"
            :readonly="!editMode"
            :rules="[v => !!v || 'Name is required']"
          ></v-text-field>
  
          <v-text-field
            v-model="profile.phoneNumber"
            label="Phone Number"
            :readonly="!editMode"
            pattern="[0-9]*"
            maxlength="10"
            :rules="[v => !!v || 'Phone number is required', v => /^\d{10}$/.test(v) || 'Phone number must be 10 digits']"
          ></v-text-field>

          <v-text-field
            v-model="profile.email"
            label="Email"
            :readonly="!editMode"
            type="email"
            :rules="[v => !!v || 'Email is required', v => /.+@.+\..+/.test(v) || 'Email must be valid']"
          ></v-text-field>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" v-if="editMode" @click="submitProfile">Submit</v-btn>
            <v-btn color="error" v-if="editMode" @click="resetProfile">Cancel</v-btn>
            <v-btn color="primary" v-else @click="editMode = $refs.form.validate()">Edit Profile</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </template>

<script>
export default {
  data() {
    return {
      profile: {
        name: 'test1',
        phoneNumber: 'tes2',
        email: 'tes3',
      },
      editMode: false,
    };
  },

  methods: {
    openPhotoDialog() {
      // Show photo upload dialog
    },

    submitProfile() {
      Swal.fire({
        title: 'Are you sure?',
        text: 'You are about to submit your changes.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, submit',
        cancelButtonText: 'Cancel',
      }).then((result) => {
        if (result.isConfirmed) {
          axios.put('/api/profile', this.profile)
            .then(() => {
              Swal.fire({
                title: 'Success!',
                text: 'Your profile has been updated.',
                icon: 'success',
              });
              this.editMode = false;
            })
            .catch(() => {
              Swal.fire({
                title: 'Error',
                text: 'An error occurred while updating your profile.',
                icon: 'error',
              });
            });
        }
      });
    },

    resetProfile() {
      // Reset profile data
    },
  },
};
</script>
