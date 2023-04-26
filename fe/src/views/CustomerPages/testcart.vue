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
                                <v-checkbox :label="`${group && group.seller ? group.seller.name : 'no name'}`"
                                    v-model="selectedSeller" :value="group.seller"
                                    :disabled="selectedSeller && selectedSeller.id !== group.seller.id"></v-checkbox>
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
            selectedSeller: null,
        };
    },
    computed: {
        selectedSellers() {
            return this.groupedCart.filter((group) => group.selected).map((group) => group.seller);
        },
    },
    methods: {
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
        },
        confirmEdit(item) {
            if (item.newQuantity !== item.quantity) {
                item.quantity = item.newQuantity;
            }
            item.editing = false;
            item.newQuantity = 0;
            //submit ke be
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
            console.log(`Checking out ${selectedSeller.name}`);
            console.log(this.groupedCart)
        },
    },
    props: {
        userdata: {
            type: Object,
            required: true
        }
    },
    mounted() {
        const grouped = {};
        //nambah cart id nanti disini
        for (const { seller, product } of this.cart) {
            if (!grouped[seller.id]) {
                grouped[seller.id] = { seller, items: [], selected: false };
            }
            grouped[seller.id].items.push({ ...product, editing: false, newQuantity: 0 });
        }
        this.groupedCart = Object.values(grouped);

         console.log(this.userdata.id)
    },
};
</script>