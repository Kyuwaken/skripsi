<template>
  <v-app>
    <!-- <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar> -->

    <v-main>
      <router-view
        :baseURL="baseURL"
        :categories="categories"
        :products="products"
      >
      </router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data() {
    return {
      baseURL : "https://google.com/",
      products: [{"id": "1", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "2", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "3", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "4", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"},{"id": "5", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}]
    }
  },
};
</script>
