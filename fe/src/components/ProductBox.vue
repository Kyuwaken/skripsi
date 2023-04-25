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
            <p>{{ product.description }}</p>
        </v-card-subtitle>
        <v-card-actions class="d-flex justify-center">
            <v-btn class="hover" color="primary"  @click="goTo">See Details</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import crypto from '@/plugins/crypto';

    export default {
        name: "ProductBox",
        props: {
            product: {
                type: Object,
                required: true,
            },
        },
        mixins: [crypto],
        created(){
            console.log(this.product)
        },
        methods:{
            goTo(){
                var user = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
                console.log("role",user)
                if(user.role == "Seller"){
                    localStorage.setItem('id', this.product.id)
                    this.$router.push({
                        name: 'sellerproductdetails',
                        params: { id: this.product.id }
                    })
                }
                else{
                    this.$router.push({
                        name: 'customerproductdetails',
                        params: { id: this.product.id }
                    })
                }
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