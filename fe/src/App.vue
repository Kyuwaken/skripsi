<template>
  <v-app>
    <v-main>
      <router-view
        :baseURL="baseURL"
        :products="products"
        :userdata="tes"
      >
      </router-view>
    </v-main>
  </v-app>
</template>


<script>
import Header from "./components/Header.vue";
import HeaderSeller from "./components/HeaderSeller.vue";
import crypto from '@/plugins/crypto';
export default {
  name: 'App',
  components: {
    Header,
    HeaderSeller
  },
  mixins: [crypto],
  created(){
    this.tes = this.decryptLocalStorage(localStorage.getItem('encryptedData'))
  },

  data() {
    return {
      baseURL : "https://google.com/",
      products: [{"id": "1", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "2", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "3", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}, {"id": "4", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"},{"id": "5", "name": "JORDAN", "description":"ini desc", "price": 15000000, "imageURL":"https://static.nike.com/a/images/t_default/b28a5765-497d-4227-9122-83c46ff7934f/air-jordan-xxxvii-sp-basketball-shoes-P3BjMD.png"}],
      tes: '',
    }
  },

};
</script>
