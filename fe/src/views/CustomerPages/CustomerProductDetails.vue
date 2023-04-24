<template>
    <!-- The container holds all the elements of the product details page -->
    <v-container>
  
      <!-- The back button allows users to go back to the previous page -->
      <v-btn icon color="primary" class="back-btn" @click="$router.go(-1)">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
  
      <!-- The carousel displays all images of the product -->
      <v-carousel v-if="productData" hide-delimiters>
        <v-carousel-item v-for="(image, index) in productData.product_image" :key="index">
          <v-img :src="image.path" width="100%"></v-img>
        </v-carousel-item>
      </v-carousel>
  
      <!-- The card holds all the product information -->
      <v-card class="pa-4">
        <v-card-title class="headline">{{ productData.name }}</v-card-title>
        <v-card-text class="body-1">{{ productData.productDescription }}</v-card-text>
        <v-card-text class="body-2">Price: {{ productData.price }}</v-card-text>
        <v-divider class="my-4"></v-divider>
  
        <!-- The card actions hold the buttons for adding the product to the cart and to the favorites -->
        <v-card-actions>
          <v-btn class="hover mr-4" color="primary" @click="addToCart">Add to cart</v-btn>
          <v-btn class="hover" color="primary" @click="clickedFavorite">
            <v-icon v-if="!productData.favorite">mdi-heart-outline</v-icon>
            <v-icon v-if="productData.favorite">mdi-heart</v-icon>
            <span class="pl-2">{{ productData.favorite ? 'Remove from favorites' : 'Add to favorites' }}</span>
          </v-btn>
        </v-card-actions>
      </v-card>
  
    </v-container>
  </template>
  
  
<script>
import { mapState, mapActions } from "vuex";
import VueCarousel from "vue-carousel";
import crypto from '@/plugins/crypto';
import Header from "../../components/Header.vue";
// import Swal from "sweetalert2";
export default {
    name: "CustomerProductDetails",
    components: {
        VueCarousel,
        Header,
    },
    computed: {
        ...mapState("product", ["productData"]),
    },
    mounted() {
        console.log(this.$route.params.id);
        this.fetchProductbyId(this.$route.params.id);

    },
    mixins: [crypto],
    methods: {
        ...mapActions("product", ["fetchProductbyId","clickFavorite"]),
        ...mapActions("cart",["postCart"]),
        addToCart(){
            var user = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
            this.postCart({product:this.productData.id,user:user.id})
        },
        clickedFavorite(){
            var user = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
            this.clickFavorite({product:this.productData.id,user:user.id})
        }
        // deleteProduct() {
        //     Swal.fire({
        //         title: 'Are you sure you want to delete this product?',
        //         icon: 'warning',
        //         showCancelButton: true,
        //         confirmButtonText: 'Yes, delete it!',
        //         cancelButtonText: 'No, cancel',
        //     }).then((result) => {
        //         if (result.value) {
        //             this.deleteProductbyId(this.$route.params.id).then(() => {
        //                 this.$router.push('/sellerproduct');
        //             });
        //         }
        //     });
        // },
    },
};
</script>
  