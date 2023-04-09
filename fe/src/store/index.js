import Vue from 'vue';
import Vuex from 'vuex';
import Swal from "sweetalert2";
import login from "./login";

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    seller: {
      name: 'John Doe',
      country: 'us',
      username: 'username',
      email: 'emailini',
      phoneNumber: '09823409823',
      description: 'menjual barang bekas'
    }
  },
  mutations: {
    SET_SELLER(state, seller) {
      state.seller = seller
    }
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

export default store
