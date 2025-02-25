# CDS524 基于Q-learning强化学习算法的迷宫导航游戏，智能体通过探索环境学习最优路径策略。

## 功能特性

- 可交互式迷宫环境（5x5网格）
- 实现Q-learning算法（含epsilon-greedy策略）
- 实时可视化智能体移动路径
- 可配置的迷宫布局和算法参数
- 支持训练过程监控和结果可视化

## 安装指南

### 依赖环境
```bash
安装依赖：
pip install pygame numpy
启动程序：
python maze_q_learning.py
```
*requirements.txt*
```
numpy==1.21.5
pygame==2.1.3
```

### 快速启动
```bash
# 训练并运行带UI的版本
python main.py --train --episodes 1000 --render

# 仅运行预训练模型
python main.py --render
```

## 项目结构
```
├── maze_env.py         # 迷宫环境类（状态/奖励定义）
├── q_learning_agent.py # Q-learning算法实现
├── maze_ui.py          # Pygame可视化模块
├── main.py             # 主程序入口
├── pretrained          # 预训练模型
│   └── q_table.npy
└── config.yaml         # 参数配置文件
```
## 界面说明
```
蓝色圆点: 智能体位置
颜色编码:
绿色: 起点
红色: 终点
紫色: 陷阱
黑色: 墙壁
```

## 参数配置
```yaml
# config.yaml
learning_rate: 0.5      # 学习率 α
discount_factor: 0.9    # 折扣因子 γ
exploration_rate: 0.2   # 探索率 ε
episodes: 1000          # 训练轮次
maze_layout:            # 自定义迷宫布局
  - [1,1,1,1,1]
  - [1,2,0,4,1]
  - [1,1,0,0,1]
  - [1,0,0,4,1]
  - [1,3,1,1,1]

```
奖励函数设计：

终点奖励：+100
陷阱惩罚：-50
撞墙惩罚：-10
每步移动惩罚：-1（鼓励最短路径）
超参数调优：
```
```
agent = QLearningAgent(env, alpha=0.5, gamma=0.95, epsilon=0.2)
收敛性检查：
观察Q值是否趋于稳定
测试成功率是否达到阈值（>90%）
```

```

## 可视化界面
```
可视化界面：
蓝色圆点表示智能体
绿色为起点，红色为终点
紫色为陷阱，黑色为墙壁
智能体会自动演示最优路径
```
![Maze UI Demo](docs/ui_demo.gif)  <!--  -->
![1](https://github.com/user-attachments/assets/7d5b2b36-268f-41cf-bff9-523782ad12ef)

## 核心算法
Q-learning更新规则：
```math
Q(s,a) ← (1-α)Q(s,a) + α[r + γ max_{a'}Q(s',a')]
```

运行效果
控制台输出：
```
开始训练...
训练进度: 0/500
训练进度: 100/500
训练进度: 200/500
训练进度: 300/500
训练进度: 400/500
训练完成，开始演示!
```


