<template>
  <v-container>
    <v-row class="mb-4">
      <v-col>
        <v-btn color="primary" icon to="/sellerprofile">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <div class="text-center">
      <h4 class="mb-4">Your Products</h4>
    </div>
    <v-row class="mt-4" v-if="productData.length > 0">
      <v-col v-for="product in productData" :key="product.id" cols="12" sm="6" md="4" lg="3">
        <ProductBox :product="product" />
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col>
        <div class="text-center my-5">
          <p>No products to display.</p>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ProductBox from "@/components/ProductBox.vue";
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Header from "../../components/Header.vue";
export default {
  name: "ProductList",
  components: {
    ProductBox,
    Header
  },
  props: {
    userdata: {
      type: Object,
      required: true
    }
  },
  computed:{
    ...mapState("product", ['productData'])
  },
  data() {
        return {
            name: '',
            productDescription: '',
            price: '',
            preorderTime: '',
            productPhoto: [],
            category: ''
        }
    },
  mounted(){
    //console.log("userdata", this.userdata.id)
    let data = {"id": this.userdata.id}
    console.log(data)
    this.fetchProductbySeller(data)
    console.log("view product data", this.productData)
  },
  methods:{
    ...mapActions('product', ['fetchProductbySeller']),
  }
};


</script>

<style scoped>
/* Add any custom styles here */
</style>
