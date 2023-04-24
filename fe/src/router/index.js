import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import("../views/Login.vue")
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUp.vue')
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
    path: '/productdetail',
    name: 'productdetail',
    component: () => import('../views/ProductDetail.vue')
  },
  {
    path: '/customerprofile',
    name: 'customerprofile',
    component: () => import('../views/CustomerPages/CustomerProfile.vue')
  },
  {
    path: '/customerhome',
    name: 'customerhome',
    component: () => import('../views/CustomerPages/CustomerHome.vue'),
    props: true
  },
  {
    path: '/customerregistration',
    name: 'customerregistration',
    component: () => import('../views/CustomerPages/CustomerRegistration.vue')
  },
  {
    path: '/customereditprofile',
    name: 'customereditprofile',
    component: () => import('../views/CustomerPages/CustomerEditProfile.vue')
  },
  {
    path: '/customerfavorite',
    name: 'customerfavorite',
    component: () => import('../views/CustomerPages/CustomerFavorite.vue')
  },
  {
    path: '/customercart',
    name: 'customercart',
    component: () => import('../views/CustomerPages/CustomerCart.vue')
  },
  {
    path: '/customersearch',
    name: 'customersearch',
    component: () => import('../views/CustomerPages/CustomerSearch.vue')
  },
  {
    path: "/customerproductdetails",
    name: "customerproductdetails",
    component: () => import("../views/CustomerPages/CustomerProductDetails.vue"),
    props: true
  },  
  {
    path: "/sellerregistration",
    name: "sellerregistration",
    component: () => import("../views/SellerPages/SellerRegistration.vue")
  },
  {
    path: "/sellerprofile",
    name: "sellerprofile",
    component: () => import("../views/SellerPages/SellerProfile.vue")
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
  },  
  {
    path: "/sellertransactionlist",
    name: "sellertransactionlist",
    component: () => import("../views/SellerPages/SellerTransactionList.vue")
  },
  {
    path: "/sellerproductdetails",
    name: "sellerproductdetails",
    component: () => import("../views/SellerPages/SellerProductDetails.vue"),
    props: true
  },  
  {
    path: "/sellereditproduct",
    name: "sellereditproduct",
    component: () => import("../views/SellerPages/SellerEditProduct.vue"),
    props: true
  },  
  {
    path: "/testing",
    name: "xxxx",
    component: () => import("../views/CustomerPages/testcart.vue"),
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
