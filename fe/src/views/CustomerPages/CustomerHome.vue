<template>
    <v-container>
        <v-row>
            <v-carousel cycle height="400" hide-delimiter-background show-arrows="hover" class="rounded-lg ma-3">
                <v-carousel-item v-for="(slide, i) in slides" :key="i">
                    <v-sheet :color="colors[i]" height="100%">
                        <div class="d-flex fill-height justify-center align-center">
                            <div class="text-h2">
                                {{ slide }} Slide
                            </div>
                        </div>
                    </v-sheet>
                </v-carousel-item>
            </v-carousel>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-sheet outlined color="white" elevation="2" rounded="lg">
                    <v-container fluid>
                        <v-row no-gutters class="ma-2">
                            Category
                        </v-row>
                        <v-row>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-sheet>
            </v-col>
        </v-row>

        <v-divider class="mt-5 mb-5"></v-divider>
        <v-row cols=12 class="mt-4" v-if="productData.length > 0">
            <v-col v-for="product in productData" :key="product.id" cols="12" sm="6" md="4" lg="3">
                <ProductHome @add-to-cart="addToCart" :product="product" />
            </v-col>
        </v-row>
        <!-- <v-row>
            <v-col cols=12>
                <v-sheet outlined color="white" elevation="5">
                    <v-row class="justify-center mt-4">
                        <h1>You May Like</h1>
                    </v-row>
                    <v-row>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                    </v-row>
                </v-sheet>
            </v-col>
        </v-row> -->


        <!-- <v-row class="ma-5">
            <v-hover>
                <router-link to="/">
                    <v-img src="https://picsum.photos/200/300/?blur"></v-img>
                </router-link>
            </v-hover>

        </v-row> -->
    </v-container>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import ProductHome from "@/components/ProductHome.vue";
import crypto from '@/plugins/crypto';
export default {
    computed: {
        ...mapState("category", ['categories']),
        ...mapState("product", ["productData"]),
    },
    data() {
        return {
            colors: [
                'indigo',
                'warning',
                'pink darken-2',
                'red lighten-1',
                'deep-purple accent-4',
            ],
            slides: [
                'First',
                'Second',
                'Third',
                'Fourth',
                'Fifth',
            ],
        }
    },
    mixins: [crypto],
    props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
    mounted() {
        //console.log("masuk mounted")
        this.fetchProduct();
        this.fetchCategories();
    },
    methods:{
        ...mapActions("category", ["fetchCategories"]),
        ...mapActions("product", ["fetchProduct"]),
        ...mapActions("cart",["postCart"]),
        addToCart(productId){
            var user = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
            this.postCart({product:productId,user:user.id})
        },
    },
    components: { ProductHome },
    props: ["products"]
}
</script>