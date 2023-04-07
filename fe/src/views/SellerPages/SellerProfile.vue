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
              <v-avatar class="mr-3" size="64">
                <img :src="sellerProfilePic" alt="Seller Profile Pic">
              </v-avatar>
              <div>
                <div>{{ sellerName }}</div>
                <div class="caption">{{ sellerCountry }}</div>
              </div>
            </v-card-title>
            <v-card-text>
              <h2>text heree</h2>
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
    data: () => ({
      sellerProfilePic: 'path/to/seller-profile-pic.png',
      sellerName: 'John Doe',
      sellerCountry: 'United States',
      items: [
        {
          title: 'Update Profile',
          icon: 'mdi-account',
          link: '/seller/profile/update'
        },
        {
          title: 'Post a Product',
          icon: 'mdi-cart',
          link: '/seller/products/post'
        },
        {
          title: 'Update Products',
          icon: 'mdi-cart-outline',
          link: '/seller/products/update'
        },
        {
          title: 'Transactions',
          icon: 'mdi-history',
          link: '/seller/transactions'
        },
        {
          title: 'Products List',
          icon: 'mdi-format-list-bulleted',
          link: '/seller/products/list'
        },
      ],
    }),
  }
  </script>
  
  <style>
  .caption {
    font-size: 12px;
    color: grey;
  }
  </style>