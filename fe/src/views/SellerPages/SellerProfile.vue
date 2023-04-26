<template>
  <v-container fluid>
    <v-app-bar app color="white" flat>
      <Header></Header>
    </v-app-bar>
    <v-row>
      <v-col cols="3">
        <v-list class="d-flex flex-column align-content-space-between">
          <v-list-item v-for="item in items" :key="item.title" router :to="item.link">
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col cols="9">
        <v-card class="fill-height">
          <v-card-title>
            <span style="text-indent: 15px">{{ profileData.name }}</span>
          </v-card-title>
          <v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Username:</div>
                <div class="info-value">{{ profileData.username }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Email:</div>
                <div class="info-value">{{ profileData.email }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Phone Number:</div>
                <div class="info-value">{{ profileData.phone }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Seller Country:</div>
                <div class="info-value">{{ profileData.country?.name }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Description:</div>
                <div class="info-value">{{ profileData.description }}</div>
              </div>
            </v-card-text>
            <v-card-actions class="justify-end mr-6">
              <v-btn variant="outlined"
              @click="editProfile"> Update </v-btn>
            </v-card-actions>
            <router-view></router-view>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import crypto from "@/plugins/crypto";
import Header from "../../components/Header.vue";
export default {
  name: 'SellerProfile',
  components:{
    Header
  },
  mixins: [crypto],
  computed: {
    ...mapState("profile", ["profileData"]),
  },
  // props: {
  //   userdata: {
  //     type: Object,
  //     required: true,
  //   },
  // },
  created() {
    var user = this.decryptLocalStorage(
        localStorage.getItem("encryptedData")
    );
    this.getProfileData(user.id);
  },
  data: () => ({
    items: [
      {
        title: 'Update Profile',
        icon: 'mdi-account',
        link: '/sellereditprofile'
      },
      {
        title: 'Post a Product',
        icon: 'mdi-cart',
        link: '/addproduct'
      },
      {
        title: 'Products List',
        icon: 'mdi-format-list-bulleted',
        link: '/sellerproduct'
      },
      {
        title: 'Transactions',
        icon: 'mdi-history',
        link: '/sellertransactionlist'
      },
      
    ],
  }),
  methods: {
    ...mapActions("profile", ["getProfileData"]),
    editProfile(){
        this.$router.push({path:"/sellereditprofile"})
    },
    saveProfile() {
      // send data to server to save
      axios
        .post("/api/profile", {
          name: this.name,
          phone: this.phone,
          email: this.email,
          photo: this.photo,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.caption {
  font-size: 12px;
  color: grey;
}
</style>
