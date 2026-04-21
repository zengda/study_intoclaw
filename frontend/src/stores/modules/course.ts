import { defineStore } from 'pinia'
import { courseApi } from '@/api/modules/courses'
import type { Course, CourseDetail } from '@/api/types'

export const useCourseStore = defineStore('course', {
  state: () => ({
    courses: [] as Course[],
    currentCourse: null as CourseDetail | null,
    isLoading: false,
    error: null as string | null
  }),
  
  actions: {
    async fetchCourses() {
      this.isLoading = true
      this.error = null
      
      try {
        const response = await courseApi.getCourses()
        this.courses = response.data
      } catch (error: any) {
        this.error = error.response?.data?.detail || '获取课程列表失败'
      } finally {
        this.isLoading = false
      }
    },
    
    async fetchCourseDetail(slug: string) {
      this.isLoading = true
      this.error = null
      
      try {
        const response = await courseApi.getCourseDetail(slug)
        this.currentCourse = response.data
      } catch (error: any) {
        this.error = error.response?.data?.detail || '获取课程详情失败'
      } finally {
        this.isLoading = false
      }
    }
  }
})