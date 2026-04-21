import { defineStore } from 'pinia'
import { authApi } from '@/api/modules/auth'
import type { UserInfo } from '@/api/types'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('access_token') || null,
    refreshToken: localStorage.getItem('refresh_token') || null,
    userInfo: null as UserInfo | null,
    isLoading: false,
    error: null as string | null
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token
  },
  
  actions: {
    async login(phone: string, password: string) {
      this.isLoading = true
      this.error = null
      
      try {
        const response = await authApi.login({ phone, password })
        const { access, refresh } = response.data
        
        this.token = access
        this.refreshToken = refresh
        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)
        
        await this.fetchUserInfo()
        return { success: true }
      } catch (error: any) {
        this.error = error.response?.data?.detail || '登录失败'
        return { success: false, error: this.error }
      } finally {
        this.isLoading = false
      }
    },
    
    async register(data: {
      phone: string
      nickName: string
      email: string
      password: string
    }) {
      this.isLoading = true
      this.error = null
      
      try {
        await authApi.register(data)
        return { success: true }
      } catch (error: any) {
        this.error = error.response?.data?.detail || '注册失败'
        return { success: false, error: this.error }
      } finally {
        this.isLoading = false
      }
    },
    
    async logout() {
      try {
        await authApi.logout()
      } catch (error) {
        console.error('Logout error:', error)
      } finally {
        this.token = null
        this.refreshToken = null
        this.userInfo = null
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
      }
    },
    
    async fetchUserInfo() {
      if (!this.token) return
      
      this.isLoading = true
      
      try {
        const response = await authApi.getUserInfo()
        this.userInfo = response.data
      } catch (error) {
        console.error('Fetch user info error:', error)
      } finally {
        this.isLoading = false
      }
    }
  },
  
  persist: {
    key: 'user-store',
    storage: localStorage,
    paths: ['token', 'refreshToken']
  }
})