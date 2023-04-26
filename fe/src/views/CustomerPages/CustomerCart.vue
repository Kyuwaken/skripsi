<template>
  <v-container>
    <v-card>
      <v-card-title>
        <h2>My Cart</h2>
      </v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <v-list>
          <v-list-item-group v-for="(group) in groupedCart" :key="group.seller.id">
            <v-row align="center">
              <v-col cols="1">
                <v-checkbox :label="`${group && group.seller ? group.seller.name : 'no name'}`" v-model="selectedSeller"
                  :value="group.seller" :disabled="selectedSeller && selectedSeller.id !== group.seller.id"></v-checkbox>
              </v-col>
            </v-row>
            <template>
              <v-list-item v-for="item in group.items" :key="item.id">
                <v-list-item-content>
                  <v-list-item-title>{{ item.name }}</v-list-item-title>
                  <v-list-item-subtitle>Price: {{ item.price }} {{ item.currency }}</v-list-item-subtitle>
                  <v-list-item-subtitle>
                    <template v-if="item.editing">
                      Quantity:
                      <v-btn class="mr-1" fab small color="primary" @click="decrementQuantity(item)">
                        <v-icon>mdi-minus</v-icon>
                      </v-btn>
                      {{ item.newQuantity }}
                      <v-btn class="ml-1" fab small color="primary" @click="incrementQuantity(item)">
                        <v-icon>mdi-plus</v-icon>
                      </v-btn>
                      <v-icon @click="confirmEdit(item)">mdi-check</v-icon>
                      <v-icon @click="cancelEdit(item)">mdi-close</v-icon>
                    </template>
                    <template v-else>
                      Quantity:
                      {{ item.quantity }}
                      <v-btn class="ml-1" fab small color="primary" @click="toggleEditing(item)">
                        <v-icon>mdi-pencil</v-icon>
                      </v-btn>
                      <v-btn class="ml-1" fab small color="primary" @click="confirmDelete(item)">
                        <v-icon>mdi-delete</v-icon>
                      </v-btn>
                    </template>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>Total: {{ item.price * item.quantity }} {{ item.currency
                  }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list-item-group>
        </v-list>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn :disabled="selectedSeller === null" color="primary" @click="checkout">Checkout</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>



<script>
import { mapActions, mapState } from "vuex";
import Header from "../../components/Header.vue";
import crypto from "@/plugins/crypto";
export default {
  name: "TransactionList",
  mixins: [crypto],
  components:{
    Header
  },
  data() {
    return {
      tempCart: [],
      groupedCart: [],
      selectedSeller: null,
    };
  },
  computed: {
    ...mapState("cart", ["cart"]),
  },

  methods: {
    ...mapActions("cart", ["fetchCartById", "updateQuantity", "deleteCart"]),
    incrementQuantity(item) {
      item.newQuantity = item.newQuantity + 1;
    },
    decrementQuantity(item) {
      if (item.quantity > 1) {
        item.newQuantity = item.newQuantity - 1;
      }
    },
    deleteProduct(item) {
      const sellerGroup = this.groupedCart.find((group) => group.seller.id === item.seller.id);
      sellerGroup.items = sellerGroup.items.filter((product) => product.id !== item.id);
      if (sellerGroup.items.length === 0) {
        this.groupedCart = this.groupedCart.filter((group) => group.seller.id !== sellerGroup.seller.id);
      }
      //submit ke be pake item.id
      this.deleteCart(item.cartId)
    },
    confirmEdit(item) {
      if (item.newQuantity !== item.quantity) {
        item.quantity = item.newQuantity;
      }
      item.editing = false;
      item.newQuantity = 0;
      //submit ke be
      this.updateQuantity({ id: item.cartId, quantity: item.quantity })
    },
    cancelEdit(item) {
      item.editing = false;
    },
    toggleEditing(item) {
      item.editing = true;
      item.newQuantity = item.quantity;
    },
    confirmDelete(item) {
      if (confirm(`Are you sure you want to delete ${item.name}?`)) {
        this.deleteProduct(item);
      }
    },
    checkout() {
      if (this.selectedSeller.length === 0) {
        alert("Please select at least one seller.");
        return;
      } else if (this.selectedSeller.length > 1) {
        alert("Please select only one seller at a time.");
        return;
      }

      // Implement checkout functionality here for the selected seller
      const selectedSeller = this.selectedSeller;
      localStorage.setItem('checkoutSellerId', selectedSeller.id)
      this.$router.push('/checkout')
      console.log(`Checking out ${selectedSeller.name}`);
      //console.log(this.groupedCart)
    },
  },
  mounted() {
    var user = this.decryptLocalStorage(
        localStorage.getItem("encryptedData")
      );
    this.fetchCartById({ id: user.id }).then(() => {
      this.tempCart = this.cart;
      //console.log("tempcart", this.tempCart)
      const grouped = {};
      for (const { product, id, quantity } of this.tempCart) {
        if (!grouped[product.seller.id]) {
          grouped[product.seller.id] = { seller: product.seller, items: [], selected: false };
        }
        grouped[product.seller.id].items.push({ ...product, editing: false, newQuantity: 0, cartId: id, quantity: quantity });
      }
      this.groupedCart = Object.values(grouped);
    })


    //console.log("grouped cart", this.groupedCart)
  },

};
</script>