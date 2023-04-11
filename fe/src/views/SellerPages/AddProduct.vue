<template>
    <v-container>
        <v-toolbar color="white" class="mb-4">
            <v-btn icon @click="$router.push('/sellerprofile')">
                <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
            <v-toolbar-title>Add Product Form</v-toolbar-title>
        </v-toolbar>
        <v-form ref="form" @submit.prevent="handleSubmit">
            <v-text-field v-model="name" label="Product Name" :rules="[requiredRule]" required></v-text-field>
            <v-textarea v-model="productDescription" label="Product Description" :rules="[requiredRule]"
                required></v-textarea>
            <v-text-field v-model.number="price" label="Product Price" :rules="[requiredRule, numericRule]"
                required></v-text-field>
            <v-text-field v-model.number="preorderTime" label="Pre-Order Time (in days)"
                :rules="[requiredRule, numericRule]" required></v-text-field>
            <v-select v-model="category" :items="categories" label="Category" :rules="[requiredRule]" required></v-select>
            <v-file-input v-model="productPhoto" accept="image/*" label="Product Images" multiple></v-file-input>
            <v-layout justify-end align-end>
                <v-btn type="submit" color="primary">Submit</v-btn>
            </v-layout>
        </v-form>
    </v-container>
</template>
  
<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Swal from 'sweetalert2'

export default {
    created() {
        this.fetchCategories();
    },
    computed: {
        ...mapState("category", ["categories"]),
        // other computed properties for this component
    },
    data() {
        return {
            name: '',
            productDescription: '',
            price: '',
            preorderTime: '',
            productPhoto: [],
            seller: '2',
            category: 'books',
            requiredRule: [v => !!v || 'Field is required'],
            numericRule: [v => /^\d+$/.test(v) || 'Input must be a number']
        }
    },
    methods: {
        ...mapActions("category", ["fetchCategories"]),
        ...mapActions('product', ['postProductData']),
        handleSubmit() {
            // Validate form data here
            if (!this.$refs.form.validate()) {
                Swal.fire({
                    icon: 'error',
                    title: 'Invalid form data',
                    text: 'Please fill out all required fields and ensure that the input is valid.'
                });
                return;
            }
            if (!this.name) {
                Swal.fire({
                    icon: 'error',
                    title: 'Name field is empty',
                    text: 'Please fill out the product name field.'
                });
                return;
            }
            if (!this.productDescription) {
                Swal.fire({
                    icon: 'error',
                    title: 'Description field is empty',
                    text: 'Please fill out the product description field.'
                });
                return;
            }
            if (!this.price) {
                Swal.fire({
                    icon: 'error',
                    title: 'Price field is empty',
                    text: 'Please fill out the product price field.'
                });
                return;
            }
            if (isNaN(this.price)) {
                Swal.fire({
                    icon: 'error',
                    title: 'Invalid input',
                    text: 'Please ensure that the price are filled with numbers.'
                });
                return;
            }
            if (!this.preorderTime) {
                Swal.fire({
                    icon: 'error',
                    title: 'Pre-Order Time field is empty',
                    text: 'Please fill out the pre-order time field.'
                });
                return;
            }
            if (isNaN(this.preorderTime)) {
                Swal.fire({
                    icon: 'error',
                    title: 'Invalid input',
                    text: 'Please ensure that pre-order time fields are filled with numbers.'
                });
                return;
            }
            // Check if the input fields are valid
            if (!this.$refs.form.validate()) {
                Swal.fire({
                    icon: 'error',
                    title: 'Invalid form data',
                    text: 'Please ensure that the input is valid.'
                });
                return;
            }

            // Submit form data here
            console.log({
                name: this.name,
                description: this.productDescription,
                price: this.price,
                preOrderTime: this.preorderTime,
                productPhoto: this.productPhoto,
                category: this.category
            });
            this.postProductData({
                name: this.name,
                productDescription: this.productDescription,
                price: this.price,
                preorderTime: this.preorderTime,
                productPhoto: this.productPhoto,
                seller: this.seller,
                category: this.category
            })//.then(() => {
            //     // Success message
            //     Swal.fire({
            //       icon: 'success',
            //       title: 'Product added successfully',
            //       text: 'Your product has been added to the store.'
            //     })
            //     // Reset form data
            //     this.name = ''
            //     this.description = ''
            //     this.price = null
            //     this.preOrderTime = null
            //     this.images = null
            //   }).catch((error) => {
            //     // Error message
            //     Swal.fire({
            //       icon: 'error',
            //       title: 'Error adding product',
            //       text: error.message || 'An unknown error occurred.'
            //     })
            //   })
        }
    }
}
</script>
  