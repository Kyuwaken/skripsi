<template>
    <v-app>
        <v-container fluid>
            <h1>Product Search</h1>
            <v-form>
                <v-row justify="center">
                    <v-col cols="12" md="6">
                        <v-select v-model="searchBy" :items="searchByOptions" label="Search By"></v-select>
                    </v-col>
                    <v-col cols="12" md="6">
                        <v-text-field v-model="searchTerm" label="Cari di Spider"
                            @input="handleSearchTermChange"></v-text-field>
                    </v-col>
                </v-row>
            </v-form>
            <v-divider></v-divider>
            <v-row justify="center" class="pa-6 pt-2">
                <v-col v-for="product in filteredProducts" :key="product.id" cols="12" sm="6" md="4" lg="3">
                    <v-card>
                        <v-img :src="product.image" height="200"></v-img>
                        <v-card-title>{{ product.name }}</v-card-title>
                        <v-card-subtitle>{{ product.price }}</v-card-subtitle>
                        <v-card-text>{{ product.description }}</v-card-text>
                        <v-card-actions>
                            <v-row justify="center" no-gutters>
                                <v-btn color="#F7F1E5" rounded>
                                    <v-icon left>mdi-information-outline</v-icon>
                                    See Details
                                </v-btn>
                                <v-spacer></v-spacer>
                                <v-btn color="#C7E9B0" rounded>
                                    <v-icon left>mdi-cart</v-icon>
                                    Add to Cart
                                </v-btn>
                            </v-row>

                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row> 
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
import axios from 'axios';
import Header from "../../components/Header.vue";
export default {
    data() {
        return {
            searchBy: 'Category',
            searchTerm: '',
            searchByOptions: [
                "Category", "Name"
            ],
            products: [
            {
                id: 1,
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 3.000.000,-",
                description: "Jordan",
                category: "Basketball"
            },
            {
                id: 2,
                image: "https://i.pinimg.com/564x/3e/96/48/3e96480afcda019d088551eb9abe8f37.jpg",
                name: "Nike Zoom X",
                price: "Rp 3.500.000,-",
                description: "Buat lari dari kenyataan",
                category: "Running"
            },
            {
                id: 3,
                image: "https://i.pinimg.com/564x/70/db/68/70db68ef1b031823da5466a6364c4174.jpg",
                name: "Adidas Tennis Sabalo",
                price: "Rp 800.000,-",
                description: "Mahal dah bos",
                category: "Fashion"
            },
            {
                id: 4,
                image: "https://i.pinimg.com/564x/da/75/d4/da75d4a493593798c4b817349ac20e14.jpg",
                name: "White Skate Shoes",
                price: "Rp 2.000.000,-",
                description: "Skating bos",
                category: "Skate"
            },
            
            ], // Data produk dari API
            // headers: [
            //   { text: 'Product Name', value: 'productName' },
            //   { text: 'Category', value: 'category' },
            //   { text: 'Price', value: 'price' },
            //   { text: 'Actions', value: 'actions', sortable: false }
            // ]
        };
    },
    components: {
    Header,
  },
    computed: {
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
        handleSearchTermChange() {
            // Fungsi untuk mereset input pencarian ketika pilihan "By Category" atau "By Name" berubah
            this.searchTerm = this.searchTerm;
        },
        viewProductDetails(product) {
            // Fungsi untuk menampilkan detail produk
            // Lakukan aksi yang diinginkan
        },
        //   fetchProducts() {
        //     // Fungsi untuk mengambil data produk dari API menggunakan Axios
        //     axios.get('/api/products')
        //       .then(response => {
        //         this.products = response.data;
        //       })
        //       .catch(error => {
        //         console.error(error);
        //       });
        //   }
    },
    mounted() {
        // Panggil fungsi fetchProducts saat komponen dimounted
        //   this.fetchProducts();
    }
};
</script>
  
<style scoped>
/* Gaya khusus untuk komponen ini */
</style>