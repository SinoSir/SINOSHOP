# 🌊 为 SINOSHOP 做出贡献 (Contributing to SINOSHOP)

> **觀天之道，執天之行。造福人民。**
> *Observe Nature's Order, Align with Ocean's Rhythm, Advance the People's Welfare.*

感谢你对 SINOSHOP 项目的关注！本指南旨在将你的才华转化为数字海洋的基石，确保每一行代码都符合 **物理精度的严苛** 与 **区块链的透明**。

---

## 🏗 贡献者能级模型 (Contributor Hierarchy)

我们通过能力证明（Proof of Capability）来分配访问权限，确保系统稳定性：

| 能级 | 角色定位 | 核心任务 | 准入条件 |
|---|---|---|---|
| **L1 先锋** | 算法挑战者 | 优化核心算法，提升物理仿真精度 | 成功完成 **Hero Task 001** (RMSD < 50mm) |
| **L2 构建者** | 协议贡献者 | 完善 R16 标准协议，维护 CI/CD 工具链 | 累积 3 个被合并的 Bugfix 或文档 PR |
| **L3 专家** | 工程实施者 | 治理合约迭代、底层物理引擎重构 | L1 资格 + 委员会提名 + 物理 CLA 签署 |

---

## 🧠 核心挑战：Hero Task 001 (入职基准)

**“这里没有平庸的代码，只有对精度的极致追求。”**

你的任务是优化 `compute()` 控制逻辑。

- **当前基准：** RMSD = 68mm (基于默认 PID 控制器)
- **目标要求：** **RMSD < 50mm**
- **技术约束：** 30s 惯性时滞，±30mm 执行器死区，高动态噪声

### 📈 推荐优化路径
1. **卡尔曼滤波**：减小传感器噪声干扰，提升数据质量。
2. **前馈补偿**：预测非线性海洋扰动力，抵消响应延迟。
3. **积分抗饱和**：在极端物理约束下保持控制器稳定性。

### ⚡ 快速启动环境 (零摩擦上手)

```bash
# 1. 克隆挑战仓库 (SINOSHOP-Core)
git clone https://github.com/SinoSir/SINOSHOP-Core.git
cd SINOSHOP-Core

# 2. 启动预装了所有依赖的容器化环境 (推荐)
docker-compose up -d environment
docker exec -it environment python run_demo.py

# 3. 本地运行 (若不使用 Docker)
pip install -r requirements.txt
python run_demo.py
📐 完整的挑战规则、评分细节与架构师破冰指南，请阅读 challenges/HERO_TASK_001.md。

🔄 标准协作工作流 (Workflow)
为了保持代码库的“整洁度”，我们严格执行以下流程。

1. 发现与对齐 (Identify)
在动手前，请先搜索 Issues。

如果是重大变更或新协议设计，请先提交 RFC (Request for Comments) Issue 与社区讨论。

2. 开发与验证 (Develop & Verify)
物理层测试：python -m pytest tests/physics/

合约层测试：forge test --gas-report

代码格式化：提交前运行 make lint (集成了 Ruff 和 Prettier)

3. 签署 CLA (法律合规)
所有代码贡献者必须同意项目根目录下的 CLA.pdf。
在你的首个 Pull Request 描述中，请第一行就加入以下声明：

I hereby agree to the SINOSHOP Contributor License Agreement (CLA.pdf).

4. 提交审查 (Review)
PR 必须通过以下全部检查：

CI/CD 流水线：所有自动化测试必须为绿色 (All Checks Passed)。

同行评审：至少获得一名核心维护者的 Approve。

🛡 安全与机密红线 (Hard Lines)
违反以下规则将导致账户直接列入灰名单，禁止参与后续贡献。

Secrets Exposure: 🚫 禁止提交任何 .env, *.pem, private_key 文件。测试用私钥请使用 Anvil 公开账户。

Hard-coded Thresholds: 🚫 禁止硬编码物理增益值 
K
s
y
n
c
K 
sync
​
 、
σ
t
h
r
e
s
h
o
l
d
σ 
threshold
​
  等。所有关键参数必须通过 config/ 或环境变量注入。

Shadow Logic: 🚫 禁止包含未经解释的二进制 Blob、闭源依赖或混淆代码。

如果你发现安全漏洞，请按 SECURITY.md 中的流程私下报告，切勿公开提及。

🏆 开发者荣誉体系
通过 L1 考核的贡献者，其 GitHub ID 将被永久记录在 HALL_OF_FAME.md 中，并获得核心团队公开致谢。

后续将考虑为顶级贡献者映射链上 Ocean Pioneer NFT，作为海洋城市早期共建者的永久证明。

貞忠昭日月，惠民播春秋。
Steadfast Loyalty glowing like the sun and moon; Benevolence nourishing the tide of time.

—— SINOSHOP 技术委员会# 贡献者指南 (Contributing Guide)

感谢你对构建海洋城市文明的统一数字度量衡产生兴趣。

## 什么是R16？

R16是一套面向海洋智慧城市基础设施的**底层编码、通信与控制协议**。它旨在终结深海基建的“数据诸侯割据”，建立全球统一的数字“度量衡”。

## 贡献者权利宪章

每一位贡献者享有：
- **署名权**：姓名永久写入协议 `Authors` 字段
- **知情权**：贡献处置决定须附带说明
- **参与权**：累计三次采纳可提名领域维护者
- **收益权**：按贡献锚点记录的权重分享长期收益
- **退出权**：停止贡献不丧失既有权利

## 快速入门

1. Fork 本仓库
2. 创建一个新分支：`git checkout -b feature/my-contribution`
3. 提交你的更改：`git commit -m '描述你的贡献'`
4. 推送到你的分支：`git push origin feature/my-contribution`
5. 提交 Pull Request

## 贡献流程

1. 查阅 [good-first-issue] 标签寻找入门任务
2. 通过 Issue 以 [R16-RFC] 前缀提交提案
3. 社区讨论 ≥ 14天
4. 核心团队使用 accepted / deferred / declined 标签决策
5. PR 必须包含测试用例，并通过 CI 扫描

## 机密边界（红线）

以下内容禁止在开源仓库提交：
- 工程阈值（如阻尼系数、频率参数）
- K_sync 精确计算逻辑
- 任何包含 `_threshold`, `_coeff`, `_formula` 的硬编码常量
- 具体的 PID 增益值或材料应力限值

完整机密清单见 [SECURITY.md](SECURITY.md)

## 贡献类型

| 类型 | 说明 | 示例 |
|:---|:---|:---|
| code | 代码贡献 | SDK、编码器、仿真沙箱 |
| doc | 文档贡献 | 协议规范、README、翻译 |
| test | 测试贡献 | 单元测试、HIL回归测试 |
| spec | 协议设计 | 编码格式、枚举表扩展 |
| review | 代码审查 | PR review反馈 |
| sim | 仿真贡献 | 沙箱模型、控制算法测试 |
| design | 架构设计 | ADR提案 |

## 联系

- 技术讨论：在 GitHub Issues 中提出
- 安全漏洞：standards@sinoshop.org
- 治理与协作：见 [GOVERNANCE.md](GOVERNANCE.md)

## 签署DCO

所有提交必须包含 Signed-off-by 声明：Liangzhenxiong SINOSHOP liangzhenxiong@gmail.com
20260502
