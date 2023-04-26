<template>
    <v-app>
        <v-app-bar app color="white" flat>
            <Header></Header>
        </v-app-bar>
        <v-container fluid>
            <v-form>
                <v-row justify="center">
                    <v-col cols="12" md="6">
                        <v-text-field v-model="searchTerm" label="Search Item" @input="searchProducts"></v-text-field>
                    </v-col>
                </v-row>
            </v-form>
            <v-divider></v-divider>
            <v-main>
                <v-container>
                    <v-row cols="12" class="mt-4" v-if="searchedProductData.length > 0">
                        <v-col v-for="product in searchedProductData" :key="product.id" cols="12" sm="6" md="4" lg="3">
                            <ProductHome @add-to-cart="addToCart" :product="product" />
                        </v-col>
                    </v-row>
                    <v-row cols="12" class="mt-4" v-else>
                        <v-col cols="12" class="text-center">
                            <p>No products found</p>
                        </v-col>
                    </v-row>
                </v-container>
            </v-main>
            <!-- <div v-for="product in filteredProducts" :key="product.id">
                {{ product.productName }}, {{ product.productCategory }}
        </div> -->
            <!-- <v-data-table
          :headers="headers"
          :items="filteredProducts"
          :search="search"
        >
          <template v-slot:item.actions="{ item }">
            <v-btn small color="primary" @click="viewProductDetails(item)">
              View Details
            </v-btn>
          </template>
        </v-data-table> -->
        </v-container>
    </v-app>
</template>
  
<script>
import { mapActions, mapState } from 'vuex';
import Header from "../../components/Header.vue";
import ProductHome from "@/components/ProductHome.vue";
export default {
    data() {
        return {
            searchTerm: '',
            searchedProductData: [],
        };
    },
    components: {
        Header,
        ProductHome,
    },
    computed: {
        ...mapState("product", ["productData"]),
        search() {
            // Fungsi untuk melakukan pencarian berdasarkan kategori atau nama produk
            return this.products.filter(product => {
                if (this.searchBy === 'Category') {
                    return product.category.toLowerCase().includes(this.searchTerm.toLowerCase());
                } else {
                    return product.name.toLowerCase().includes(this.searchTerm.toLowerCase());
                }
            });
        },
        filteredProducts() {
            // Fungsi untuk melakukan pengurutan data produk berdasarkan nama produk
            return this.search.sort((a, b) => {
                const nameA = a.name.toLowerCase();
                const nameB = b.name.toLowerCase();
                if (nameA < nameB) return -1;
                if (nameA > nameB) return 1;
                return 0;
            });
        }
    },
    methods: {
        ...mapActions("product", ["fetchProduct", "fetchProductbySeller"]),
        ...mapActions("cart", ["postCart"]),
        searchProducts() {
            if (!this.searchTerm) {
                this.searchedProductData = this.productData
            } else {
                this.searchedProductData = this.productData.filter((product) => {
                    const productName = product.name.toLowerCase();
                    const productDescription = product.productDescription.toLowerCase();
                    return productName.includes(this.searchTerm.toLowerCase()) || productDescription.includes(this.searchTerm.toLowerCase());
                });
            }

            console.log("searched", this.searchedProductData)
        },
        addToCart(productId) {
            var user = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
            this.postCart({ product: productId, user: user.id })
        },
    },
    mounted() {
        // Panggil fungsi fetchProducts saat komponen dimounted
        //this.fetchProducts().then(()=>{
        //     this.searchTerm = localStorage.getItem('searchedValue')
        //     this.searchProducts()
        // });
        let data = { "id": "2" }
        this.fetchProductbySeller(data).then(() => {
            this.searchTerm = localStorage.getItem('searchedValue')
            localStorage.removeItem('searchedValue')
            this.searchProducts()
        })

    }
};
</script>
  
<style scoped>
/* Gaya khusus untuk komponen ini */
</style>