import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    theme: 'light' as 'light' | 'dark',
    sidebar: {
      opened: true,
      withoutAnimation: false
    },
    loading: false
  }),
  
  actions: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light'
      document.documentElement.classList.toggle('dark', this.theme === 'dark')
    },
    
    toggleSidebar() {
      this.sidebar.opened = !this.sidebar.opened
      this.sidebar.withoutAnimation = false
    },
    
    setLoading(loading: boolean) {
      this.loading = loading
    }
  },
  
  persist: {
    key: 'app-store',
    storage: localStorage,
    paths: ['theme', 'sidebar']
  }
})