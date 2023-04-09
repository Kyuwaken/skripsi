import store from ".";
import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    LOGIN: "login/",
};


const login = {
    namespaced: true,
    state:{
        loginData:{
            username:"",
            name:"",
            role:""
        }
    },
    mutations:{
        SET_LOGIN(state,loginData){
            state.loginData = loginData
        },
    },
    actions:{
        postLogin({commit},body){
            return new Promise((resolve, reject) => {
                getAPI
                  .post(ENDPOINT.LOGIN, body)
                  .then((response) => {
                    commit("SET_LOGIN", response.data);
                    // commit("SET_USERNAME", response.data["username"]);
                    // commit("SET_NAME", response.data["name"]);
                    // commit("SET_ROLE", response.data["role"]);
                    resolve(response.data);
                  })
                  .catch((error) => {
                    reject(error);
                  });
              });
        }
    }
};
export default login;