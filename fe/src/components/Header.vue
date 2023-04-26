<template>
    <v-toolbar flat max-width="auto">
      <v-toolbar-title @click="$router.push('/customerhome/')">Spider</v-toolbar-title>
    <!-- mau dibikin ada text searchnya dan bkn button -->
    <!-- <v-spacer></v-spacer> -->
      <!-- <v-btn icon width="auto">
        <div class="pa-5 rounded-pill">
          <v-icon>mdi-magnify</v-icon>
          Search
        </div>
        
      </v-btn> -->
      
      <v-spacer></v-spacer>
      <v-btn icon @click="$router.push('/customerfavorite/')" v-if="user.role==='Customer'">
        <v-icon>mdi-heart-outline</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn icon @click="$router.push('/customercart/')" v-if="user.role==='Customer'">
        <v-icon>mdi-cart-outline</v-icon>
      </v-btn>

      <v-btn icon @click="$router.push('/customerprofile/')" v-if="user.role==='Customer'">
        <v-icon>mdi-account-outline</v-icon>
      </v-btn>

      <v-btn icon @click="setLogOut" v-if="user">
        <v-icon>mdi-logout</v-icon>
      </v-btn>

    </v-toolbar>
</template>

<style scoped>
    .bgcolor {
        background-color:white;
    }
</style>

<script>
import { mapActions } from 'vuex'
import crypto from '@/plugins/crypto'
export default {
    name: 'Header',
    mixins: [crypto],
    data(){
      return{
        user:'',
      }
    },
    created(){
      var localS = localStorage.getItem('encryptedData')
      if(localS){
        this.user = this.decryptLocalStorage(localS)
      }
      else{
        this.user=''
      }
    },
    methods:{
      ...mapActions("login", ["logOut"]),
      setLogOut(){
        this.logOut().then(()=>{
          localStorage.clear()
          this.$router.push({name:"Login"})
        })
      },
      checkLogin(){
        var localS = localStorage.getItem('encryptedData')
        if(localS){
          this.user = this.decryptLocalStorage(localS)
        }
        else{
          this.user=''
        }
      }
    }
}
</script>