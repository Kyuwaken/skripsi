import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/customerprofile',
    name: 'customerprofile',
    component: () => import('../views/CustomerProfile.vue')
  },
  {
    path: '/customerhome',
    name: 'customerhome',
    component: () => import('../views/CustomerHome.vue')
  },
  {
    path: '/customerregistration',
    name: 'customerregis',
    component: () => import('../views/CustomerRegistration.vue')
  },
  {
    path: '/customereditprofile',
    name: 'customereditprofile',
    component: () => import('../views/CustomerEditProfile.vue')
  },
  {
    path: "/sellerregistration",
    name: "sellerregis",
    component: () => import("../views/SellerPages/SellerRegistration.vue")
  },
  {
    path: "/sellerprofile",
    name: "sellerprofile",
    component: () => import("../views/SellerPages/SellerProfile.vue")
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue")
  },
  {
    path: "/sellereditprofile",
    name: "sellereditprofile",
    component: () => import("../views/SellerPages/SellerEditProfile.vue")
  },
  {
    path: "/sellerproduct",
    name: "sellerproduct",
    component: () => import("../views/SellerPages/SellerProduct.vue")
  },
  {
    path: "/addproduct",
    name: "addproduct",
    component: () => import("../views/SellerPages/AddProduct.vue")
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
