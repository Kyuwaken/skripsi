<template>
    <v-container>
      <!-- foto produk -->
      <v-row>
        <!-- foto produk -->
        <v-col>
          <v-card>
            <v-img src="https://picsum.photos/id/11/500/300"></v-img>
          </v-card>
        </v-col>
  
        <!-- harga, nama, wishlist, dll -->
        <v-col>
          <v-btn color="pink" icon @click="toggleWishlist()">
            <v-icon>
              {{ itemIsInWishlist ? "mdi-heart" : "mdi-heart-outline" }}
            </v-icon>
          </v-btn>
  
          <h1>{{ itemName }}</h1>
          <h3>Rp 100.000,-</h3>
  
          <v-rating
            readonly
            length="5"
            :value="item.rating"
            color="yellow"
          ></v-rating>
  
          <v-btn color="primary" rounded v-if="!item.isInCart" @click="addToCart">
            <v-icon left>mdi-cart</v-icon>
            Add to Cart
          </v-btn>
  
        </v-col>
      </v-row>
  
      <!-- deksirpsi panajng -->
      <v-row>
        <v-col>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header> Description </v-expansion-panel-header>
              <v-expansion-panel-content>
                {{ itemDescription }}
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
  
      <!-- review -->
      <v-row>
        <v-col>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header> Reviews </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-list>
                  <v-list-item v-for="(review, i) in item.reviews" :key="i">
                    <v-list-item-content>
                      <v-row no-gutters class="grey--text">
                        <small>
                          {{ reviewUsername }}
                        </small>
  
                        <v-spacer></v-spacer>
  
                        <v-rating
                          readonly
                          length="5"
                          size="16"
                          :value="review.rating"
                          color="yellow"
                        ></v-rating>
                      </v-row>
                      <v-row no-gutters>
                        {{ reviewContent }}
                      </v-row>
  
                      <v-row no-gutters>
                        <v-divider></v-divider>
                      </v-row>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
  
        <!-- ini valid -->
        <!-- <CustomReview>
        </CustomReview> -->
  
        <!-- ini juga valid -->
        <!-- <custom-review>
        </custom-review> -->
      </v-row>
  
    </v-container>
  </template>
  
  <script>
  // import CustomReview from "asdlkfjahsdlfj"
//   import { mapState, mapActions, mapGetters, mapMutations } from "vuex";

  
  export default {
    data:() => ({
        itemName : "Water Bottle",
        itemDescription: "very nice",
        itemIsInWishlist: "",
      item: [
        {
            // name:"Water Bottle",
            // description: "very nice",
            // review: [
            //     {
            //         reviewUsername: "Elbert",
            //         reviewContent: "Top"
            //     },
            //     {
            //         reviewUsername: "Elbertss",
            //         reviewContent: "Topssss"
            //     },
            // ]
        }
      ]
    }),
    toggleWishlist(){

    },


  };
  </script>
  
  