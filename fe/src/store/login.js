import store from ".";
import { getAPI } from "@/plugins/axios-api.js";

const ENDPOINT = {
    LOGIN: "login/",
    LOGOUT: "/logout/",
};


const login = {
    namespaced: true,
    state:{
        loginData:{
            id:"",
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
            console.log("body",body)
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
        },
        logOut({commit}){
            return new Promise((resolve, reject) => {
                getAPI
                  .get(ENDPOINT.LOGOUT)
                  .then((response) => {
                    // commit("SET_LOGIN", response.data);
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