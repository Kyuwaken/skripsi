import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    COUNTRY: "/country/",
  };
  
  const country = {
    namespaced: true,
    state: {
      countries: [],
    },
    mutations: {
      SET_COUNTRIES(state, countries) {
        state.countries = countries;
      },
    },
    getters: {
      getCountry: state => {
        return state.countries
      }
    },
    actions: {
      fetchCountries({ commit }) {
        return new Promise((resolve, reject) => {
          getAPI(ENDPOINT.COUNTRY)
            .then((response) => {
              console.log("masuk js country")
              // const countries = response.data.map((country) => ({
              //   id: country.id,
              //   name: country.name,
              // }));
              console.log(response.data)
              commit("SET_COUNTRIES", response.data);
              resolve(response);
            })
            .catch((error) => {
              reject(error);
            });
        });
      },
    },
  };
  
  export default country;