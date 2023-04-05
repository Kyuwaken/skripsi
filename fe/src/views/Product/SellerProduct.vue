<template>
    <div class="container">
        <div class="row">
            <div class="col-12 text-center">
                <h4> Your Products</h4>
                <router-link :to="{name: 'AddProduct'}" style="float: right">
                    <button class="btn" >
                        Add Product
                    </button> </router-link>
            </div>
        </div>
        <v-row justify="space-between">
            <v-col v-for="product of products" :key="product.id">
                <ProductBox :product="product"/>
            </v-col>
        </v-row>
        <!-- <div class="row"> -->
<!--            display all the products in productbox component-->
            <!-- <div v-for="product of products" :key="product.id"
                 class="col-md-6 col-xl-4 col-12 pt-3 d-flex">
                <ProductBox :product="product"/>
            </div>
        </div> -->
    </div>
</template>
<script>
    import ProductBox from "../../components/ProductBox.vue";
    export default {
        components: {ProductBox},
        props:["products"]
    }
</script>