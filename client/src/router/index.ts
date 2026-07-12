import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import SignUp from "../components/SignUp.vue";
import { useAuth } from "../composables/useAuth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home, meta: { requiresAuth: true } },
    { path: "/signup", component: SignUp },
    { path: "/login", component: Login, meta: { guestOnly: true } },
  ],
});

router.beforeEach(async (to) => {
  if (to.meta.guestOnly) {
    const { validateToken } = useAuth();
    const isAuthenticated = await validateToken();
    if (isAuthenticated) return "/";
  }
  if (to.meta.requiresAuth) {
    const { validateToken } = useAuth();
    const isAuthenticated = await validateToken();
    if (!isAuthenticated) return "/login";
  }
});

export default router;
