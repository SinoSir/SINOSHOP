# CALOS 接口契约 / CALOS SPECIFICATION

> **状态：** 公开接口定义 | **版本：** V1.0  
> 本文件定义 SINOSHOP 数字层与 CALOS 物理系统之间的数据交换格式。  
> CALOS 物理系统的具体实现存放于 `SinoSir/CALOS_OpenSources`。

---

## 1. 概述

CALOS（恒定高度控制系统）负责管理 SINOSHOP 跨海通道的物理层——防波堤、浮力控制、结构监测。  
SINOSHOP 数字层通过 R16 协议总线从 CALOS 获取物理状态数据，进行数字孪生与资产确权。

**核心原则：**
- CALOS 是物理数据的**提供者**，SINOSHOP 是数据的**消费者与治理者**。
- 数据交换通过标准化 API 完成，双方独立部署。
- CALOS 的核心控制算法属于 L3 资产，本文件仅定义接口。

---

## 2. 数据交换模型
