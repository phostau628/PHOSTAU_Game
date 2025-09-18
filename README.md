# PHOSTAU_Game

一款基于Pygame开发的纵向射击游戏，包含多种游戏模式和独特的BOSS战系统，玩家将在一波波敌人的攻势中生存并反击。

ps:本游戏尤其面向籽岷爱好者或战机类游戏爱好者，或两者兼之。


## 📖 项目文件说明：
- `src/`：存放游戏主程序（普通模式+挑战模式代码）
- `chart/`：存放所有游戏图片资源（玩家、敌人、BOSS素材）
- `introduction/`：存放游戏补充说明（如玩法细节、更新日志等，可选）


## 🎮 游戏简介
这是一款快节奏的纵向射击游戏，玩家需操控角色躲避敌人攻击并消灭所有对手，共20波关卡，每5波触发BOSS战，最终20波将面对双BOSS集群。随着波数推进，玩家火力会自动升级（射击角度增多、射速提升），两种难度模式满足不同玩家需求。


## ✨ 游戏特色
- **双模式体验**：普通模式（`src/Zimin_Fighter_normal.py`）难度适中，适合新手；挑战模式（`src/Zimin_Fighter_challenge.py`）敌人生命值更高，适合进阶玩家
- **渐进式火力系统**：1-5波基础单角度射击 → 6-10波多角度散射 → 11-15波宽幅覆盖 → 16-20波全屏攻击，无需手动解锁
- **5种独特BOSS**：每种BOSS有专属外观、生命值和弹幕模式（旋转弹、追踪弹、环形弹等），战斗策略差异化
- **动态视觉效果**：子弹带有渐隐拖尾轨迹，不同类型子弹对应专属颜色（如玩家弹浅灰、BOSS弹红色），提升沉浸感
- **智能敌人AI**：敌人会根据屏幕边界调整移动方向，避免卡在边缘，战斗流程更流畅


## 📋 角色与敌人设定
### 玩家角色
| 属性         | 普通模式 | 挑战模式 |
|--------------|----------|----------|
| 生命值       | 300点    | 320点    |
| 移动控制     | WASD键   | WASD键   |
| 攻击方式     | 空格键发射子弹（可长按） | 空格键发射子弹（可长按） |
| 移动范围     | 限制在1000×600像素屏幕内 | 限制在1000×600像素屏幕内 |

### 敌人类型
#### 1. 普通敌人
- 尺寸：60×60像素  
- 生命值：普通模式100点 / 挑战模式260点  
- 攻击方式：四向散射子弹（角度-135°、-45°、45°、135°）  
- 移动速度：水平±2像素/帧，垂直0.5-1.5像素/帧  

#### 2. BOSS敌人
| BOSS类型 | 尺寸     | 普通模式生命值 | 挑战模式生命值 | 移动速度（水平） | 子弹速度 | 核心攻击模式               |
|----------|----------|----------------|----------------|------------------|----------|----------------------------|
| 1号      | 140×140  | 500            | -              | ±3像素/帧        | 4        | 旋转弹幕（30°间隔，随时间旋转） |
| 2号      | 160×160  | 2222           | 3666           | ±2像素/帧        | 5        | 双向螺旋弹（正向+反向相位叠加） |
| 3号      | 180×180  | 6666           | 8888           | ±1.5像素/帧      | 6        | 散射弹+3发追踪弹（锁定玩家） |
| 4号      | 170×170  | 10000          | 12888          | ±4像素/帧        | 3        | 随机环形弹（18发无规律分布） |
| 5号      | 170×170  | 10000          | 16666          | ±3像素/帧        | 7        | 定向宽幅弹（7个固定角度覆盖） |


## 🚀 安装与运行
### 前置要求
- 操作系统：Windows/macOS/Linux  
- Python 版本：3.8 及以上  
- 依赖库：Pygame  


### 步骤1：获取项目代码
#### 方式1：Git克隆（推荐）
打开终端/命令提示符，执行以下命令，将项目下载到本地：
```bash
git clone https://github.com/phostau628/PHOSTAU_Game.git
cd PHOSTAU_Game  # 进入项目根目录（此时能看到src/、chart/、introduction/三个文件夹）
```

#### 方式2：下载ZIP压缩包（无Git时用）
1. 访问仓库地址：https://github.com/phostau628/PHOSTAU_Game.git  
2. 点击右上角「Code」→「Download ZIP」  
3. 解压压缩包，进入解压后的「PHOSTAU_Game」文件夹（确保根目录下有src/、chart/、introduction/）


