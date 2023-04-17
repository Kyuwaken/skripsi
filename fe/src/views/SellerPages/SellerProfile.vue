<template>
  <v-container fluid>
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
            <span style="text-indent: 15px">{{ sellerName }}</span>
          </v-card-title>
          <v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Username:</div>
                <div class="info-value">{{ sellerUsername }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Email:</div>
                <div class="info-value">{{ sellerEmail }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Phone Number:</div>
                <div class="info-value">{{ sellerPhoneNumber }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Seller Country:</div>
                <div class="info-value">{{ sellerCountry }}</div>
              </div>
            </v-card-text>
            <v-card-text>
              <div class="info-box">
                <div class="info-title">Description:</div>
                <div class="info-value">{{ description }}</div>
              </div>
            </v-card-text>
            <router-view></router-view>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'SellerProfile',
  computed: {
    sellerName() {
      return this.$store.getters.sellerName;
    },
    sellerUsername() {
      return this.$store.getters.sellerUsername;
    },
    sellerEmail() {
      return this.$store.getters.sellerEmail;
    },
    sellerPhoneNumber() {
      return this.$store.getters.sellerPhoneNumber;
    },
    sellerCountry() {
      return this.$store.getters.sellerCountry;
    },
    description() {
      return this.$store.getters.sellerDescription;
    },
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
};
</script>

<style>
.caption {
  font-size: 12px;
  color: grey;
}
</style>
