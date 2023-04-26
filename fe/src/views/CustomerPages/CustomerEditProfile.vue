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
            :rules="[v => !!v || 'Name is required']"
          ></v-text-field>
          <v-text-field
            v-model="profile.username"
            label="Username"
            :rules="[v => !!v || 'Username is required']"
          ></v-text-field>
  
          <v-text-field
            v-model="profile.phone"
            label="Phone Number"
            pattern="[0-9]*"
            maxlength="15"
            :rules="[v => !!v || 'Phone number is required', v => /^\d{15}$/.test(v) || 'Phone number must be 10 digits']"
          ></v-text-field>

          <v-text-field
            v-model="profile.email"
            label="Email"
            type="email"
            :rules="[v => !!v || 'Email is required', v => /.+@.+\..+/.test(v) || 'Email must be valid']"
          ></v-text-field>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" @click="resetProfile">Cancel</v-btn>
            <v-btn color="primary" @click="submitProfile">Submit</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Swal from 'sweetalert2';
import Header from "../../components/Header.vue";
export default {
  data() {
    return {
      profile: {
        name: '',
        username:'',
        phone: '',
        email: '',
      }
    };
  },
  props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState("profile", ["profileData"]),
  },
  created(){
    this.getProfileData(this.userdata.id);
    this.profile.name=this.profileData.name;
    this.profile.phone=this.profileData.phone;
    this.profile.email=this.profileData.email;
    this.profile.username = this.profileData.username
  },

  methods: {
    ...mapActions("profile", ["getProfileData","updateProfileData"]),
    openPhotoDialog() {
      // Show photo upload dialog
    },
    submitProfile() {
      this.updateProfileData({id:this.userdata.id,body:this.profile}).then(()=>{
        Swal.fire({
          icon: 'success',
          title: 'Update Profile',
          text: 'Your profile has been updated.'
        }).then(()=>{
          this.$router.push('/customerprofile')
        })
      })
    },

    resetProfile() {
      this.$router.push('/customerprofile')
      // Reset profile data
    },
  },
};
</script>
