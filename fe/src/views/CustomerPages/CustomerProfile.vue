<template>
  <v-container fluid>
    <v-row>
      <!-- <v-col cols="3">
        <v-list class="d-flex flex-column align-content-space-between">
          <v-list-item
            v-for="item in items"
            :key="item.title"
            router
            :to="item.link"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col> -->
      <v-btn icon left @click="$router.push('/customerhome/')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-col cols="12">
        <v-card class="fill-height">
          <v-card-title>
            <div>{{ profileData.name }}</div>
          </v-card-title>
          <v-card-text> Username : {{ profileData.username }} </v-card-text>
          <v-card-text> Phone : {{ profileData.phone }} </v-card-text>
          <v-card-text> Email : {{ profileData.email }} </v-card-text>
          <v-card-actions class="justify-end mr-6">
            <v-btn variant="outlined" @click="editProfile"> Update </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Header from "../../components/Header.vue";
export default {
  name: "BuyerProfile",
  components: {
    Header,
  },
  data: () => ({
    buyerName: "JohnyDoe",
    phone: "",
    email: "",
    photo: "",
    nik: "",
    profile_picture: "",
    items: [
      {
        title: "History",
        icon: "mdi-history",
        link: "/customertransaction/",
      },
      {
        title: "Favorite",
        icon: "mdi-heart-outline",
        link: "/customerfavorite/",
      },
      {
        title: "Cart",
        icon: "mdi-cart-outline",
        link: "/customercart/",
      },
    ],
  }),
  computed: {
    ...mapState("profile", ["profileData"]),
  },
  props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
  created() {
    this.getProfileData(this.userdata.id);
    console.log(this.userdata);
  },
  methods: {
    ...mapActions("profile", ["getProfileData"]),
    editProfile() {
      this.$router.push({ path: "/customereditprofile" });
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
h1 {
  margin: 0;
  font-size: 36px;
}
</style>