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
pip install -r requirements.txt
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

agent = QLearningAgent(env, alpha=0.5, gamma=0.95, epsilon=0.2)
收敛性检查：

观察Q值是否趋于稳定
测试成功率是否达到阈值（>90%）


### 训练过程
```bash
Episode 500/1000 | Success rate: 72% | Avg steps: 18.3
Episode 1000/1000 | Success rate: 93% | Avg steps: 11.7
```

### 可视化界面
![Maze UI Demo](docs/ui_demo.gif)  <!-- 需替换为实际截图 -->

## 核心算法
Q-learning更新规则：
```math
Q(s,a) ← (1-α)Q(s,a) + α[r + γ max_{a'}Q(s',a')]
```

## 常见问题
**Q: 智能体卡在局部最优解怎么办？**  
A: 尝试：
1. 增加探索率（`exploration_rate` > 0.3）
2. 调整奖励函数（陷阱惩罚增强）
3. 延长训练周期（`episodes` > 2000）

**Q: 如何修改迷宫布局？**  
1. 在`config.yaml`中编辑`maze_layout`
2. 确保包含唯一起点(2)和终点(3)
3. 保持5x5的矩阵格式


