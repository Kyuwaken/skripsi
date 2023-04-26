import { getAPI, employeeAPI } from "@/plugins/axios-api";
import router from "@/router";
import store from "@/store";
import crypto from "./crypto";
// import { encrypt, now } from "./Fernet";

import Swal from "sweetalert2";

function interceptSuccess(response) {
  if (
    response.status === 200 ||
    response.status === 201 ||
    response.status === 204
  ) {
    return Promise.resolve(response);
  } else {
    console.log("masuk error1")

    return Promise.reject(response);
  }
}

function interceptError(error) {
  // if error has no response
  if (!error.response) {
    alertError(
      "Connection Error",
      "Please check your internet connection or try again later"
    );
  }
  // error has response has status code
  else if (error.response.status) {
    switch (error.response.status) {
      case 400:
        // bad request
        break;
      case 401:
        // 401 - unauthorized
        alertError("Error Login", "Incorrect username or password");
        store
          .dispatch("auth/logout", false)
          .then(() => router.push({ name: "sso" }));
        break;
      case 404:
        // not found
        break;
      default:
        alertError("Unknown Error", "Please try again later");
        break;
    }
  } else {
    alertError("Unknown Error", "Please try again later");
  }
  return Promise.reject(error);
}

function alertError(title, text, timer = 3000, timerProgressBar = true) {
  Swal.fire({
    icon: "error",
    title: title,
    text: text,
    timer: timer,
    timerProgressBar: timerProgressBar,
    footer:
      "<small>If this problem persists, please contact Admin</small>",
  });
}

// const salt = "@@@@";

export default function interceptors() {
  // const tokenEmployee = process.env.VUE_APP_APIKEY;
  // intercept requests, adds token to request header
  getAPI.interceptors.request.use(
    (config) => {
      var token = localStorage.getItem('encryptedData')
      if (token) {
        var data = crypto.methods.decryptLocalStorage(token);
        var id = data.id.toString()
        var tokens = crypto.methods.encryptData(id)
        config.headers["Authorization"] = `Token ${tokens}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  // intercept responses
  getAPI.interceptors.response.use(
    (response) => {
      console.log("masuk")
      return interceptSuccess(response);
    },
    (error) => {
      console.log("masuk error")

      return interceptError(error);
    }
  );

  // intercept requests, adds token to request header
  // employeeAPI.interceptors.request.use(
  //   (config) => {
  //     var token = encryptStorage.getItem("Token");
  //     let app_id = "PANDA_DASHBOARD_ITHC";
  //     if (token) {
  //       // append token with current datetime, then encrypt
  //       token = token + salt + now() + salt + app_id;
  //       token = encrypt(token);
  //       config.headers.common["Authorization"] = `Api-Key ${tokenEmployee}`;
  //       // config.headers.common["Client-ID"] = `Client ${token}`;
  //     }
  //     return config;
  //   },
  //   (error) => {
  //     return Promise.reject(error);
  //   }
  // );

  // intercept responses
  // employeeAPI.interceptors.response.use(
  //   (response) => {
  //     return interceptSuccess(response);
  //   },
  //   (error) => {
  //     return interceptError(error);
  //   }
  // );
}
