<template>
    <v-container>
        <v-btn icon left @click="goBack">
            <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <h1 class="text-center my-6">List of Transactions</h1>
        <v-list class="my-4" style="max-height: 600px; overflow-y: auto;">
            <v-list-item v-for="(transaction, index) in transactions" :key="index" class="mb-16">
                <v-row>
                    <v-col cols="2">
                        <v-img :src="transaction.productPhoto" height="100"></v-img>
                    </v-col>
                    <v-col cols="7">
                        <v-list-item-content>
                            <div class="text-h6">{{ transaction.productName }}</div>
                            <div class="mt-2">Price: {{ transaction.price }}</div>
                            <div>Quantity: {{ transaction.quantity }}
                            function(transaction.transaction_detail)</div>
                        </v-list-item-content>
                        return len(Transaction_detail)
                    </v-col>
                    <v-col>
                        <v-list-item-action>
                            <v-btn class="mt-8" color="primary" @click="goToDetailsPage(transaction)">View Details</v-btn>
                        </v-list-item-action>
                    </v-col>
                </v-row>
                <v-divider ></v-divider>
            </v-list-item>
        </v-list>
    </v-container>
</template>
  
<script>
export default {
    name: 'TransactionList',
    data() {
        return {
            transactions: [
                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 1',
                    price: 10.99,
                    quantity: 1,
                },
                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 2',
                    price: 5.99,
                    quantity: 2,
                },
                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },                {
                    productPhoto: 'https://via.placeholder.com/150',
                    productName: 'Product 3',
                    price: 8.99,
                    quantity: 3,
                },
            ],
        };
    },
    methods: {
        goToDetailsPage(transaction) {
            // Navigate to the transaction details page
        },
        goBack() {
            this.$router.push('/sellerprofile');
        },
    },
};
</script>