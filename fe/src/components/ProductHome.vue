<template>
    <v-card elevation="10">
        <v-card-title class="pa-0">
            <img 
                class="card-image" 
                :src="product.product_image[0].path"
                :alt="product.name"
            />
        </v-card-title>
        <v-card-subtitle class="pa-2">
            <h3>{{ product.name }}</h3>
            <p>{{ product.price }}</p>
        </v-card-subtitle>
        <v-card-actions class="d-flex justify-center">
            <v-btn class="hover" color="primary" @click="goTo">See Details</v-btn>
            <v-btn class="hover" color="primary" @click="addToCart">Add to cart</v-btn>
            <v-btn class="hover" color="primary" @click="addToFavorite">Add to favorite</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "ProductHome",
        props: ["product"],
        methods:{
            addToCart(){
                this.$emit('add-to-cart', this.product.id)
            },
            addToFavorite(){
                this.$emit('add-to-favorite', this.product.id)
            },
            goTo(){
                this.$router.push({name: 'customerproductdetails', params: { id: this.product.id }})
            }
        },
    }
</script>

<style scoped>
.card-image {
    height: 200px;
    width: 100%;
}
</style>