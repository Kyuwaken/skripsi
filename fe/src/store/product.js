import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    CREATE_PRODUCT_WITH_IMAGE: "/product/create-product-with-image/",
};

const product = {
    namespaced: true,
    state: {
        productData: {
            productPhoto: [],
            name: "",
            category: "",
            price: null,
            preorderTime: null,
            productDescription: "",
            seller: "2",
        },
    },
    mutations: {
        SET_PRODUCT_DATA(state, productData) {
            state.productData = productData;
        },
    },
    actions: {
        postProductData({ commit }, productData) {
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.CREATE_PRODUCT_WITH_IMAGE, productData)
                    .then((response) => {
                        commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },
    },
};

export default product;