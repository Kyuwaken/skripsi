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
    actions: {
      fetchCategories({ commit }) {
        return new Promise((resolve, reject) => {
          getAPI(ENDPOINT.CATEGORY)
            .then((response) => {
              const categories = response.data.map((category) => ({
                id: category.id,
                name: category.name,
              }));
              commit("SET_CATEGORIES", categories);
              resolve(categories);
            })
            .catch((error) => {
              reject(error);
            });
        });
      },
    },
  };
  
  export default category;