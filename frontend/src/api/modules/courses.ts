import request from '../request'
import type { Course, CourseDetail, Lesson, Review, ApiResponse } from '../types'

export const courseApi = {
  /**
   * 获取课程列表
   */
  getCourses: () => {
    return request.get<ApiResponse<Course[]>>('/v1/courses/')
  },
  
  /**
   * 获取课程详情
   */
  getCourseDetail: (slug: string) => {
    return request.get<ApiResponse<CourseDetail>>(`/v1/courses/${slug}/`)
  },
  
  /**
   * 获取课程章节
   */
  getCourseLessons: (slug: string) => {
    return request.get<ApiResponse<Lesson[]>>(`/v1/courses/${slug}/lessons/`)
  },
  
  /**
   * 获取课程评价
   */
  getCourseReviews: (slug: string) => {
    return request.get<ApiResponse<Review[]>>(`/v1/courses/${slug}/reviews/`)
  },
  
  /**
   * 提交课程评价
   */
  submitCourseReview: (slug: string, data: { content: string; rating: number }) => {
    return request.post<ApiResponse<Review>>(`/v1/courses/${slug}/reviews/`, data)
  }
}