### 步骤2：安装Pygame依赖
在项目根目录的终端/命令提示符中，执行以下命令安装游戏必需的Pygame库：
```bash
# Windows 系统
python -m pip install pygame

# macOS/Linux 系统（若python命令无效，替换为python3）
python3 -m pip install pygame
```


### 步骤3：启动游戏
#### 方式1：终端/命令提示符启动
- 普通模式：
  ```bash
  # Windows
  python src/Zimin_Fighter_normal.py

  # macOS/Linux
  python3 src/Zimin_Fighter_normal.py
  ```
- 挑战模式：
  ```bash
  # Windows
  python src/Zimin_Fighter_challenge.py

  # macOS/Linux
  python3 src/Zimin_Fighter_challenge.py
  ```

#### 方式2：VS Code启动（新手友好）
1. 用VS Code打开「PHOSTAU_Game」项目根目录（选择文件夹时直接选PHOSTAU_Game）  
2. 安装Python插件（搜索「Python」，选择微软官方版本）  
3. 在左侧「资源管理器」中展开`src`文件夹，双击打开对应模式的文件（如`Zimin_Fighter_normal.py`）  
4. 点击右上角绿色「运行Python文件」按钮，或按快捷键`Ctrl+F5`  


## 🕹️ 游戏操作指南
| 按键       | 功能                 |
|------------|----------------------|
| W          | 向上移动             |
| A          | 向左移动             |
| S          | 向下移动             |
| D          | 向右移动             |
| 空格键     | 发射子弹（长按可持续攻击） |
| 窗口关闭按钮 | 退出游戏             |


## ⚠️ 常见问题解决
### 1. 提示「缺少关键文件：XXX.jpg」
- 原因：`chart`文件夹路径错误，或图片文件缺失/重命名（代码默认从根目录的`chart/`读取图片）  
- 解决：  
  1. 确认`chart`文件夹在项目根目录下（路径：`PHOSTAU_Game/chart/`），而非`src/chart/`  
  2. 检查`chart`内是否有以下图片（文件名需完全一致，包括后缀）：  
     - 玩家图：`3D03487997CF31B6E196BCC5AD61E1D1.jpg`  
     - 普通敌人图：`5D12D4322F494C8D40ACB659FA2536DD.jpg`  
     - BOSS图：`2EF80F6C18C57E37D25365CA2A8E4FD6.jpg`、`62200DD83E5F8819034E6D058F452E5F.jpg`、`75CCE7B5E1B58922D3B49B6455844113.jpg`、`58EBE0C66C49A01BE71264AC79DD0AF0.jpg`、`2A5AFB066FB306E54DD6EDAB5EF294E6.jpg`  

### 2. 提示「ModuleNotFoundError: No module named 'pygame'」
- 原因：Pygame未安装，或安装的Python版本与运行版本不匹配  
- 解决：  
  1. 重新执行步骤2的Pygame安装命令  
  2. Windows系统若`python`无效，尝试`py -3.10 -m pip install pygame`（3.10替换为你的Python版本）；macOS/Linux用`python3`替代`python`  

### 3. 游戏窗口闪退，无报错提示
- 原因：Python版本低于3.8，或显卡驱动不支持Pygame渲染  
- 解决：  
  1. 升级Python到3.8及以上版本（推荐3.10，兼容性更好）  
  2. 以管理员身份启动终端/VS Code，再重新运行游戏  


## 📂 项目完整结构
```
PHOSTAU_Game/                  # 项目根目录
├─ src/                        # 源代码目录
│  ├─ Zimin_Fighter_normal.py  # 普通模式主程序（正确拼写normal）
│  └─ Zimin_Fighter_challenge.py # 挑战模式主程序
├─ chart/                      # 图片资源目录（与src并列）
│  ├─ 3D03487997CF31B6E196BCC5AD61E1D1.jpg  # 玩家角色图片
│  ├─ 5D12D4322F494C8D40ACB659FA2536DD.jpg  # 普通敌人图片
│  ├─ 2EF80F6C18C57E37D25365CA2A8E4FD6.jpg  # BOSS 1图片
│  ├─ 62200DD83E5F8819034E6D058F452E5F.jpg  # BOSS 2图片
│  ├─ 75CCE7B5E1B58922D3B49B6455844113.jpg  # BOSS 3图片
│  ├─ 58EBE0C66C49A01BE71264AC79DD0AF0.jpg  # BOSS 4图片
│  └─ 2A5AFB066FB306E54DD6EDAB5EF294E6.jpg  # BOSS 5图片
├─ introduction/               # 补充说明目录（与src/chart并列，可选）
│  └─ （可放玩法细节、更新日志等文件）
└─ README.md                   # 游戏说明文档（当前文件）
```
```
