<template>
    <v-container>
      <v-btn icon color="primary" class="back-btn" @click="$router.go(-1)">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-carousel v-if="productData">
        <v-carousel-item
          v-for="(image, index) in productData.product_image"
          :key="index"
        >
          <v-img
            :src="'data:' + image.imageType + ';base64,' + image.stringBase64"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
      <v-card>
        <v-card-title>{{ productData.name }}</v-card-title>
        <v-card-text>{{ productData.productDescription }}</v-card-text>
        <v-card-text>Price: {{ productData.price }}</v-card-text>
        
      </v-card>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import VueCarousel from "vue-carousel";
  
  export default {
    name: "ProductDetails",
    components: {
      VueCarousel,
    },
    computed: {
      ...mapState("product", ["productData"]),
    },
    mounted() {
      console.log(this.$route.params.id);
      this.fetchProductbyId(this.$route.params.id);
    },
    methods: {
      ...mapActions("product", ["fetchProductbyId"]),
    },
  };
  </script>