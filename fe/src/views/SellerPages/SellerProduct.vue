<template>
  <v-container>
    <v-row class="mb-4">
      <v-col>
        <v-btn color="primary" icon to="/sellerprofile">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <div class="text-center">
      <h4 class="mb-4">Your Products</h4>
    </div>
    <v-row justify="space-between" class="mt-4" v-if="products.length > 0">
      <v-col v-for="product in products" :key="product.id" cols="12" sm="6" md="4" lg="3">
        <ProductBox :product="product" />
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col>
        <div class="text-center my-5">
          <p>No products to display.</p>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ProductBox from "@/components/ProductBox.vue";

export default {
  name: "ProductList",
  components: {
    ProductBox
  },
  props: {
    products: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
