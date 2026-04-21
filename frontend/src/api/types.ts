// API 响应类型
export interface ApiResponse<T = any> {
  data: T
  message?: string
  code?: number
}

// 用户相关类型
export interface UserInfo {
  id: number
  phone: string
  nickName: string
  email: string
  avatarUrl?: string
  regtime: string
  last_time: string
  state: number
}

// 课程相关类型
export interface Course {
  id: number
  title: string
  description: string
  price: number
  slug: string
  cover?: string
  thumbnail?: string
  students: number
  created_at: string
}

export interface CourseDetail extends Course {
  content: string
  teacher: {
    id: number
    name: string
    avatar: string
    bio: string
  }
  lessons: Lesson[]
  reviews: Review[]
}

export interface Lesson {
  id: number
  title: string
  content: string
  duration: string
  order: number
  video_url: string
}

export interface Review {
  id: number
  user_id: number
  user_name: string
  content: string
  rating: number
  created_at: string
}

// 订单相关类型
export interface Order {
  order_no: string
  amount: number
  status: string
  created_at: string
  items: OrderItem[]
}

export interface OrderItem {
  course_id: number
  title: string
  price: number
}

// 支付相关类型
export interface Payment {
  payment_no: string
  order_no: string
  amount: number
  status: string
  channel: string
  pay_url: string
  created_at: string
}

// 登录请求
export interface LoginRequest {
  phone: string
  password: string
}

// 注册请求
export interface RegisterRequest {
  phone: string
  nickName: string
  email: string
  password: string
}

// 登录响应
export interface LoginResponse {
  access: string
  refresh: string
}