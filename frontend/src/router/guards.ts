import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/modules/user'

/**
 * 设置路由守卫
 */
export function setupGuards(router: ReturnType<typeof createRouter>) {
  router.beforeEach(async (to, from, next) => {
    // 设置页面标题
    if (to.meta.title) {
      document.title = `${to.meta.title} - Study Intoclaw`
    }

    const userStore = useUserStore()
    const requiresAuth = to.meta.requiresAuth !== false

    // 检查是否需要登录
    if (requiresAuth && !userStore.isLoggedIn) {
      // 跳转到登录页
      next({ name: 'Login', query: { redirect: to.fullPath } })
      return
    }

    // 已登录用户不能访问登录/注册页
    if (userStore.isLoggedIn && (to.name === 'Login' || to.name === 'Register')) {
      next({ name: 'Home' })
      return
    }

    next()
  })

  router.afterEach(() => {
    // 页面加载完成后的处理
  })
}