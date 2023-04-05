<template>
    <v-card elevation="10">
        <v-card-title class="pa-0">
            <img 
                class="card-image" 
                :src= "product.imageURL"
            />
        </v-card-title>
        <v-card-text class="pa-2">
            <h3>{{ product.name }}</h3>
        </v-card-text>
        <v-card-actions class="d-flex justify-center">
          <v-btn color="primary">See Details</v-btn>
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
.card-image{
    height: 200px;
    width: 100%;
}
</style>