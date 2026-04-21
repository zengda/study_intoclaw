import { createPinia } from 'pinia'

export const pinia = createPinia()

export * from './modules/user'
export * from './modules/course'
export * from './modules/app'