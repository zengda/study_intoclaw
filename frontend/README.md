# Study Intoclaw 前端项目

## 技术栈
- 构建工具：Vite 5+
- 框架：Vue 3（Composition API + `<script setup>` 语法）
- 语言：TypeScript（严格模式）
- 路由：Vue Router 4（history 模式）
- 状态管理：Pinia（配合持久化插件）
- HTTP 请求：Axios（统一拦截器，支持 Token 自动注入）
- UI 组件库：Element Plus（按需自动导入）
- CSS 方案：SCSS + UnoCSS
- 代码规范：ESLint + Prettier + Husky（配置 lint-staged）

## 目录结构

```
frontend/
├── public/ # 静态资源（不经过构建）
├── src/
│ ├── api/ # API 接口模块
│ │ ├── modules/ # 按业务拆分的接口
│ │ ├── request.ts # Axios 实例配置
│ │ └── types.ts # 接口响应类型定义
│ ├── assets/ # 需要构建的资源
│ │ ├── styles/ # 样式文件
│ ├── components/ # 通用组件
│ ├── composables/ # 组合式函数
│ ├── router/ # 路由配置
│ ├── stores/ # Pinia 状态管理
│ ├── types/ # 全局 TypeScript 类型定义
│ ├── utils/ # 工具函数
│ ├── views/ # 页面组件
│ ├── App.vue
│ └── main.ts
├── .env.development
├── .env.production
├── .eslintrc.cjs
├── .prettierrc
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

## 安装依赖

```bash
cd frontend
npm install
```

## 启动开发服务器

```bash
npm run dev
```

访问地址：`http://localhost:5173`

## 构建生产版本

```bash
npm run build
```

构建产物将输出到 `dist` 目录

## 代码规范

### 运行 ESLint

```bash
npm run lint
```

### 运行 Prettier

```bash
npm run format
```

## 环境变量

- `.env.development`：开发环境配置
- `.env.production`：生产环境配置

## 注意事项

1. 确保后端服务运行在 `http://localhost:8000`
2. 前端 API 代理已配置为 `/api` 指向后端服务
3. 登录后会自动保存 token 到本地存储
4. 支持自动刷新 token

## 功能模块

### 公开模块
- 首页（课程推荐、轮播图）
- 课程列表（支持搜索）
- 课程详情（包含课程介绍、章节列表、教师信息）
- 用户登录/注册（JWT 认证）

### 学员模块（需登录）
- 个人中心（资料修改、头像上传）
- 我的课程（已购/已选课程列表，学习进度）
- 课程播放页面（视频播放器、章节切换、笔记）
- 测验页面（单选题/多选题，自动计时与评分）
- 问答社区（课程内提问与回答）

### 教师/管理员模块（预留）
- 课程管理（创建/编辑课程，上传视频）
- 数据看板（选课统计、收入概览）