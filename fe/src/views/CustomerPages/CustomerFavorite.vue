<template>
    <v-container fluid>
        <v-row justify="center">
            <v-col cols="12">
                <v-card>
                    <v-card-title>
                        <h1 class="text-center">Favorite</h1>
                    </v-card-title>
                    <v-row justify="center" class="pa-6 pt-2">
                        <v-col v-for="(product, index) in products" :key="index" cols="12" sm="6" md="4" lg="3">
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
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        products: [
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
            {
                image: "https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png",
                name: "Air Jordan",
                price: "Rp 100.000.000,-",
                description: "Mahal dah bos"
            },
        ],

    }),
    created() {
        axios.get('/api/products')
            .then(response => {
                this.products = response.data;
            })
            .catch(error => {
                console.log(error);
            })
    }
}
</script>