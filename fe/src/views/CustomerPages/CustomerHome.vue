<template>
  <v-container>
    <v-app-bar app color="white" flat>
      <Header></Header>
    </v-app-bar>
    <v-row>
      <v-col cols="12" class="mb-3">
        <v-text-field
          label="Search"
          solo-inverted
          prepend-inner-icon="mdi-magnify"
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- <v-row>
      <v-col cols="12">
        <v-carousel
          cycle
          height="400"
          hide-delimiter-background
          show-arrows="hover"
          class="rounded-lg ma-3"
        >
          <v-carousel-item v-for="(slide, i) in slides" :key="i">
            <v-sheet :color="colors[i]" height="100%">
              <div class="d-flex fill-height justify-center align-center">
                <div class="text-h2">{{ slide }} Slide</div>
              </div>
            </v-sheet>
          </v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row> -->
    <v-row>
      <v-col cols="12" class="d-flex justify-center">
        <v-btn-toggle v-model="selectedCategory" mandatory>
          <v-btn
            v-for="(category, index) in categories"
            :key="index"
            :value="category"
            @click="getByCategory(category)"
          >
            <v-icon>{{ category.icon }}</v-icon>
            {{ category.name }}
          </v-btn>
        </v-btn-toggle>
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col cols="12">
        <v-sheet outlined color="white" elevation="2" rounded="lg">
          <v-container fluid>
            <v-row no-gutters class="ma-2"> Category </v-row>
            <v-row>
              <v-col cols="auto">
                <v-btn elevation="2" icon tile width="100" height="100">
                  <v-icon>mdi-tshirt-crew-outline</v-icon>

                  Clothes
                </v-btn>
              </v-col>
              <v-col cols="auto">
                <v-btn elevation="2" icon tile width="100" height="100">
                  <v-icon>mdi-shoe-sneaker</v-icon>

                  Shoes
                </v-btn>
              </v-col>
              <v-col cols="auto">
                <v-btn elevation="2" icon tile width="100" height="100">
                  <v-icon>mdi-home-lightbulb</v-icon>

                  Houseware
                </v-btn>
              </v-col>
              <v-col cols="auto">
                <v-btn elevation="2" icon tile width="100" height="100">
                  <v-icon>mdi-food-outline</v-icon>

                  Food & Baverage
                </v-btn>
              </v-col>
              <v-col cols="auto">
                <v-btn elevation="2" icon tile width="100" height="100">
                  <v-icon>mdi-dots-horizontal-circle-outline</v-icon>

                  Others
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-sheet>
      </v-col>
    </v-row> -->

    <v-divider class="mt-5 mb-5"></v-divider>

    <v-row cols="12" class="mt-4" v-if="productData.length > 0">
      <v-col
        v-for="product in productData"
        :key="product.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <ProductHome @add-to-cart="addToCart" :product="product" />
      </v-col>
    </v-row>
  </v-container>
</template>
  
  <script>
import { mapState, mapActions } from "vuex";
import ProductHome from "@/components/ProductHome.vue";
import crypto from "@/plugins/crypto";
import Header from "../../components/Header.vue";
export default {
  computed: {
    ...mapState("category", ["categories"]),
    ...mapState("product", ["productData"]),
  },
  data() {
    return {
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4",
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      search: "",
      reloaded: false,
      categories: [
        {
          id: 0,
          name: "All",
        },
        {
          id: 1,
          name: "Clothes",
          icon: "mdi-tshirt-crew-outline",
        },
        {
          id: 2,
          name: "Shoes",
          icon: "mdi-shoe-sneaker",
        },
        {
          id: 3,
          name: "Electronics",
          icon: "mdi-devices",
        },
        {
          id: 4,
          name: "Houseware",
          icon: "mdi-home-lightbulb",
        },
        {
          id: 5,
          name: "Food & Baverage",
          icon: "mdi-food-outline",
        },
        {
          id: 6,
          name: "Others",
          icon: "mdi-dots-horizontal-circle-outline",
        },
      ],
    };
  },
  mixins: [crypto],
  props: {
    userdata: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    //console.log("masuk mounted")
    this.fetchProduct();
    this.fetchCategories();
    if (!this.reloaded) {
      console.log(this.reloaded);

      //location.reload();
      this.reloaded = true;
      console.log(this.reloaded);
    }
  },
  methods: {
    ...mapActions("category", ["fetchCategories"]),
    ...mapActions("product", ["fetchProduct","fetchProductbyCategory"]),
    ...mapActions("cart", ["postCart"]),
    addToCart(productId) {
      var user = this.decryptLocalStorage(
        localStorage.getItem("encryptedData")
      );
      this.postCart({ product: productId, user: user.id });
    },
    getByCategory(category){
        if(category.id === 0){
            this.fetchProduct();
        }
        else{
            this.fetchProductbyCategory({id:category.id})
        }
        console.log(category)
    }
  },
  components: { ProductHome, Header },
  props: ["products"],
};
</script>