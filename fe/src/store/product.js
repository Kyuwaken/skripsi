import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    CREATE_PRODUCT_WITH_IMAGE: "product/create-product-with-image/",
};

const createProduct = {
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
                const formData = new FormData();
                formData.append("productPhoto", productData.images);
                formData.append("name", productData.name);
                formData.append("category", productData.category);
                formData.append("price", productData.price);
                formData.append("preorderTime", productData.preOrderTime);
                formData.append("productDescription", productData.description);
                formData.append("seller", productData.seller);

                getAPI
                    .post(ENDPOINT.CREATE_PRODUCT_WITH_IMAGE, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        },
                    })
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

export default createProduct;