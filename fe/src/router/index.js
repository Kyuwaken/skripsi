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
    component: () => import("../views/SellerRegistration.vue")
  },
  {
    path: "/sellerprofile",
    name: "sellerprofile",
    component: () => import("../views/SellerProfile.vue")
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue")
  },
  {
    path: "/sellereditprofile",
    name: "sellereditprofile",
    component: () => import("../views/SellerEditProfile.vue")
  },
  {
    path: "/sellerproduct",
    name: "sellereditprofile",
    component: () => import("../views/Product/SellerProduct.vue")
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
