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
        },
    },
    mutations: {
        SET_PRODUCT_DATA(state, productData) {
            state.productData = productData;
        },
    },
    actions: {
        postProductData({ commit }, productData) {
            let formData = new FormData();
            formData.append('name', productData.name);
            formData.append('productDescription', productData.productDescription);
            formData.append('price', productData.price);
            formData.append('preorderTime', productData.preorderTime);
            formData.append('category', productData.category);
            productData.productPhoto.forEach(photo => {
                formData.append('productPhoto', photo, photo.name);
            });
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.CREATE_PRODUCT_WITH_IMAGE, formData)
                    .then((response) => {
                        //commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },

        fetchProductbySeller({commit}, )
    },
};

export default product;