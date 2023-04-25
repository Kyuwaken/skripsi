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
      fetchCartById({ commit }, body) {
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.CART + 'user/', body)
                .then((response) => {
                    console.log(response.data)
                    commit("SET_CART", response.data);
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
      updateQuantity({commit}, body){
        let id = body.id
        delete body.id
        console.log("di cart js",body)
        return new Promise((resolve, reject) => {
          getAPI
                .patch(ENDPOINT.CART + id + '/', body)
                .then((response)=>{
                    resolve(response.data);
                })
                .catch((error)=>{
                    reject(error);
                })
        })
      },
      deleteCart({commit}, body){
        return new Promise((resolve, reject) => {
          getAPI
                .delete(ENDPOINT.CART + body + '/')
                .then((response)=>{
                    resolve(response.data);
                })
                .catch((error)=>{
                    reject(error);
                })
        })
      }
    },
  };
  
  export default cart;