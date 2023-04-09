import Vue from 'vue';
import Vuex from 'vuex';
import Swal from "sweetalert2";
import login from "./login";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    alertError({ _commit }, { errorMsg, error }) {
      Swal.fire({
        icon: "error",
        title: errorMsg,
        text: error,
      });
    },
    alertSuccess({ _commit }, { title, text }) {
      Swal.fire({
        icon: "success",
        title: title,
        text: text,
      });
    },
  },
  modules: {
    login
  }
})
