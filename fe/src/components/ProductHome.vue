<template>
    <v-card elevation="10">
        <v-card-title class="pa-0">
            <img 
                class="card-image" 
                :src="'data:' + product.product_image[0].imageType + ';base64,' + product.product_image[0].stringBase64"
                :alt="product.name"
            />
        </v-card-title>
        <v-card-subtitle class="pa-2">
            <h3>{{ product.name }}</h3>
            <p>{{ product.price }}</p>
        </v-card-subtitle>
        <v-card-actions class="d-flex justify-center">
            <v-btn class="hover" color="primary" :to="{ name: 'sellerproductdetails', params: { id: product.id } }">See Details</v-btn>
            <v-btn class="hover" color="primary" onclick="addToCart(product.id)">Add to cart</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "ProductHome",
        props: ["product"],
        props: {
            userdata: {
            type: Object,
            required: true,
            },
        },
        methods:{
            ...mapActions("cart",["postCart"]),
            addToCart(productId){
                this.postCart({product:productId,user:this.userdata.id})
            }
        }
    }
</script>

<style scoped>
    .card-image {
    height: 200px;
    width: 100%;
}
</style>