<template>
  <v-container fluid>
    <v-row class="justify-md-start">
      <v-col cols="12" class="text-left mt-5">
        <v-btn icon color="secondary" dark @click="goBack()">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-row class="justify-center">
      <v-col cols="6" sm="4" md="3" lg="2">
        <v-card class="mx-auto mb-5" max-width="350">
          <v-card-title class="text-center">
            <h2 class="mb-0">Register as Customer </h2>
          </v-card-title>
          <v-card-actions class="justify-center">
            <v-btn block color="primary" dark @click="goToCustomerRegister()">
              Sign Up
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="6" sm="4" md="3" lg="2">
        <v-card class="mx-auto mb-5" max-width="350">
          <v-card-title class="text-center">
            <h2 class="mb-0">Register as Seller</h2>
          </v-card-title>
          <v-card-actions class="justify-center">
            <v-btn block color="primary" dark @click="goToSellerRegister()">
              Sign Up
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    goBack() {
      this.$router.push({ path: '/' })
    },
    goToCustomerRegister() {
      this.$router.push({ path: '/customerregistration' })
    },
    goToSellerRegister() {
      this.$router.push({ path: '/sellerregistration' })
    },
  },
}
</script>