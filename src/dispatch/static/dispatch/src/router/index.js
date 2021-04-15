import Vue from "vue"
import Router from "vue-router"
import { publicRoute, protectedRoute } from "./config"

import store from "@/store"
import pkceAuthProvider from "@/auth/pkceAuthProvider"
import basicAuthProvider from "@/auth/basicAuthProvider"
import customAuthProvider from "@/auth/customAuthProvider"

const routes = protectedRoute.concat(publicRoute)

Vue.use(Router)

const router = new Router({
  mode: "history",
  linkActiveClass: "active",
  routes: routes,
})

const authProviderSlug =
  process.env.VUE_APP_DISPATCH_AUTHENTICATION_PROVIDER_SLUG || "dispatch-auth-provider-basic"

// router guards
router.beforeEach((to, from, next) => {
  store.dispatch("app/setLoading", true)
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.state.auth.currentUser.loggedIn) {
      if (authProviderSlug === "dispatch-auth-provider-pkce") {
        pkceAuthProvider.login(to, from, next)
      } else if (authProviderSlug === "dispatch-auth-provider-basic") {
        basicAuthProvider.login(to, from, next)
      } else {
        // defaults to none, allows custom providers
        customAuthProvider.login(to, from, next)
      }
    } else {
      next()
    }
  } else {
    next()
  }
})

function hasQueryParams(route) {
  return !!Object.keys(route.query).length
}

router.beforeEach((to, from, next) => {
  // We only want to automatically copy params when we are navigating
  // "project" subMenu's
  if (to.meta.subMenu === "project") {
    if (!hasQueryParams(to) && hasQueryParams(from)) {
      next({ name: to.name, query: from.query })
    } else {
      next()
    }
  }
  next()
})

router.afterEach(function () {
  store.dispatch("app/setLoading", false)
})

export default router
