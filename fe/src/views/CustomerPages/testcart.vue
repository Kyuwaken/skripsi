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
              <v-subheader>{{ group && group.seller ? group.seller.name : 'no name' }}</v-subheader>
              <v-list-item v-for="(item, i) in group.items" :key="i">
                <v-list-item-content>
                  <v-list-item-title>{{ item.name }}</v-list-item-title>
                  <v-list-item-subtitle>Price: {{ item.price }} {{
                    item.currency }}</v-list-item-subtitle>
                  <v-list-item-subtitle>Quantity:
                    <v-btn class="mr-1" fab small color="primary"
                      @click="decrementQuantity(item)">
                      <v-icon>mdi-minus</v-icon>
                    </v-btn>
                    {{ item.quantity }}
                    <v-btn class="ml-1" fab small color="primary"
                      @click="incrementQuantity(item)">
                      <v-icon>mdi-plus</v-icon>
                    </v-btn>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>Total: {{ item.price * item.quantity
                  }} {{ item.currency }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="checkout">Checkout</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  
  <script>
  export default {
    data() {
      return {
        cart: [
          {
            product: { id: 1, name: "Product A", price: 10, quantity: 2, currency: "USD" },
            seller: { id: 1, name: "Seller A" },
          },
          {
            product: { id: 2, name: "Product B", price: 15, quantity: 1, currency: "USD" },
            seller: { id: 2, name: "Seller B" },
          },
          {
            product: { id: 3, name: "Product C", price: 20, quantity: 3, currency: "USD" },
            seller: { id: 1, name: "Seller A" },
          },
        ],
        groupedCart: [],
      };
    },
    computed: {
      selectedSellers() {
        return this.groupedCart.filter((group) => group.selected).map((group) => group.seller);
      },
    },
    methods: {
      incrementQuantity(item) {
        item.editing = true;
        item.newQuantity = item.quantity + 1;
      },
      decrementQuantity(item) {
        if (item.quantity > 1) {
          item.editing = true;
          item.newQuantity = item.quantity - 1;
        }
      },
      deleteProduct(item) {
        const sellerGroup = this.groupedCart.find((group) => group.seller.id === item.seller.id);
        sellerGroup.items = sellerGroup.items.filter((product) => product.id !== item.id);
        if (sellerGroup.items.length === 0) {
          this.groupedCart = this.groupedCart.filter((group) => group.seller.id !== sellerGroup.seller.id);
        }
      },
      confirmEdit(item) {
        if (item.newQuantity !== item.quantity) {
          item.quantity = item.newQuantity;
        }
        item.editing = false;
        item.newQuantity = 0;
      },
      checkout() {
        if (this.selectedSellers.length === 0) {
          alert("Please select at least one seller.");
          return;
        } else if (this.selectedSellers.length > 1) {
          alert("Please select only one seller at a time.");
          return;
        }
  
        // Implement checkout functionality here for the selected seller
        const selectedSeller = this.selectedSellers[0];
        console.log(`Checking out ${selectedSeller.name}`);
      },
    },
    mounted() {
      const grouped = {};
      for (const { seller, product } of this.cart) {
        if (!grouped[seller.id]) {
          grouped[seller.id] = { seller, items: [], selected: false };
        }
        grouped[seller.id].items.push({ ...product, editing: false, newQuantity: 0 });
      }
      this.groupedCart = Object.values(grouped);
    },
  };
  </script>