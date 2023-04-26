<template>
    <v-container>
        <v-toolbar color="white" class="mb-4">
            <v-btn icon @click="$router.push('/sellerprofile')">
                <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
            <v-toolbar-title>Add Product Form</v-toolbar-title>
        </v-toolbar>
        <v-form ref="form" @submit.prevent="handleSubmit">
            <vue-upload-multiple-image @upload-success="uploadImageSuccess" @edit-image="editImage"
                @mark-is-primary="markIsPrimary" @limit-exceeded="limitExceeded" @before-remove="beforeRemove"
                id-upload="myIdUpload" id-edit="myIdEdit" :max-image=20 primary-text="Default"
                browse-text="Browse picture(s)" drag-text="Drag pictures" mark-is-primary-text="Set as default"
                popup-text="This image will be displayed as default" :multiple=true :show-edit=true :show-delete=true
                :show-add=true>
            </vue-upload-multiple-image>
            <v-text-field v-model="name" label="Product Name" required></v-text-field>
            <v-textarea v-model="productDescription" label="Product Description" required></v-textarea>
            <v-text-field v-model="price" label="Product Price" type="number" :hint="formattedPrice" persistent-hint
                required />
            <v-menu v-model="readyAtMenu" :close-on-content-click="true" :nudge-right="40" transition="scale-transition"
                offset-y min-width="290px">
                <template v-slot:activator="{ on }">
                    <v-text-field v-model="readyAt" label="Ready At" prepend-icon="mdi-calendar" readonly v-on="on"
                        required></v-text-field>
                </template>
                <v-date-picker v-model="readyAt" no-title scrollable>
                </v-date-picker>
            </v-menu>
            <v-select v-model="category" :items=categories item-text="name" item-title="name" item-value="id"
                label="Category" return-object required></v-select>
            <v-layout justify-end align-end>
                <v-btn type="submit" color="primary">Submit</v-btn>
            </v-layout>
        </v-form>
    </v-container>
</template>
  
<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Swal from 'sweetalert2';
import VueUploadMultipleImage from '@/components/vue-upload-multiple-image.vue';
import Header from "../../components/Header.vue";
export default {
    computed: {
        ...mapState("category", ['categories']),
        formattedPrice() {
            const price = parseFloat(this.price);
            if (!isNaN(price)) {
                return price.toLocaleString("id-ID", {
                    style: "currency",
                    currency: "IDR",
                });
            } else {
                return "";
            }
        },
    },
    components: {
        VueUploadMultipleImage,
        Header
    },
    data() {
        return {
            name: '',
            productDescription: '',
            price: null,
            productPhoto: [],
            category: '',
            readyAt: null,
            readyAtMenu: false,
            displayPrice: null,
            newProductPhoto:[],
        }
    },
    mounted() {
        //console.log("masuk mounted")
        this.fetchCategories();
    },
    methods: {
        ...mapActions("category", ["fetchCategories"]),
        ...mapActions('product', ['postProductData']),

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
            if (!this.readyAt) {
                Swal.fire({
                    icon: 'error',
                    title: 'Ready At date field is empty',
                    text: 'Please fill out the Ready At field.'
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
                readyAt: this.readyAt,
                productPhoto: this.productPhoto,
                category: this.category.id
            });

            this.productPhoto.forEach(photo => {
                if (!('size' in photo)) {
                    const imageData = photo.path;
                    const splitData1 = imageData.split('data:');
                    const imageType1 = splitData1[1].split(';')[0]; // get the image type (e.g. jpeg, png, etc.)
                    const splitData2 = imageData.split('data:image/');
                    const imageType2 = splitData2[1].split(';')[0];
                    const base64String = imageData.split(',')[1];
                    const binaryString = atob(base64String);
                    const arrayBuffer = new ArrayBuffer(binaryString.length);
                    const uint8Array = new Uint8Array(arrayBuffer);
                    for (let i = 0; i < binaryString.length; i++) {
                        uint8Array[i] = binaryString.charCodeAt(i);
                    }
                    const blob = new Blob([uint8Array], { type: imageType1 });
                    const filename = "image." + imageType2;
                    const fileSize = blob.size;

                    // Create a new File object from the Blob
                    const file = new File([blob], filename, { type: imageType1 });
                    const fileName = file.name;

                    // Add the file to the form data
                    this.newProductPhoto.push(file);
                }
                else {

                    //console.log("di looping productphoto else", photo)
                    this.newProductPhoto.push(photo)
                }
            });

            this.postProductData({
                name: this.name,
                productDescription: this.productDescription,
                price: this.price,
                readyAt: this.readyAt,
                category: this.category.id,
                productPhoto: this.newProductPhoto
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
            this.$router.push({ path: "/sellerprofile" })
        },
        uploadImageSuccess(formData, index, fileList, imageList) {
            console.log('data', formData, index, 'file', fileList, 'image', imageList)
            this.productPhoto = imageList
            // Upload image api
            // axios.post('http://your-url-upload', formData).then(response => {
            //   console.log(response)
            // })
        },
        beforeRemove(index, removeCallBack, imageList) {
            console.log('index', index)
            var r = confirm("remove image")
            if (r == true) {
                removeCallBack()
            }
            this.productPhoto = imageList
        },
        editImage(formData, index, fileList, imageList) {
            console.log('edit data', formData, index, fileList)
            this.productPhoto = imageList
        },
        markIsPrimary(index, fileList) {
            console.log('markIsPrimary data', index, fileList)
        },
        limitExceeded(amount) {
            console.log('limitExceeded data', amount)
        }
    },
    watch: {
        price(val) {
            //this.getFormattedPrice(val)
        }
    }
}
</script>
  