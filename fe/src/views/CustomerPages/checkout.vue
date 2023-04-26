<template>
    <v-container class="mx-auto" max-width="600">
        <v-card class="my-4">
            <v-card-title class="headline">Address</v-card-title>
            <v-card-text>
                <v-form ref="addressForm">

                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="address" label="Address" required></v-text-field>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="city" label="City" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="state" label="State" required></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="postalCode" label="Postal Code" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="country" label="Country" required></v-text-field>
                        </v-col>
                    </v-row>
                </v-form>
            </v-card-text>
        </v-card>

        <v-card class="my-4">
            <v-card-title class="headline">Products</v-card-title>
            <v-list>
                <v-list-item v-for="(product, index) in products" :key="index">
                    <v-list-item-content>
                        <v-list-item-title>{{ product.name }}</v-list-item-title>
                        <v-list-item-subtitle>Price: {{ formatPrice(product.price) }}</v-list-item-subtitle>
                        <v-list-item-subtitle>Quantity: {{ product.quantity }}</v-list-item-subtitle>
                        <v-list-item-subtitle>Subtotal: {{ formatPrice(product.price * product.quantity) }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card>

        <v-card class="my-4">
            <v-card-title class="headline">Price Calculation</v-card-title>
            <v-card-text>
                <div>Total: {{ formatPrice(total) }}</div>
                <div>DownPayment (30%): {{ formatPrice(downPayment) }}</div>
            </v-card-text>
        </v-card>

        <v-card class="my-4">
            <v-card-title class="headline">Select Payment Method</v-card-title>
            <v-card-text>
                <v-radio-group v-model="selectedPayment">
                    <v-radio v-for="(payment, index) in paymentOptions" :key="index" :label="payment.name"
                        :value="payment.id"></v-radio>
                </v-radio-group>
            </v-card-text>
        </v-card>

        <v-btn color="primary" @click="checkout" class="mt-4">Checkout</v-btn>
    </v-container>
</template>

<script>
import Swal from "sweetalert2";
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
    mounted() {
        this.fetchCartById({ id: this.userdata.id }).then(() => {

            console.log("tempcart", this.cart)
            for (const { product, quantity } of this.cart) {
                console.log(product.seller.id, localStorage.getItem('checkoutSellerId'))
                if (product.seller.id == localStorage.getItem('checkoutSellerId')) {
                    console.log('masuk if')
                    this.products.push({ ...product, quantity: quantity })
                }
            }
            console.log(this.products)
        })
    },
    data() {
        return {
                address: '',
                city: '',
                state: '',
                postalCode: '',
                country: '',
            products: [],
            selectedPayment: '',
            paymentOptions: [
                { id: 1, name: 'ovo' },
                { id: 2, name: 'gopay' },
                { id: 3, name: 'debit' }
            ],
            // showPopup: false,
            // paid: false,
        };
    },
    props: {
        userdata: {
            type: Object,
            required: true
        }
    },
    computed: {
        ...mapState("cart", ["cart"]),
        total() {
            let total = this.products.reduce((total, product) => {
                return total + (product.price * product.quantity);
            }, 0);
            return Math.round(total);
        },
        downPayment() {
            let dp = this.total * 0.3;
            return Math.round(dp);
        },

    },
    methods: {
        ...mapActions("cart", ["fetchCartById"]),

        formatPrice(price) {
            return price.toLocaleString("id-ID", {
                style: "currency",
                currency: "IDR"
            });
        },

        checkout() {
            if (this.$refs.addressForm.validate()) {
                this.showPopup()
            }
        },
        showPopup() {
            // const now = new Date();
            // const deadline = new Date(now.getTime() + 60 * 60 * 1000);
            // const deadlineText = `Please complete your payment before ${deadline.toLocaleString()}`;
            const deadlineText = `Please complete your payment`;

            Swal.fire({
                title: "Payment",
                text: deadlineText,
                icon: "info",
                button: "checkout",
                closeOnClickOutside: false,
                closeOnEsc: false,
                timerProgressBar: true,
                showCancelButton: true,
                cancelButtonText: "Cancel",
                confirmButtonText: "Already Paid",
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    return new Promise((resolve) => {
                        Swal.showLoading();
                        setTimeout(() => {
                            resolve();
                        }, 3000); // Wait for 3 seconds to simulate payment processing
                    });
                },
                allowOutsideClick: false,
                reverseButtons: true
            }).then((result) => {
                if (result.dismiss === Swal.DismissReason.cancel) {
                    Swal.fire({
                        title: "Transaction Cancelled",
                        text: "The transaction has been cancelled",
                        icon: "error",
                        confirmButtonText: "Back to Home",
                        allowOutsideClick: false
                    }).then(() => {
                        this.$router.push('/customerhome')
                    })
                } else {
                    Swal.fire({
                        title: "Payment",
                        text: "Thank you for shopping!",
                        icon: "success",
                        confirmButtonText: "Back to Home",
                        allowOutsideClick: false
                    }).then(() => {
                        //delete

                        //create transaction
                        let product = [];
                        this.products.forEach(item => {
                            product.push({ product_id: item.id, readyAt: item.readyAt.substr(0, 10), productPrice: item.price, quantity: item.quantity })
                        });
                        console.log("checkout ", product)
                        let address = `${this.address}, ${this.city}, ${this.State}, ${this.postalCode}, ${this.country}`
                        let data = {product, payment_method : this.selectedPayment, address: address, nominal: this.downPayment}
                        console.log(data)
                        //this.createTransaction()
                        //this.$router.push('/customerhome')
                    })
                }

            })
                .catch((error) => {
                    // Handle error or do nothing
                });
        }
    },
};
</script>
