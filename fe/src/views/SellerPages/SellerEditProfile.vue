<template>
    <v-card>
      <v-card-title>
        <v-btn icon @click="$router.push('/sellerprofile')">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <span class="headline">Edit Profile</span>
      </v-card-title>
  
      <v-card-text>
        <v-form ref="form">
          <v-text-field
            v-model="profile.username"
            label="Username"
            :rules="[v => !!v || 'username is required']"
          ></v-text-field>

          <v-text-field
            v-model="profile.name"
            label="Name"
            :rules="[v => !!v || 'Name is required']"
          ></v-text-field>
  
          <v-text-field
            v-model="profile.phone"
            label="Phone Number"
            pattern="[0-9]*"
            maxlength="15"
            :rules="[v => !!v || 'Phone number is required', v => /^\d{10}$/.test(v) || 'Phone number must be 10 digits']"
          ></v-text-field>
  
          <v-text-field
            v-model="profile.email"
            label="Email"
            type="email"
            :rules="[v => !!v || 'Email is required', v => /.+@.+\..+/.test(v) || 'Email must be valid']"
          ></v-text-field>
  
          <!-- <v-text-field
            v-model="profile.country"
            label="Country"
            :readonly="!editMode"
            :rules="[v => !!v || 'Country is required']"
          ></v-text-field> -->

          <v-select v-model="profile.country" :items=countries item-text="name" item-title="name" item-value="id"
                label="Country" return-object :rules="[v => !!v || 'Country is required']" required></v-select>
  
          <v-textarea
            v-model="profile.description"
            label="Description"
          ></v-textarea>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="submitProfile">Submit</v-btn>
            <v-btn color="error" @click="resetProfile">Cancel</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </template>

<script>
import { mapActions, mapState } from 'vuex';
import Swal from 'sweetalert2';
export default {
  computed:{
    ...mapState("country",['countries']),
    ...mapState("profile", ["profileData"]),
  },
  data() {
    return {
      profile: {
        name: '',
        phone: '',
        email: '', 
        country: '',
        description: '',
      }
    };
  },
  props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
  created(){
    this.getProfileData(this.userdata.id);
    console.log(
      "Masuk data",this.profileData
    )
    this.fetchCountries();
    this.profile.name=this.profileData.name;
    this.profile.phone=this.profileData.phone;
    this.profile.email=this.profileData.email;
    this.profile.username = this.profileData.username
    this.profile.country = this.profileData.country
    this.profile.description = this.profileData.description
    console.log(
      "Masuk profil",this.profile
    )
  },
  methods: {
    ...mapActions("country",["fetchCountries"]),
    ...mapActions("profile", ["getProfileData","updateProfileData"]),
    openPhotoDialog() {
      // Show photo upload dialog
    },

    submitProfile() {
      this.profile.country=this.profile.country?.id
      this.updateProfileData({id:this.userdata.id,body:this.profile}).then(()=>{
        Swal.fire({
          icon: 'success',
          title: 'Update Profile',
          text: 'Your profile has been updated.'
        }).then(()=>{
          this.$router.push('/sellerprofile')
        })
      })
    },

    resetProfile() {
      // Reset profile data
      this.$router.push('/sellerprofile')
    },
  },
};
</script>
