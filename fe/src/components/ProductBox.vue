<template>
    <v-card elevation="10">
        <v-card-title class="pa-0">
            <img 
                class="card-image" 
                :src="product.imageURL"
                :alt="product.name"
            />
        </v-card-title>
        <v-card-subtitle class="pa-2">
            <h3>{{ product.name }}</h3>
            <p>{{ product.description }}</p>
        </v-card-subtitle>
        <v-card-actions class="d-flex justify-center">
            <v-btn class="hover" color="primary">See Details</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "ProductBox",
        props: ["product"]
    }
</script>

<style scoped>
.card-image {
    height: 200px;
    width: 100%;
}
</style>