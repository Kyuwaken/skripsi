<template>
    <v-container>
        <v-row>
            <v-carousel cycle height="400" hide-delimiter-background show-arrows="hover" class="rounded-lg ma-3">
                <v-carousel-item v-for="(slide, i) in slides" :key="i">
                    <v-sheet :color="colors[i]" height="100%">
                        <div class="d-flex fill-height justify-center align-center">
                            <div class="text-h2">
                                {{ slide }} Slide
                            </div>
                        </div>
                    </v-sheet>
                </v-carousel-item>
            </v-carousel>
        </v-row>
        <v-row>
            <v-col cols="6">
                <v-sheet outlined color="white" elevation="2" rounded="lg">
                    <v-container fluid>
                        <v-row no-gutters class="ma-2">
                            Category
                        </v-row>
                        <v-row>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                            <v-col cols="auto">
                                <v-btn elevation="2" icon tile width="100" height="100">
                                        <v-icon>mdi-tshirt-crew-outline</v-icon>
                                    
                                        Clothes
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-sheet>
            </v-col>
        </v-row>

        <v-divider class="mt-5 mb-5"></v-divider>

        <v-row>
            <v-col cols=12>
                <v-sheet outlined color="white" elevation="5">
                    <v-row class="justify-center mt-4">
                        <h1>You May Like</h1>
                    </v-row>
                    <v-row>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0 mr-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                        <v-col class="ma-7 mt-0">
                            <router-link to="/">
                                <v-img src="https://picsum.photos/200/300/?"></v-img>
                            </router-link>
                        </v-col>
                    </v-row>
                </v-sheet>
            </v-col>
        </v-row>


        <!-- <v-row class="ma-5">
            <v-hover>
                <router-link to="/">
                    <v-img src="https://picsum.photos/200/300/?blur"></v-img>
                </router-link>
            </v-hover>

        </v-row> -->
    </v-container>
</template>

<script>
import ProductBox from "../components/ProductBox.vue";
export default {
    data() {
        return {
            colors: [
                'indigo',
                'warning',
                'pink darken-2',
                'red lighten-1',
                'deep-purple accent-4',
            ],
            slides: [
                'First',
                'Second',
                'Third',
                'Fourth',
                'Fifth',
            ],
        }
    },
    components: { ProductBox },
    props: ["products"]
}
</script>