import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    CREATE_PRODUCT_WITH_IMAGE: "/product/create-product-with-image/",
    GET_SELLER_PRODUCT: "/product/seller/",
    GET_ALL_PRODUCT: "/product/",
    GET_CATEGORY_PRODUCT: "product/get-by-category/",
    FAVORITE: "/favorite/"
};

const product = {
    namespaced: true,
    state: {
        productData: [],
    },
    mutations: {
        SET_PRODUCT_DATA(state, productData) {
            console.log("masuk mutataion", productData)
            state.productData = productData;
        },
    },
    actions: {
        postProductData({ commit }, productData) {
            console.log("masuk post product")
           let formData = new FormData();
           formData.append('name', productData.name);
           formData.append('productDescription', productData.productDescription);
           formData.append('price', productData.price);
           formData.append('readyAt', productData.readyAt);
           formData.append('category', productData.category);
           productData.productPhoto.forEach(photo => {
               console.log("product js",photo)
               formData.append('image', photo, photo.name);
           });
           return new Promise((resolve, reject) => {
               getAPI
                   .post(ENDPOINT.CREATE_PRODUCT_WITH_IMAGE, formData)
                   .then((response) => {
                       resolve(response.data);
                   })
                   .catch((error) => {
                       reject(error);
                   });
           });
       },

        fetchProductbySeller({commit}, sellerId){
            console.log("masuk sellerproduct")
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.GET_SELLER_PRODUCT, sellerId)
                    .then((response) => {
                        commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },

        fetchProduct({commit}){
            console.log("masuk fetch product")
            return new Promise((resolve, reject) => {
                getAPI
                    .get(ENDPOINT.GET_ALL_PRODUCT)
                    .then((response) => {
                        commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },
        fetchProductbyId({commit}, productId){
            console.log("masuk fetch product by id")
            return new Promise((resolve, reject) => {
                getAPI
                    .get(ENDPOINT.GET_ALL_PRODUCT.concat(productId, "/"))
                    .then((response) => {
                        commit("SET_PRODUCT_DATA", response.data);
                        console.log("data di get by id", this.productData)
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },    
        fetchProductbyCategory({commit}, categoryId){
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.GET_CATEGORY_PRODUCT, categoryId)
                    .then((response) => {
                        commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },    
        deleteProductbyId({commit}, productId){
            console.log("masuk delete product by id")
            return new Promise((resolve, reject) => {
                getAPI
                    .delete(ENDPOINT.GET_ALL_PRODUCT.concat(productId, "/"))
                    .then((response) => {
                       // commit("SET_PRODUCT_DATA", response.data);
                        //console.log("data di get by id", this.productData)
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            });
        },
        clickFavorite({commit},body){
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.FAVORITE,body)
                    .then((response)=>{
                        commit("SET_PRODUCT_DATA",response.data)
                        resolve(response.data);
                    })
                    .catch((error)=>{
                        reject(error);
                    })
            })
          },
        updateProductData({ commit }, productData) {
            console.log("masuk update product")
            //console.log(productId)

           let formData = new FormData();
           formData.append('name', productData.name);
           formData.append('productDescription', productData.productDescription);
           formData.append('price', productData.price);
           formData.append('preorderTime', productData.preorderTime);
           formData.append('category', productData.category);
           productData.productPhoto.forEach(photo => {
               formData.append('image', photo, photo.name);
           });
           return new Promise((resolve, reject) => {
               getAPI
                   .patch(ENDPOINT.GET_ALL_PRODUCT.concat(productData.id, '/'), formData)
                   .then((response) => {
                       resolve(response.data);
                   })
                   .catch((error) => {
                       reject(error);
                   });
           });
       },
        fetchFavoriteById({ commit }, body) {
            return new Promise((resolve, reject) => {
                getAPI
                    .post(ENDPOINT.FAVORITE + 'user/', body)
                    .then((response) => {
                        console.log(response.data)
                        commit("SET_PRODUCT_DATA", response.data);
                        resolve(response.data);
                    })
                    .catch((error) => {
                        reject(error);
                    });
            })
        }
    },
};

export default product;