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
            <v-card-text>Description: {{ productData.productDescription }}</v-card-text>
            <v-card-text>Ready At: {{ productData.readyAt }}</v-card-text>
            <v-card-text>Price: {{ productData.price }}</v-card-text>
            <v-card-actions>
                <v-btn color="primary"
                    @click="$router.push({ name: 'sellereditproduct', params: { id: productData.id } })">Edit</v-btn>
                <v-btn color="error" @click="deleteProduct(productData.id)">Delete</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>
  
<script>
import { mapState, mapActions } from "vuex";
import VueCarousel from "vue-carousel";
import Swal from "sweetalert2";
import Header from "../../components/Header.vue";
export default {
    name: "ProductDetails",
    components: {
        VueCarousel,
        Header
    },
    computed: {
        ...mapState("product", ["productData"]),
    },
    mounted() {
        console.log("product id localstorage",localStorage.getItem('id'));
        this.fetchProductbyId(localStorage.getItem('id'));

    },
    methods: {
        ...mapActions("product", ["fetchProductbyId", "deleteProductbyId"]),

        deleteProduct() {
            Swal.fire({
                title: 'Are you sure you want to delete this product?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Yes, delete it!',
                cancelButtonText: 'No, cancel',
            }).then((result) => {
                if (result.value) {
                    this.deleteProductbyId(localStorage.getItem('id')).then(() => {
                        this.$router.push('/sellerproduct');
                    });
                }
            });
        },
    },
};
</script>
  