"""
Q-learning迷宫游戏完整实现
运行命令：python maze_q_learning.py
"""

import pygame
import numpy as np

# ================= 迷宫环境 =================
class MazeEnv:
    def __init__(self):
        # 迷宫地图 (0:路, 1:墙, 2:起点, 3:终点, 4:陷阱)
        self.grid = [
            [1, 1, 1, 1, 1],
            [1, 2, 0, 4, 1],
            [1, 1, 0, 0, 1],
            [1, 0, 0, 4, 1],
            [1, 3, 1, 1, 1]
        ]
        self.start = (1, 1)
        self.end = (4, 1)
        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state
    
    def step(self, action):
        moves = [(-1,0), (0,1), (1,0), (0,-1)]  # 上,右,下,左
        new_row = self.state[0] + moves[action][0]
        new_col = self.state[1] + moves[action][1]
        
        if 0 <= new_row < 5 and 0 <= new_col < 5:
            cell = self.grid[new_row][new_col]
            if cell == 3:    # 到达终点
                return (new_row, new_col), 100, True
            elif cell == 4:  # 陷阱
                return (new_row, new_col), -50, False
            elif cell == 1:  # 撞墙
                return self.state, -10, False
            else:            # 正常移动
                self.state = (new_row, new_col)
                return self.state, -1, False
        else:                # 越界
            return self.state, -10, False

# ================= Q-learning算法 =================
class QLearningAgent:
    def __init__(self, env):
        self.env = env
        self.q_table = np.zeros((5, 5, 4))  # 状态空间5x5，4个动作
        
        # 超参数
        self.alpha = 0.5   # 学习率
        self.gamma = 0.9   # 折扣因子
        self.epsilon = 0.3 # 探索率

    def choose_action(self, state):
        # ε-greedy策略
        if np.random.random() < self.epsilon:
            return np.random.choice(4)  # 随机探索
        else:
            return np.argmax(self.q_table[state[0], state[1], :])  # 利用

    def update_q_table(self, state, action, reward, new_state):
        # Q值更新公式
        old_value = self.q_table[state[0], state[1], action]
        next_max = np.max(self.q_table[new_state[0], new_state[1], :])
        new_value = (1 - self.alpha)*old_value + self.alpha*(reward + self.gamma*next_max)
        self.q_table[state[0], state[1], action] = new_value

# ================= 游戏界面 =================
class MazeUI:
    def __init__(self, env):
        pygame.init()
        self.env = env
        self.cell_size = 60
        self.window = pygame.display.set_mode((5*self.cell_size, 5*self.cell_size))
        pygame.display.set_caption("Q-learning迷宫")
        
        # 颜色配置
        self.colors = {
            0: (255, 255, 255),  # 路
            1: (0, 0, 0),        # 墙
            2: (0, 255, 0),      # 起点
            3: (255, 0, 0),      # 终点
            4: (128, 0, 128),    # 陷阱
            "agent": (0, 0, 255) # 智能体
        }
    
    def draw(self, agent_pos):
        # 绘制网格
        for i in range(5):
            for j in range(5):
                color = self.colors[self.env.grid[i][j]]
                pygame.draw.rect(self.window, color, 
                               (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
        
        # 绘制智能体
        pygame.draw.circle(self.window, self.colors["agent"],
                          (agent_pos[1]*self.cell_size + self.cell_size//2,
                           agent_pos[0]*self.cell_size + self.cell_size//2),
                           self.cell_size//3)
        pygame.display.update()

# ================= 主程序 =================
def main():
    # 初始化
    env = MazeEnv()
    agent = QLearningAgent(env)
    ui = MazeUI(env)
    clock = pygame.time.Clock()
    
    # 训练参数
    episodes = 500
    
    # 训练阶段
    print("开始训练...")
    for episode in range(episodes):
        state = env.reset()
        done = False
        
        while not done:
            action = agent.choose_action(state)
            new_state, reward, done = env.step(action)
            agent.update_q_table(state, action, reward, new_state)
            state = new_state
        
        # 每100轮显示进度
        if episode % 100 == 0:
            print(f"训练进度: {episode}/{episodes}")
    
    # 测试阶段
    print("训练完成，开始演示!")
    state = env.reset()
    done = False
    while not done:
        # 处理退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # 选择动作
        action = np.argmax(agent.q_table[state[0], state[1], :])
        state, reward, done = env.step(action)
        
        # 更新界面
        ui.draw(state)
        clock.tick(5)  # 控制演示速度为5帧/秒
        
    pygame.time.wait(2000)  # 成功时保持2秒
    pygame.quit()

if __name__ == "__main__":
    main()