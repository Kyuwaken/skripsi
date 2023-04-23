<template>
    <v-container>
        <v-btn icon color="primary" class="back-btn" @click="$router.go(-1)">
            <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-carousel v-if="productData">
            <v-carousel-item v-for="(image, index) in productData.product_image" :key="index">
                <v-img :src="image.path"></v-img>
            </v-carousel-item>
        </v-carousel>
        <v-card>
            <v-card-title>{{ productData.name }}</v-card-title>
            <v-card-text>{{ productData.productDescription }}</v-card-text>
            <v-card-text>Price: {{ productData.price }}</v-card-text>
            <!-- <v-card-actions>
                <v-btn color="primary"
                    @click="$router.push({ name: 'sellereditproduct', params: { id: productData.id } })">Edit</v-btn>
                <v-btn color="error" @click="deleteProduct(productData.id)">Delete</v-btn>
            </v-card-actions> -->
        </v-card>
        <v-card-actions>
            <v-btn class="hover" color="primary" @click="addToCart">Add to cart</v-btn>
            <v-btn class="hover" color="primary" @click="clickedFavorite"><v-icon v-if="!productData.favorite">mdi-heart-outline</v-icon> <v-icon v-if="productData.favorite">mdi-heart</v-icon></v-btn>
        </v-card-actions>
    </v-container>
</template>
  
<script>
import { mapState, mapActions } from "vuex";
import VueCarousel from "vue-carousel";
import crypto from '@/plugins/crypto';
// import Swal from "sweetalert2";
export default {
    name: "CustomerProductDetails",
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
  