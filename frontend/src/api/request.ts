import axios from 'axios'
import type { AxiosRequestConfig, AxiosResponse } from 'axios'
import { useUserStore } from '@/stores/modules/user'
import router from '@/router'

// 创建 axios 实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const userStore = useUserStore()
    const token = userStore.token
    
    if (token) {
      config.headers = config.headers || {}
      config.headers.Authorization = `Bearer ${token}`
    }
    
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse) => {
    return response
  },
  async (error) => {
    if (error.response?.status === 401) {
      const userStore = useUserStore()
      const refreshToken = userStore.refreshToken
      
      if (refreshToken) {
        try {
          const response = await axios.post('/api/v1/auth/refresh/', {
            refresh: refreshToken
          })
          
          const { access, refresh } = response.data
          userStore.token = access
          userStore.refreshToken = refresh
          localStorage.setItem('access_token', access)
          localStorage.setItem('refresh_token', refresh)
          
          // 重新发送原请求
          error.config.headers.Authorization = `Bearer ${access}`
          return service(error.config)
        } catch (refreshError) {
          // 刷新失败，跳转到登录页
          await userStore.logout()
          router.push({ name: 'Login' })
        }
      } else {
        // 没有 refresh token，跳转到登录页
        await userStore.logout()
        router.push({ name: 'Login' })
      }
    }
    
    return Promise.reject(error)
  }
)

export default service