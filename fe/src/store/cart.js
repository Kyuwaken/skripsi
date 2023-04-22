import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    CART: "/cart/",
  };
  
  const cart = {
    namespaced: true,
    state: {
      cart: [],
    },
    mutations: {
      SET_CART(state, cart) {
        state.cart = cart;
      },
    },
    getters: {
      getCart: state => {
        return state.cart
      }
    },
    actions: {
      fetchCartById({ commit }, customerId) {
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.CART + 'user/', customerId)
                .then((response) => {
                    commit("SET_PRODUCT_DATA", response.data);
                    resolve(response.data);
                })
                .catch((error) => {
                    reject(error);
                });
        });
      },
      postCart({commit},body){
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.CART,body)
                .then((response)=>{
                    resolve(response.data);
                })
                .catch((error)=>{
                    reject(error);
                })
        })
      },
      decreaseCart({commit},body){
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.CART + 'decrease-quantity/',body)
                .then((response)=>{
                    resolve(response.data);
                })
                .catch((error)=>{
                    reject(error);
                })
        })
      },
      customCart({commit},body){
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.CART + 'custom-quantity/',body)
                .then((response)=>{
                    resolve(response.data);
                })
                .catch((error)=>{
                    reject(error);
                })
        })
      },
    },
  };
  
  export default cart;