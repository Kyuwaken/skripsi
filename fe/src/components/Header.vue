<template>
    <v-toolbar flat max-width="auto">
      <v-toolbar-title>Spider</v-toolbar-title>
    <!-- mau dibikin ada text searchnya dan bkn button -->
    <!-- <v-spacer></v-spacer> -->
      <!-- <v-btn icon width="auto">
        <div class="pa-5 rounded-pill">
          <v-icon>mdi-magnify</v-icon>
          Search
        </div>
        
      </v-btn> -->
      
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-heart-outline</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn icon @click="$router.push('/customercart/')">
        <v-icon>mdi-cart-outline</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-account-outline</v-icon>
      </v-btn>

    </v-toolbar>
</template>

<style scoped>
    .bgcolor {
        background-color:white;
    }
</style>

<script>
export default {
    name: 'Header',
    data: () => ({

    }),
}
</script>