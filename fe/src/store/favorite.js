import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    FAVORITE: "/favorite/",
  };
  
  const favorite = {
    namespaced: true,
    state: {
      favorite: [],
    },
    mutations: {
      SET_FAVORITE(state, favorite) {
        state.favorite = favorite;
      },
    },
    getters: {
      getFavorite: state => {
        return state.favorite
      }
    },
    actions: {
      fetchFavoriteById({ commit }, body) {
        return new Promise((resolve, reject) => {
            getAPI
                .post(ENDPOINT.FAVORITE + 'user/', body)
                .then((response) => {
                    console.log(response.data)
                    commit("SET_FAVORITE", response.data);
                    resolve(response.data);
                })
                .catch((error) => {
                    reject(error);
                });
        });
      },
      // removeToFavorite({commit},body){
      //   return new Promise((resolve, reject) => {
      //       getAPI
      //           .post(ENDPOINT.FAVORITE + 'remove/',body)
      //           .then((response)=>{
      //               resolve(response.data);
      //           })
      //           .catch((error)=>{
      //               reject(error);
      //           })
      //   })
      // },
    },
  };
  
  export default favorite;