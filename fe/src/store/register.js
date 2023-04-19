import store from ".";
import { getAPI } from "@/plugins/axios-api.js";
import Swal from "sweetalert2";

const ENDPOINT = {
    REGIS: "user/",
};


const register = {
    namespaced: true,
    state:{
        userData:{
            username: "",
            password: "",
            name: "",
            role: null,
            phone: "",
            email:""
        }
    },
    mutations:{
    },
    actions:{
        postUser({commit},body){
            console.log("body",body)
            return new Promise((resolve, reject) => {
                getAPI
                  .post(ENDPOINT.REGIS, body)
                  .then((response) => {
                    Swal.fire({
                        icon: "success",
                        title: "User succesfully registered",
                        text: "",
                        footer:
                          "<small>Thankyou for joining us</small>",
                      });
                    resolve(response.data);
                  })
                  .catch((error) => {
                    console.log(error)
                    Swal.fire({
                        icon: "error",
                        title: "Username already exist",
                        text: "Username has to be unique",
                        footer:
                          "<small>If this problem persists, please contact Admin</small>",
                      });
                  });
              });
        }
    }
};
export default register;