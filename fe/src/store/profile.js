import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    USER: "/user/",
};

const profile = {
    namespaced: true,
    state: {
        profileData: {
            username:"",
            name:"",
            role:{},
            phone:"",
            email:"",
            country:{}
        },
    },
    mutations: {
        SET_PROFILE_DATA(state, profileData) {
            state.profileData = profileData;
        },
    },
    actions: {
        getProfileData({ commit },id) {
            return new Promise((resolve, reject) => {
              getAPI(ENDPOINT.USER +id+"/")
                .then((response) => {
                  console.log("masuk js category")
                  // const categories = response.data.map((category) => ({
                  //   id: category.id,
                  //   name: category.name,
                  // }));
                  commit("SET_PROFILE_DATA", response.data);
                  resolve(response);
                })
                .catch((error) => {
                  reject(error);
                });
            });
        },
        updateProfileData({commit},data){
            console.log(data)
            return new Promise((resolve,reject)=>{
                getAPI
                .patch(ENDPOINT.USER+data.id+"/",data.body)
                .then((response)=>{
                    resolve(response.data)
                })
            })
        }

    },
};

export default profile;