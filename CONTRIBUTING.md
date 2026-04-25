# 贡献者指南 (Contributing Guide)

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
