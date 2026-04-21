import request from '../request'
import type { LoginRequest, LoginResponse, RegisterRequest, UserInfo, ApiResponse } from '../types'

export const authApi = {
  /**
   * 用户登录
   */
  login: (data: LoginRequest) => {
    return request.post<ApiResponse<LoginResponse>>('/v1/auth/login/', data)
  },
  
  /**
   * 用户注册
   */
  register: (data: RegisterRequest) => {
    return request.post<ApiResponse>('/v1/auth/register/', data)
  },
  
  /**
   * 用户登出
   */
  logout: () => {
    return request.post<ApiResponse>('/v1/auth/logout/')
  },
  
  /**
   * 获取用户信息
   */
  getUserInfo: () => {
    return request.get<ApiResponse<UserInfo>>('/v1/users/me/')
  }
}