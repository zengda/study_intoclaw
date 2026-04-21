// 路由配置
export const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/home/index.vue'),
    meta: {
      title: '首页',
      requiresAuth: false
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/user/login.vue'),
    meta: {
      title: '登录',
      requiresAuth: false
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/user/register.vue'),
    meta: {
      title: '注册',
      requiresAuth: false
    }
  },
  {
    path: '/courses',
    name: 'Courses',
    component: () => import('@/views/course/list.vue'),
    meta: {
      title: '课程列表',
      requiresAuth: false
    }
  },
  {
    path: '/course/:slug',
    name: 'CourseDetail',
    component: () => import('@/views/course/detail.vue'),
    meta: {
      title: '课程详情',
      requiresAuth: false
    }
  },
  {
    path: '/user/profile',
    name: 'UserProfile',
    component: () => import('@/views/user/profile.vue'),
    meta: {
      title: '个人中心',
      requiresAuth: true
    }
  },
  {
    path: '/user/courses',
    name: 'UserCourses',
    component: () => import('@/views/user/courses.vue'),
    meta: {
      title: '我的课程',
      requiresAuth: true
    }
  },
  {
    path: '/player/:courseId',
    name: 'CoursePlayer',
    component: () => import('@/views/course/player.vue'),
    meta: {
      title: '课程播放',
      requiresAuth: true
    }
  },
  {
    path: '/payment',
    name: 'Payment',
    component: () => import('@/views/payment/index.vue'),
    meta: {
      title: '支付',
      requiresAuth: true
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/error/404.vue'),
    meta: {
      title: '404',
      requiresAuth: false
    }
  }
]