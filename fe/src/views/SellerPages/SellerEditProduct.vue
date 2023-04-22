<template>
    <v-container>
        <v-toolbar color="white" class="mb-4">
            <v-btn icon @click="$router.push('/sellerprofile')">
                <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
            <v-toolbar-title>Edit Product Form</v-toolbar-title>
        </v-toolbar>
        <v-form ref="form" @submit.prevent="handleSubmit">
            <vue-upload-multiple-image :dataImages = "productPhoto" @upload-success="uploadImageSuccess" @edit-image="editImage"
                @mark-is-primary="markIsPrimary" @limit-exceeded="limitExceeded" @before-remove="beforeRemove"
                id-upload="myIdUpload" id-edit="myIdEdit" :max-image=20 primary-text="Default"
                browse-text="Browse picture(s)" drag-text="Drag pictures" mark-is-primary-text="Set as default"
                popup-text="This image will be displayed as default" :multiple=true
                :show-edit=true :show-delete=true :show-add=true>
            </vue-upload-multiple-image>
            <v-text-field v-model="name" label="Product Name" :rules="[requiredRule]" required></v-text-field>
            <v-textarea v-model="productDescription" label="Product Description" :rules="[requiredRule]"
                required></v-textarea>
            <v-text-field v-model.number="price" label="Product Price" :rules="[requiredRule, numericRule]"
                required></v-text-field>
            <v-text-field v-model.number="preorderTime" label="Pre-Order Time (in days)"
                :rules="[requiredRule, numericRule]" required></v-text-field>
            <v-select v-model="category" :items="categories" item-text="name" item-title="name" item-value="id"
                label="Category" return-object :rules="[requiredRule]" required></v-select>
            <v-file-input v-model="productPhoto" accept="image/*" label="Product Images" multiple></v-file-input>
            <v-layout justify-end align-end>
                <v-btn type="submit" color="primary">Submit</v-btn>
            </v-layout>
        </v-form>
    </v-container>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Swal from "sweetalert2";
import VueUploadMultipleImage from '@/components/vue-upload-multiple-image.vue';

export default {
    computed: {
        ...mapState("category", ["categories"]),
        ...mapState("product", ["productData"]),
    },
    data() {
        return {
            name: "",
            productDescription: "",
            price: "",
            preorderTime: "",
            productPhoto: [],
            category: "",
            requiredRule: [v => !!v || "Field is required"],
            numericRule: [v => /^\d+$/.test(v) || "Input must be a number"],
        };
    },
    components: {
        VueUploadMultipleImage,
    },
    created() {
        const id = this.$route.params.id;
        this.fetchProductbyId(id);
    },
    methods: {
        ...mapActions("category", ["fetchCategories"]),
        ...mapActions("product", ["updateProductData", "fetchProductbyId"]),
        handleSubmit() {
            // Validate form data here
            console.log(this.category)
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
            // console.log({
            //     name: this.name,
            //     description: this.productDescription,
            //     price: this.price,
            //     preOrderTime: this.preorderTime,
            //     productPhoto: this.productPhoto,
            //     category: this.category.id
            // });



            this.postProductData({
                name: this.name,
                productDescription: this.productDescription,
                price: this.price,
                preorderTime: this.preorderTime,
                category: this.category.id,
                productPhoto: this.productPhoto
            }).then(() => {
                // Success message
                Swal.fire({
                    icon: 'success',
                    title: 'Product added successfully',
                    text: 'Your product has been added to the store.'
                })
                // Reset form data
                this.name = ''
                this.productDescription = ''
                this.price = ''
                this.preorderTime = ''
                this.category = ''
                this.productPhoto = []

                this.$router.push({ path: "/sellerprofile" })
            }).catch((error) => {
                // Error message
                Swal.fire({
                    icon: 'error',
                    title: 'Error adding product',
                    text: error.message || 'An unknown error occurred.'
                })
                this.name = ''
                this.productDescription = ''
                this.price = ''
                this.preorderTime = ''
                this.category = ''
                this.productPhoto = []
            })
        },
        uploadImageSuccess(formData, index, fileList) {
            console.log('data', formData, index, fileList)
            // Upload image api
            // axios.post('http://your-url-upload', formData).then(response => {
            //   console.log(response)
            // })
        },
        beforeRemove(index, removeCallBack) {
            console.log('index', index)
            var r = confirm("remove image")
            if (r == true) {
                removeCallBack()
            }
        },
        editImage(formData, index, fileList) {
            console.log('edit data', formData, index, fileList)
        },
        markIsPrimary(index, fileList) {
            console.log('markIsPrimary data', index, fileList)
        },
        limitExceeded(amount) {
            console.log('limitExceeded data', amount)
        }
    },
    watch: {
        productData(productData) {
            this.name = productData.name;
            this.productDescription = productData.productDescription;
            this.price = productData.price;
            this.preorderTime = productData.preorderTime;
            this.productPhoto = productData.productPhoto;
            this.category = productData.category;
        }
    }
}

</script>