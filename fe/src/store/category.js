import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    CATEGORY: "/category",
  };
  
  const category = {
    namespaced: true,
    state: {
      categories: [],
    },
    mutations: {
      SET_CATEGORIES(state, categories) {
        state.categories = categories;
      },
    },
    getters: {
      getCategory: state => {
        return state.categories
      }
    },
    actions: {
      fetchCategories({ commit }) {
        return new Promise((resolve, reject) => {
          getAPI(ENDPOINT.CATEGORY)
            .then((response) => {
              console.log("masuk js category")
              // const categories = response.data.map((category) => ({
              //   id: category.id,
              //   name: category.name,
              // }));
              console.log(response.data)
              commit("SET_CATEGORIES", response.data);
              resolve(response);
            })
            .catch((error) => {
              reject(error);
            });
        });
      },
    },
  };
  
  export default category;