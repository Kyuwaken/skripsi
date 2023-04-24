<template>
  <v-container>
    <v-btn icon left @click="$router.push('/customerhome/')">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>
    <h1 class="text-center my-6">My Cart</h1>
    <v-list class="my-4" style="max-height: 600px; overflow-y: auto">
      <v-list-item
        v-for="(transaction, index) in transactions"
        :key="index"
        class="mb-16 list_item"
        :style="index == 0 ? 'border-top: 5px solid rgba(0, 0, 0, 0.12)' : ''"
      >
        <v-row v-if="index == 0" class="mt-6 mb-6">
            <v-col cols="2">
                <img :src="transaction.product.product_image[0].path" :alt="transaction.product.name" height="100">
            </v-col>
            <v-col cols="7">
                <v-list-item-content>
                <div class="text-h6">{{ transaction.product.name }}</div>
                <div class="mt-2">Price: {{ transaction.product.price }}</div>
                <div>
                    Quantity:
                    {{
                    transaction.quantity
                    }}
                    function(transaction.transaction_detail)
                </div>
                </v-list-item-content>
                return len(Transaction_detail)
            </v-col>
            <v-col>
                <v-list-item-action>
                <v-btn
                    class="mt-8"
                    color="primary"
                    @click="goToDetailsPage(transaction)"
                    >View Details</v-btn
                >
                <v-btn
                    icon
                    @click="goToDetailsPage(transaction)"
                    ><v-icon>
                      mdi-minus-box-outline
                    </v-icon>
                </v-btn>
                <v-btn
                    icon
                    @click="goToDetailsPage(transaction)"
                    ><v-icon>
                      mdi-plus-box-outline
                    </v-icon>
                </v-btn>
                </v-list-item-action>
            </v-col>
        </v-row>
        <v-row v-else class="mb-6">
            <v-col cols="2">
                <img :src="transaction.product.product_image[0].path" :alt="transaction.product.name" height="100">
            </v-col>
            <v-col cols="7">
                <v-list-item-content>
                <div class="text-h6">{{ transaction.product.name }}</div>
                <div class="mt-2">Price: {{ transaction.product.price }}</div>
                <div>
                    Quantity:
                    {{
                    transaction.quantity
                    }}
                    function(transaction.transaction_detail)
                </div>
                </v-list-item-content>
                return len(Transaction_detail)
            </v-col>
            <v-col>
                <v-list-item-action>
                <v-btn
                    class="mt-8"
                    color="primary"
                    @click="goToDetailsPage(transaction)"
                    >View Details</v-btn
                >
                </v-list-item-action>
            </v-col>
        </v-row>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<style scoped>
.list_item {
  border-bottom: 5px solid rgba(0, 0, 0, 0.12);
}
</style>
  
<script>
import { mapActions, mapState } from "vuex";
import Header from "../../components/Header.vue";
export default {
  name: "TransactionList",
  components:{
    Header
  },
  data() {
    return {
      transactions: [
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 1",
          price: 10.99,
          quantity: 1,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 2",
          price: 5.99,
          quantity: 2,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
        {
          image: "https://via.placeholder.com/150",
          productName: "Product 3",
          price: 8.99,
          quantity: 3,
        },
      ],
    };
  },
  props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapState("cart", ["cart"]),
  },
  created() {
    this.fetchCartById({id:this.userdata.id}).then(()=>{
        console.log("cart",this.cart)
        this.transactions = this.cart
    })
  },
  methods: {
    ...mapActions("cart", [
      "fetchCartById",
      "postCart",
      "decreaseCart",
      "customCart",
    ]),
    goToDetailsPage(transaction) {
      this.$router.push({name: 'customerproductdetails', params: { id: transaction.product.id }})
      // Navigate to the transaction details page
    },
  },
};
</script>